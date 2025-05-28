# !/bin/bash

# FV
source ~/oss-cad-suite/environment && python3 template.py gen && sby -f template.sby && deactivate
# cocoTB
python3 -m venv cocotb_env && source cocotb_env/bin/activate && pip install cocotb && pip install pytest && make && deactivate