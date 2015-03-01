pelican content -s publishconf.py
rsync -avc --delete output/ karthur.org:/var/www/karthur/
