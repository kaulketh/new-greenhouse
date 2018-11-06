#!bin/sh
#updates the scripts from the repository in current directory


archive='greenhouse.tar.gz'
project='53'

# function display usage
display_usage() {
echo
echo "Use it with last commit ID as parameter and token for acces to gitlab!"
echo "ie: $BASH_SOURCE abc123310749b9a6b366b90e0a0248db79f951123 eXe4NA6xq2WQeg3DHFBd"
}


# if less than two argument supplied, display usage
if [ $# -le 1  ] 
	then 
		display_usage
		exit 1
fi


sudo rm -v *.pyc
sudo rm -v *.py

sudo wget -O $archive https://gitlab.bekast.de/api/v4/projects/$project/repository/archive?private_token=$2

sudo tar -xvzf $archive --wildcards greenhouse-master-$1/scripts/*.py -C /home/pi/scripts/TelegramBot/
sudo tar -xvzf $archive --wildcards greenhouse-master-$1/scripts/*.sh -C /home/pi/scripts/TelegramBot/

sudo mv -v greenhouse-master-$1/scripts/*.py /home/pi/scripts/TelegramBot/
sudo mv -v greenhouse-master-$1/scripts/*.sh /home/pi/scripts/TelegramBot/
sudo rm -r -v greenhouse-master*

sudo chmod -v +x *.py
sudo chmod -v +x *.sh

sudo rm -v *.gz


