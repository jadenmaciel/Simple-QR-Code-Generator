# Simple-QR-Code-Generator
Creating a simple QR code generator from the use of Python. 

# 1. Create a fresh venv with pip / setuptools/ wheel pre-installed

python3 -m venv --upgrade-deps ~/venv

# 2. Activate and verify

source ~/venv/bin/activate
which python -> /home/USERNAME/venv/bin/python
which pip -> /home/USERNAME/venv/bin/pip

# 3. Install qrcode inside venv

pip install "qrcode[pil]"
pip list | grep qrcode

# 4. Run the script insie the same terminal of venv

python ~/venv/repos/Simple-QR-Code-Generator/main.py
or
python main.py
