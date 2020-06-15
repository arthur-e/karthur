pelican content -s publishconf.py

# Remove raw TeX from HTML output
. ./clean.sh

rsync -avc --delete output/ $1@karthur.org:/var/www/karthur/
rsync -avc content/ $1@karthur.org:/home/arthur/Blog
