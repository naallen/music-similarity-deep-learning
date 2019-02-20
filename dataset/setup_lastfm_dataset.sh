echo "Downloading Last.FM Dataset..."
wget "http://mtg.upf.edu/static/datasets/last.fm/lastfm-dataset-360K.tar.gz"
tar xfvz lastfm-dataset-360K.tar.gz
mv lastfm-dataset-360K/* .
