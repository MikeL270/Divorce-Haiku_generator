# Divorce Letter Haiku Generator Server Installer
# Sets up the virutal enviroment for your convenience
# Created with regret by Michael Lance
# This script's b-day is 4/25/2024
# Last updated 4/25/2024
#-----------------------------------------------------------------------------------------------------------#
import os
import subprocess
import sys

def create_venv(path):
    # Create a the virtual environment at a specified directory
    try:
        subprocess.check_call([sys.executable, "-m", "venv", path])
        print(f"Environment successfully created at {path}")
    except subproccess.CalledProcessError as e:
        print("failed to create virtual environment")
        print(e)
        sys.exit(1)

def activate_venv():
    activate_script = os.path.join("venv", "bin", "activate") if os.name != "nt" else os.path.join("venv", "Scripts", "activate")
    activate_command = f". {activate_script}"
    return activate_command

def install_requirements():
    try:
        subprocess.check_call(f"{sys.executable} -m pip install -r requirements.txt", shell=True)
        print("Dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        print("Failed to install dependencies")
        print(e)
        sys.exit(1)

def run_setup():
    subprocess.check_call([sys.executable, "setup.py", "install"])
    print("Package installed.")
    
if __name__ == "__main__":
    venv_path = "venv"
    create_venv(venv_path)
    sys.executable = f"{venv_path}/bin/python" if sys.platform != "win32" else f"{venv_path}\\Scripts\\python.exe"
    
    install_requirements()
    run_setup()