# FAKE_ALERT
(predicts the sanity of the article)

The sanity predictor model is a single, end to end system consisting of lexical as well as similarity features fed through a multi-layer perceptron.

The features extracted from the headline and article body pairs consist of three overarching elements only:
* A bag-of-words term frequency (BoW-TF) vector of the headline
* A BoW-TF vector of the body
* The cosine similarity of term frequency-inverse document frequency(TF-IDF) vectors of the headline and body

### Prerequisites

python 3.5.2
numpy 1.14.0
scikit-learn 0.19.1
tensorflow  1.8.0


### Executing

simply execute the 'pred.py'.

The `pred.py` script can be run in two different modes: 'load' or 'train'.

Execution of the `pred.py` file in 'load' mode entails the
following:

* The train set will be loaded from `train_stances.csv` and `train_bodies.csv`.
* The test set will be loaded from `test_stances_unlabeled.csv` and `train_bodies.csv`.
* The model is then used to predict the labels on the processed test set.

The file name for the predictions can be changed in section '# Set file names' at the top of `pred.py`, if required.

## Team Members [Duplicate Anonymous]

* [Rishabh Umrao] - Full implementation
* [Astitva Singh] - Academic supervision
* [Mohd. Bilal] - advice
* [Yash Chaudhary] - advice



ppt: https://drive.google.com/open?id=13CGTu6zFISdkrs0OZaiyhfpUKETL7bz9