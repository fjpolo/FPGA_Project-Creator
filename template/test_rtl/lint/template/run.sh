# !/bin/bash

# oss-cad-suite env
source ~/oss-cad-suite/environment

# Run verilator as linter
verilator --lint-only --Wall --cc ${PWD}/../../../rtl/template.v
