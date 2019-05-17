set -e
pythonver=$(which python3.6)
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
if [ ! -z $pythonver ]; then
echo "This should say python3.6 or something."
python3.6 --version
else
echo "Python3.6 is not installed. Please install it. Only 3.6. Not 3.7. Or you can try. I don't know. I wouldn't."
exit 1
fi

sudo pip3 install -r requirements.txt --timeout 5
sudo pip3 install -Iv https://github.com/Rapptz/discord.py/archive/v0.16.12.tar.gz --timeout 5
echo "Note: You might find some dependancy errors! please make an issue report on the github so i can fix my stupid bullshit."

