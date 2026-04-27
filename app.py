from flask import Flask,render_template,request
import os
from deepfake_detector import predict_fake

app=Flask(__name__)

UPLOAD_FOLDER="uploads"
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    file=request.files['video']

    if file:
        path=os.path.join(
            app.config['UPLOAD_FOLDER'],
            file.filename
        )

        file.save(path)

        result=predict_fake(path)

        return render_template(
            'index.html',
            prediction=result
        )

if __name__=="__main__":
    app.run(debug=True)
