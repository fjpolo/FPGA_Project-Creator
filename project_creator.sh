#!/bin/bash

# Define the template directory
TEMPLATE_DIR="./template"

# Check if the template directory exists
if [ ! -d "$TEMPLATE_DIR" ]; then
  echo "Template directory not found: $TEMPLATE_DIR"
  exit 1
fi

# Ask the user for the project name
read -p "Enter the project name: " PROJECT_NAME

# Check if the project name is empty
if [ -z "$PROJECT_NAME" ]; then
  echo "Project name cannot be empty."
  exit 1
fi

# Define the new project directory
PROJECT_DIR="./$PROJECT_NAME"

# Check if the project directory already exists
if [ -d "$PROJECT_DIR" ]; then
  echo "Project directory already exists: $PROJECT_DIR"
  exit 1
fi

# Copy the template directory to the new project directory
echo "Copying template to new project directory..."
cp -r "$TEMPLATE_DIR" "$PROJECT_DIR"

# Function to rename directories and files
rename_items() {
  local path="$1"
  local old_name="$2"
  local new_name="$3"

  # Rename directories and files
  find "$path" -depth -name "*$old_name*" | while read -r item; do
    new_item=$(echo "$item" | sed "s/$old_name/$new_name/g")
    mv "$item" "$new_item"
  done
}

# Function to replace placeholders in files
replace_in_files() {
  local path="$1"
  local old_name="$2"
  local new_name="$3"

  # Replace placeholders in files
  find "$path" -type f -exec sed -i "s/$old_name/$new_name/g" {} +
}

# Rename directories and files
echo "Renaming directories and files..."
rename_items "$PROJECT_DIR" "template" "$PROJECT_NAME"

# Replace placeholders in files
echo "Replacing placeholders in files..."
replace_in_files "$PROJECT_DIR" "template" "$PROJECT_NAME"

echo "Project '$PROJECT_NAME' created successfully in '$PROJECT_DIR'."