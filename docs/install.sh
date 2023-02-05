wget -qO - http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/3bf863cc.pub | sudo apt-key add -
sudo apt-get update
sudo apt-get upgrade -y
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt install nodejs npm nginx ffmpeg software-properties-common python3 python3.9 python3-pip python3.9-distutils python3.9-dev pkg-config libicu-dev lsof nano -y
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 1000
pip3 install setuptools-rust
pip3 install --upgrade setuptools
curl https://sh.rustup.rs -sSf | sh -s -- -y

python -m pip install --upgrade pip
pip3 install --upgrade setuptools
pip install git+https://github.com/openai/whisper.git