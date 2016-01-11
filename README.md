# Installation

## Create a virtualenv

### With pew

(more informations https://github.com/berdario/pew )

- Get pew if needed: `sudo pip install pew` 
- Change directory to an appropriate place: `cd ~/MyProjects/`
- Initialize a virtualenv: `pew mkproject --python python3 iMower`
- Upgrade pip: `pip install --upgrade pip`

The virtualenv is automatically activated, and you are moved in the iMower directory. Now, usage of python or pip use ones of the virtualenv instead of system's ones.
To exit the virtualenv, use `exit` or `ctrl-D`.
To re-activate the virtualenv, use `pew workon iMower`.

## Get sources

- Clone repository using your favorite method, in the current directory (`.`): 
    + HTTPS: `git clone https://github.com/IALab-net/iMower.git .`
    + SSH: `git clone git@github.com:IALab-net/iMower.git .`

## Initialize the virtualenv

- Install dependancies: `pip install -r requirements.txt`

# Usage

## Launch

- Launch with default parameters: `python run.py`

