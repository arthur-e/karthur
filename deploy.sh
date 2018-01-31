pelican content -s publishconf.py

# Remove raw TeX from CV
sed -i "s/\\\hfill//g" output/pages/cv.html

rsync -avc --delete output/ karthur.org:/var/www/karthur/
rsync -avc content/ karthur.org:/home/arthur/Blog
