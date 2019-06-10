from flask import Flask, request, redirect, url_for , render_template
import json
from flask import Response
import depression_detection_tweets
import face_recognition

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/sentimental_analysis', methods = ['GET'])
def sentimental_analysis():
    return render_template('senti-index.html')

@app.route('/sentiment', methods = ['GET'])
def sentiment():
    val= depression_detection_tweets.func("I am happy")
    print(val)
    return render_template("index.html")


@app.route('/emotion_detection', methods = ['GET'])
def emotion_detection():
    try:
        val=face_recognition.func()
        print(val)
    except:
        pass
    return render_template("index.html")


@app.route('/BDI', methods = ['GET'])
def bdi():
    return render_template('BDI.html')

#@app.route('/employee',methods = ['GET'])
#def employee()
 #   print(json.dumps(employees))
  #  return json.dumps(employees)

if __name__ == '__main__':
    app.run()