# HeavyWater-classification-model

Train a document classification model, and then deploy it to AWS as a webservice.

This python web application is now available on http://ec2-52-2-85-139.compute-1.amazonaws.com/

The structure of this repo:

1. The "application" folder includes classification.py (flask code), pikle files (Model_LR_test.pkl: pickled Model, labelEncoder.pkl: used for getting text labels), requirements.txt files (for determine which package to install on the server that run your application), two folders (templates: html files; static:CSS and Javascript files)
  requirements.txt is included for installing required packages in the virtual environment.

2. The "classification_code" folder contains the python code for data processing, model training and test.
  Data Processing code includes: feature extraction, feature selection
  Model training code includes: 1. popular classifiers comparison; 2. ensemble classifier comparison; 3. SVM classifier comparison
