# Using Deep Learning to Measure Music Similarity
#### CS230 Project - Nicholas Allen

## Description

This project aims to develop a neural network which takes two audio tracks and outputs a "similarity" score for the pair of tracks, where similarity is measured by user reviews and preferences. Currently, it is using Last.FM data to gauge the similarity of different artists to eachother, then scraped audio data to provide inputs. Learning is done using audio spectrogram data as input, with a generated user preference metric specific to each possible combination of artists as the output.

## Setup

First, the Last.FM dataset will need to be downloaded from http://mtg.upf.edu/static/datasets/last.fm/lastfm-dataset-360K.tar.gz and extracted to a dataset directory. This can also be done with the `setup_lastfm_dataset.sh` script in the dataset directory. To scrape audio data, edit `params.json` and add your Spotify API keys, as well as modifying any parameters necessary in the file (such as number of artists you want to scrape) and then run through `scrapeartists.ipynb`. Then, spectrogram images need to be generated for each audio sample by running `generatespec.py` as a Python script. Generating the user preferences database is done in `gen_split_dataset.ipynb`, which generates several types of databases (each with a different user preference metric) and saves them. Neural network development is performed in `development.ipynb`.

## Dataset

The dataset used is generated from the previous Last.FM data, by counting the number of times a given user listens to both of each given pair of artists. These values are then normalized against the total listeners for each artist, and then globally scaled from 0 to 1. Scraped audio data is converted to mel-spectrograms of size 256x64. 

## Neural Network

The neural network architecture is based on a siamese network, where each pair of images is fed into separate neural networks which share the same weights and parameters. The siamese networks are composed of multiple 1D convolutions along the time axis, with a final global max-pooling along the time axis, and a densely-connected layer to compress the output into a flat vector. The L1 norm between the outputs of each siamese network is taken, and the resulting vector fed into a logistic neuron to generate the final output, which in this case is the similarity score generated earlier.
