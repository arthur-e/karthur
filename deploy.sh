pelican content -s publishconf.py
rsync -avc --delete output/ karthur.org:/var/www/karthur/
rsync -avc --delete content/ karthur.org:/home/arthur/Blog
