# HeavyWater-classification-model

Train a document classification model, and then deploy it to AWS as a webservice.

This python web application is now available on http://ec2-52-2-85-139.compute-1.amazonaws.com/

The structure of this repo:

1. The "application" folder includes classification.py (flask code), a trained pikled model (.sav file Note: not the latest one) and two folders (static and templates storing html, CSS, Javascript files)

2. The "classification_code" folder contains the python code for data processing, model training and test.
