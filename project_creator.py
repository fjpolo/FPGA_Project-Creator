import os
import shutil
import re

def ignore_cocotb_env(src, names):
    """
    Function to be used with shutil.copytree's 'ignore' argument.
    It tells copytree to ignore the 'cocotb_env' directory if found.
    """
    ignored_names = []
    if 'cocotb_env' in names:
        ignored_names.append('cocotb_env')
        print(f"Ignoring 'cocotb_env' directory in {src} during copy.")
    return set(ignored_names)

def copy_template(template_dir, project_dir):
    """Copy the template directory to the new project directory, ignoring cocotb_env."""
    if os.path.exists(project_dir):
        raise FileExistsError(f"Project directory already exists: {project_dir}")
    # Use the ignore_cocotb_env function to skip the 'cocotb_env' directory
    shutil.copytree(template_dir, project_dir, ignore=ignore_cocotb_env)
    print(f"Copied template to new project directory: {project_dir}")

def rename_items(path, old_name, new_name):
    """Rename directories and files by replacing old_name with new_name."""
    # Rename directories first (depth-first to handle nested directories)
    for root, dirs, files in os.walk(path, topdown=False):
        for dir_name in dirs:
            if old_name.lower() in dir_name.lower():
                old_dir = os.path.join(root, dir_name)
                # Ensure we don't rename the newly created project directory's base itself prematurely
                # This regex ensures we only replace 'template' if it's part of a path segment or file/dir name
                new_dir_name = re.sub(r'\b' + re.escape(old_name) + r'\b', new_name, dir_name, flags=re.IGNORECASE)
                new_dir = os.path.join(root, new_dir_name)

                if old_dir != new_dir:
                    os.rename(old_dir, new_dir)
                    print(f"Renamed directory: {old_dir} -> {new_dir}")

        for file_name in files:
            if old_name.lower() in file_name.lower():
                old_file = os.path.join(root, file_name)
                new_file_name = re.sub(r'\b' + re.escape(old_name) + r'\b', new_name, file_name, flags=re.IGNORECASE)
                new_file = os.path.join(root, new_file_name)
                if old_file != new_file:
                    os.rename(old_file, new_file)
                    print(f"Renamed file: {old_file} -> {new_file}")

def replace_in_files(path, old_name, new_name):
    """Replace occurrences of old_name with new_name in file contents."""
    old_name_upper = old_name.upper()
    new_name_upper = new_name.upper()

    for root, _, files in os.walk(path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                
                # Replace old_name with new_name (case-insensitive word boundary to avoid partial replacements)
                new_content = re.sub(r'\b' + re.escape(old_name) + r'\b', new_name, content, flags=re.IGNORECASE)
                # Replace ALL_CAPS version without word boundary if necessary, adjust as needed
                new_content = re.sub(re.escape(old_name_upper), new_name_upper, new_content) # No word boundary for upper to catch TEMPLATE_VAR

                if new_content != content:
                    with open(file_path, 'w', encoding='utf-8') as file:
                        file.write(new_content)
                    print(f"Updated file: {file_path}")
            except (UnicodeDecodeError, IOError):
                print(f"Skipping binary or unreadable file: {file_path}")

def main():
    # Define the template directory
    template_dir = "./template"

    # Check if the template directory exists
    if not os.path.exists(template_dir):
        print(f"Template directory not found: {template_dir}")
        return

    # Ask the user for the project name
    project_name = input("Enter the project name: ").strip()
    if not project_name:
        print("Project name cannot be empty.")
        return

    # Define the new project directory
    project_dir = f"./{project_name}"

    try:
        # Step 1: Copy the template directory (ignoring cocotb_env)
        copy_template(template_dir, project_dir)

        # Step 2: Rename directories and files
        print("Renaming directories and files...")
        # Start renaming from the project_dir itself
        rename_items(project_dir, "template", project_name)

        # Step 3: Replace placeholders in files
        print("Replacing placeholders in files...")
        replace_in_files(project_dir, "template", project_name)

        print(f"Project '{project_name}' created successfully in '{project_dir}'.")
        print("\nIMPORTANT: The 'cocotb_env' virtual environment was not copied from the template.")
        print(f"Please navigate to '{project_dir}/amaranth/' and create/activate your virtual environment:")
        print(f"  cd {project_dir}/amaranth/")
        print("  python3 -m venv cocotb_env")
        print("  source cocotb_env/bin/activate")
        print("  pip install cocotb amaranth # Or your required dependencies")

    except FileExistsError as e:
        print(f"Error: {e}. Please remove the existing project directory or choose a different name.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
