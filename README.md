# Project Creator Script

This script automates the creation of a new project by copying a template directory, renaming directories and files, and replacing placeholders with the project name. It is designed to work on both macOS and Ubuntu.

---

## Features

1. **Copy Template Directory**:
   - Copies the `template` directory to a new project directory, with every file inside.

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
   - clone this repo `git clone https://github.com/fjpolo/FPGA_Project-Creator`.

2. **Make the Shell Script Executable**:
   - Run the following command to make the shell script executable:
     ```bash
     chmod +x project_creator.sh
     ```

---

## Usage

### Step 1: Run the Script
- Execute the shell script:
  ```bash
  ./project_creator.sh # Project Creator Script
  ```

This script automates the creation of a new project by copying a template directory, renaming directories and files, and replacing placeholders with the project name. It is designed to work on both macOS and Ubuntu.

---

## Project structure

```
Closed. This question does not meet Stack Overflow guidelines. It is not currently accepting answers.
This question does not appear to be about a specific programming problem, a software algorithm, or software tools primarily used by programmers. If you believe the question would be on-topic on another Stack Exchange site, you can leave a comment to explain where the question may be able to be answered.

Closed 4 years ago.

This post was edited and submitted for review 2 years ago and failed to reopen the post:

Original close reason(s) were not resolved

I want a Linux command to print directory & file structures in the form of a tree, possibly with Unicode icons before each file, and some hint for the best syntax to include the output in a Markdown document, without spaces between lines.

Example:

.
├── template
    ├── include
    │   ├── template.h
    ├── python
    │   ├── design.py
    ├── rtl
    │   ├── template.v
    ├── src
    │   ├── template.c
    │   ├── template.cpp
    ├── test_fw
    ├── test_py
    ├── test_rtl
        ├── equivalence
        ├── formal
        │   ├── template
        │   │   ├── .gitignore
        │   │   ├── properties.v
        │   │   ├── run.sh
        │   │   ├── template.sby
        │   ├── run_all.sh
        ├── lint
        │   ├── template
        │   │   ├── run.sh
        │   ├── run_all.sh
        ├── mutation
        │   ├── template
        │   │   ├── config.mcy
        │   │   ├── run.sh
        │   │   ├── test_eq.sby
        │   │   ├── test_eq.sh
        │   │   ├── test_eq.v
        │   │   ├── test_fm.sby
        │   │   ├── test_fm.sh
        │   │   ├── test_fm.v
        │   │   ├── test_sim.v
        │   │   ├── test_sim.sh
        │   ├── create_mutation_eq.sh
        │   ├── create_mutation_fm.sh
        │   ├── run_all.sh
        ├── simulation
            ├── cocotb
            │   ├── template
            │   │   ├── run.sh
            │   │   ├── testbench.py
            │   │   ├── testrunner_icarus.py
            │   │   ├── testrunner_verilator.py
            │   ├── run_all.sh
            ├── icarus
            │   ├── template
            │   │   ├── run.sh
            │   │   ├── testbench.v
            │   ├── run_all.sh
            ├── verilator
            ├── run_all.sh
```

---

## Testing

### test_rtl

- Execute the shell script:
```bash
  ./ptest_all.sh # Runs all run_all.sh testing scripts in the directory
```