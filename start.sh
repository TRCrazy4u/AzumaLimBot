if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/TRCrazy4u/AzumaLimBot.git /AzumaLimBot
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /AzumaLimBot
fi
cd /AzumaLimBot
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
