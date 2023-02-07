## Install on vast.ai

### Step 1

```bash
wget -qO - http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/3bf863cc.pub | apt-key add -


apt-get update
apt-get upgrade -y
add-apt-repository ppa:deadsnakes/ppa -y
apt install ffmpeg software-properties-common python3 python3.9 python3-pip python3.9-distutils nano -y
update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 1000

curl https://sh.rustup.rs -sSf | sh -s -- -y
```

### Step 2

Install virtualenv and packages neccesary for the API

```bash
pip3 install virtualenv

virtualenv env # create enviroment
source env/bin/activate # activate
```

after activate enviroment, you can install packages for API

```bash
pip3 install setuptools-rust
pip3 install --upgrade setuptools
pip3 install openai-whisper
pip3 install Flask flask_cors waitress cohere
```

### Step 3

Open **onstart.sh** file and write the command to run API:

```
CORS='' API_TRIAL_KEY='' python3 app.py
```

### Step 4

Run **onstart.sh**

```bash
sh ./onstart.sh
```
