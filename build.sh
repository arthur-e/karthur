rm -fr output/
pelican content
cd output/
python -m http.server
cd ..
