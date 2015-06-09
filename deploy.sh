pelican content -s publishconf.py
rsync -avc --delete output/ karthur.org:/var/www/karthur/
rsync -avc content/ karthur.org:/home/arthur/Blog
