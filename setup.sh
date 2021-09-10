USERNAME=arthur
VENV_DIR=/usr/local/pythonenv/pelican

virtualenv -p /usr/bin/python3 $VENV_DIR

# Installing pelican-plugins repo
cd /usr/local/
sudo mkdir pelican
sudo chown $USERNAME pelican
cd pelican
git clone https://github.com/getpelican/pelican-plugins

# Temporary fix for render_math
# cd pelican-plugins
# git checkout 560b6ad61ade9e73d7482abdf4d8287032817631

# Install cmake
# sudo apt install cmake

# Installing support for the thumbnailer plug-in
# NOTE: This will break other applications that depend on OpenJPEG
# cd /usr/local/
# sudo mkdir openjpeg
# sudo chown arthur openjpeg
# cd openjpeg
# wget http://downloads.sourceforge.net/project/openjpeg.mirror/2.1.0/openjpeg-2.1.0.tar.gz
# tar -xzvf openjpeg-2.1.0.tar.gz && rm openjpeg-2.1.0.tar.gz && cd openjpeg-2.1.0
# cmake .
# make
# sudo make install
# sudo ldconfig

source $VENV_DIR/bin/activate
pip install -r /usr/local/dev/karthur/REQUIREMENTS

# Get fonts
rsync -avc $USERNAME@karthur.org:/var/www/karthur/theme/fonts /usr/local/dev/karthur/themes/karthur/static/

cd $VENV_DIR
source $VENV_DIR/retrieve.sh $USERNAME

# Update symbolic links
unlink /usr/local/dev/karthur/content/pages/cv.md
ln -s ~/Sync/Documents/CV.md /usr/local/dev/karthur/content/pages/cv.md
unlink /usr/local/dev/karthur/content/static/docs/Endsley_CV.pdf
ln -s ~/Sync/Documents/Endsley_CV.pdf /usr/local/dev/karthur/content/static/docs/Endsley_CV.pdf
