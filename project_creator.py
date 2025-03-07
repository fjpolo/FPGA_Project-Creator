import os
import shutil
import re

def copy_template(template_dir, project_dir):
    """Copy the template directory to the new project directory."""
    if os.path.exists(project_dir):
        raise FileExistsError(f"Project directory already exists: {project_dir}")
    shutil.copytree(template_dir, project_dir)
    print(f"Copied template to new project directory: {project_dir}")

def rename_items(path, old_name, new_name):
    """Rename directories and files by replacing old_name with new_name."""
    # Rename directories first (depth-first to handle nested directories)
    for root, dirs, files in os.walk(path, topdown=False):
        for dir_name in dirs:
            if old_name.lower() in dir_name.lower():
                old_dir = os.path.join(root, dir_name)
                new_dir = os.path.join(root, re.sub(old_name, new_name, dir_name, flags=re.IGNORECASE))
                if old_dir != new_dir:
                    os.rename(old_dir, new_dir)
                    print(f"Renamed directory: {old_dir} -> {new_dir}")

        for file_name in files:
            if old_name.lower() in file_name.lower():
                old_file = os.path.join(root, file_name)
                new_file = os.path.join(root, re.sub(old_name, new_name, file_name, flags=re.IGNORECASE))
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
                # Replace old_name with new_name (case-insensitive)
                new_content = re.sub(old_name, new_name, content, flags=re.IGNORECASE)
                new_content = re.sub(old_name_upper, new_name_upper, new_content)
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
        # Step 1: Copy the template directory
        copy_template(template_dir, project_dir)

        # Step 2: Rename directories and files
        print("Renaming directories and files...")
        rename_items(project_dir, "template", project_name)

        # Step 3: Replace placeholders in files
        print("Replacing placeholders in files...")
        replace_in_files(project_dir, "template", project_name)

        print(f"Project '{project_name}' created successfully in '{project_dir}'.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()