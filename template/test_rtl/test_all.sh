#!/bin/bash

# Source the OSS CAD Suite environment
  echo "[SIMULATION] Sourcing OSS CAD Suite environment..."
source ~/oss-cad-suite/environment
if [ $? -ne 0 ]; then
    echo "[SIMULATION] ailed to source OSS CAD Suite environment. Exiting script."
    exit 1
fi

# Loop through all directories in the current directory
for dir in */; do
  # Check if the directory contains a run_all.sh script
  if [ -f "$dir/run_all.sh" ]; then
    echo "[SIMULATION] Running $dir/run_all.sh..."

    # Run the run_all.sh script and capture the exit status
    (cd "$dir" && ./run_all.sh)
    exit_status=$?

    # Check if the script failed
    if [ $exit_status -ne 0 ]; then
      echo "[SIMULATION] template failed!"
    else
      echo "[SIMULATION] template passed!"
    fi
  else
    echo "[SIMULATION] No run_all.sh found in $dir"
  fi
done