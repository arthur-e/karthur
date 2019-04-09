pelican content -s publishconf.py

# Remove raw TeX from HTML output
. ./clean.sh

rsync -avc --delete output/ karthur.org:/var/www/karthur/
rsync -avc content/ karthur.org:/home/arthur/Blog
