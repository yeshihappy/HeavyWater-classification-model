from flask import Flask, jsonify, request, abort, render_template
from sklearn import pipeline
import re
try:
   import cPickle as pickle
except:
   import pickle

#create app
app = Flask(__name__)

## load model from S3
# from boto.s3.key import Key
# from boto.s3.connection import S3Connection
# BUCKET_NAME= 'YOURBUCKETNAME'
# MODEL_FILE_NAME='finalized_model_svm_SGD.sav'
# MODEL_LOCAL_PATH='\temp\'+MODEL_FILE_NAME
# bucket=S3Connection().create_bucket(BUCKET_NAME)
# key_obj=Key(bucket)
# key_obj.key=MODEL_FILE_NAME
# contents = key_obj.get_contents_to_filename(MODEL_LOCAL_PATH)
# model=pickle.load(open(MODEL_LOCAL_PATH,'rb'))

# load model from local
filename='finalized_model_svm_SGD.sav'
model=pickle.load(open(filename,'rb'))

@app.route('/')
def initial():
  return render_template('index.html')

@app.route('/index',methods=['GET'])
def index():
  return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
  if request.method=='POST':
      words=str(request.form['input'])
      words=[str(i).strip() for i in re.split(';|,|\*|\n|\t',words) if i]
      Y_pred=model.predict(words)
      result={}
      for i in range(len(Y_pred)):
        result[i]="Document Label : "+ str(Y_pred[i])
      return render_template('result.html',words=words,result=result)

if __name__ == '__main__':
    app.run()
    #app.run(host='0.0.0.0', port=80)
