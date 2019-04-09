rm -fr output/
pelican content

# Remove raw TeX from HTML output
. ./clean.sh

# Host a server in the output directory
cd output/
python -m http.server
cd ..
