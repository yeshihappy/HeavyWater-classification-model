from flask import Flask, request, render_template,url_for,redirect
from sklearn import pipeline
import re, string
try:
   import cPickle as pickle
except:
   import pickle

#create app
app = Flask(__name__)

# load model from local
filename='test_LR_test.pkl'
model=pickle.load(open(filename,'rb'))
# load label encoder to get text labels
labelEncoder='labelEncoder.pkl'
encoder=pickle.load(open(labelEncoder,'rb'))

@app.route('/',methods=['GET'])
def index():
  return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
  if request.method=='POST':
  	words=request.form['input']
  	if words:
  		# split documents words by ;,\n\t
  		temp=re.split(';|,|\n|\t',str(words).strip())
  		# remove punctuation chars, whitespaces, and None values from the string list (time consuming)
  		#words=[''.join(c for c in s if c not in string.punctuation).strip() for s in temp if s]
  		# remove empty strings
  		words=[word.strip() for word in temp if word.strip()]
  		# if list is not empty
  		if len(words) > 0:
  			Y_pred=model.predict(words)   # get prediction ID
  			Y_pred_labels=encoder.inverse_transform(Y_pred) # get predition text labels
  			Y_pred_Pro=model.predict_proba(words)
  			confidence={}
  			for i in range(len(Y_pred_Pro)):
  				confidence[i]="{:0.2f}".format(100*max(Y_pred_Pro[i])) # confidence in %
  			return render_template('result.html',words=words,result=Y_pred_labels,confidence=confidence)
  return redirect(url_for('index')) # redirect to index page if method == get OR error

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0')