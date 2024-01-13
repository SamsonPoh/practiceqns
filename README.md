# Setup
System Package Managers: apt-get, snap, yum, apt, homebrew, chocolately
Python Package Managers: pip, conda

## Ubuntu (WSL)
``` sh
## Install Python
# sudo apt list                       # show all installed packages
# sudo apt update                     # updates the list of available packages for install (often needed on first boot, or after sometime)
# sudo apt upgrade                    # download and upgrade the package
sudo apt search python                # search for available package for installation
sudo apt install python311            # install the specific version of python
## Install Flask
# pip list
pip install flask
```

## MacOS
``` sh
## Install Python
# brew list                         # show all installed packages
brew install python@3.11
## Install Flask
# pip list
pip install flask
```

# Example Usage
``` sh
# Run Example Python
python basic.py

# Run Simple Webapp
python web-basic.py

# Run Flask Webapp
python web-flask.py

# Run Flask Webapp (with Port from system environment variables)
export PORT=9123
python web-flask-envvar.py
unset PORT                          # removes env variable
```

# Additional Useful Commands
``` sh
pwd             # shows present working directory
cd ~            # change to user directory `/home/{username}`
cd ..           # change to parent directory (i.e. 1 level up)
code .          # opens Visual Studio Code against the present directory
```
