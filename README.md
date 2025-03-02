# Project Creator Script

This script automates the creation of a new project by copying a template directory, renaming directories and files, and replacing placeholders with the project name. It is designed to work on both macOS and Ubuntu.

---

## Features

1. **Copy Template Directory**:
   - Copies the `template` directory to a new project directory.

2. **Rename Directories and Files**:
   - Renames directories and files by replacing the placeholder `template` with the project name (case-insensitive).

3. **Replace Placeholders in Files**:
   - Replaces occurrences of `template` and `TEMPLATE` in file contents with the project name (case-insensitive).

4. **Skip Binary or Unreadable Files**:
   - Skips binary or unreadable files to avoid errors.

---

## Prerequisites

- **Python 3**: The script is written in Python and requires Python 3 to run.
- **Template Directory**: A `template` directory must exist in the same location as the script.
- **oss-cad-suite**: OSS CAD Suite is a binary software distribution for a number of open source software used in digital logic design. ⚠️ needed in **~/oss-cad-suite**

---

## Setup

1. **Clone or Download the Script**:
   - Download the `project_creator.py` and `project_creator.sh` files to your project directory.

2. **Make the Shell Script Executable**:
   - Run the following command to make the shell script executable:
     ```bash
     chmod +x project_creator.sh
     ```

3. **Create the Template Directory**:
   - Create a `template` directory in the same location as the script.
   - Populate the `template` directory with your project structure, using `template` as a placeholder for the project name.

---

## Usage

### Step 1: Run the Script
- Execute the shell script:
  ```bash
  ./project_creator.sh # Project Creator Script
  ```

This script automates the creation of a new project by copying a template directory, renaming directories and files, and replacing placeholders with the project name. It is designed to work on both macOS and Ubuntu.


## Testing

### test_rtl

- Execute the shell script:
```bash
  ./ptest_all.sh # Runs all run_all.sh testing scripts in the directory
```