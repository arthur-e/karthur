virtualenv -p /usr/bin/python3 /usr/local/pythonenv/pelican-env

# Installing pelican-plugins repo
cd /usr/local/
sudo mkdir pelican
sudo chown arthur pelican
cd pelican
git clone https://github.com/getpelican/pelican-plugins

# Install cmake
sudo apt install cmake

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

source /usr/local/pythonenv/pelican-env/bin/activate
pip install -r /usr/local/dev/karthur/REQUIREMENTS

# Get fonts
rsync -avc karthur.org:/var/www/karthur/theme/fonts /usr/local/dev/karthur/themes/karthur/static/
