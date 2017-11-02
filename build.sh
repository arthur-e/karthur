rm -fr output/
pelican content

# Remove raw TeX from CV
sed -i "s/\\\hfill//g" output/pages/cv.html

# Host a server in the output directory
cd output/
python -m http.server
cd ..
