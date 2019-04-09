# Remove raw TeX from CV
sed -i "s/\\\hfill//g" output/pages/cv.html
sed -i -E "s/\\\setlength.+parindent.+//g" output/pages/cv.html
sed -i -E "s/\\\hangindent=.em//g" output/pages/cv.html
sed -i -E "s/\\\pubgroup.+\}//g" output/pages/cv.html

# TODO Recursively replace "---" with "&#8212;" to fix em dashes
