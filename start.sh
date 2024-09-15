#Dont change anything without informing us
if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/DONATE-ARMY-BOTS/DONATE_ARMY_ULTIMATE_FILTER
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /DONATE_ARMY_ULTIMATE_FILTER
fi
cd /DONATE_ARMY_ULTIMATE_FILTER
pip3 install -U -r requirements.txt
echo "sᴛᴀʀᴛɪɴɢ ᴅᴏɴᴀᴛᴇ_ᴀʀᴍʏ ™ ʙᴏᴛ...."
python3 bot.py
