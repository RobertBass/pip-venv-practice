#TERMINAL INSTRUCTIONS
#WSL-LINUX
```sh
python3 -V
sudo apt install -y python3-pip
pip3 -V
sudo apt install -y build-essential libssl-dev libffi-dev python3-dev
```

#MAC
```sh
sudo xcode-select --install
sudo xcode-select --reset
brew install python3
```

#GAME PROJECT
```sh
cd game
python3 main.py
```

#CREATING ENVIRONMENTS
```sh
sudo apt install python3-venv
#MOVE TO PROOJECT FILE
python3 -m venv nameOfEnvironment #CREATING ENVIRONMENT
source nameOfEnvironment/bin/activate #RUNNING ENVIRONMENT
deactivate #TO EXIT OF ENVIRONMENT
```

#REQUIREMENTS.TXT
```sh
pip3 freeze > requirements.txt
pip3 install -r requirements.txt
```