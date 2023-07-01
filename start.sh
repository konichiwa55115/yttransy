echo "Cloning Repo...."
git clone https://github.com/konichiwa55115/vidtrim /kony
git clone https://github.com/GregorR/rnnoise-models /kony/vidtrim
cd /kony
pip3 install -r requirements.txt
echo "Starting Bot...."
gunicorn app:app & python3 bot.py
