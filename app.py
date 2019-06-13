from flask import Flask, request, redirect, url_for , render_template
import json
from flask import Response
import depression_detection_tweets
import face_recognition

app = Flask(__name__)
res={"e":0,"s":0,"b":0}
#< a href = "{{ url_for('logout') }}" > logout < / a >

@app.route("/")
def index():
    return render_template('index.html')


@app.route('/sentimental_analysis', methods = ['GET'])
def sentimental_analysis():
    return render_template('senti-index.html')

@app.route('/sentiment/<s>', methods = ['GET'])
def sentiment(s):
    val= depression_detection_tweets.func(s)
    res["s"]=10*val;
    return render_template("index.html")


@app.route('/emotion_detection', methods = ['GET'])
def emotion_detection():
    try:
        val=face_recognition.func()
        if val>0.2:res["e"]=0
        if val<-0.2:res["e"]=10

    except:
        pass
    return render_template("index.html")


@app.route('/BDI', methods = ['GET'])
def BDI():
    return render_template('BDI.html')

@app.route('/BDIEvaluate/<score>')
def get_javascript_data(score):
    val=(int(score)/63)
    res["b"]=val*80
    print(val)
    return render_template("index.html")

@app.route('/Result', methods = ['GET'])
def Result():
    s=0
    for i in res:
        s+=(res[i])
    s=round(s,2)
    print(s)
    return render_template('Result.html',score=s)


#@app.route('/employee',methods = ['GET'])
#def employee()
 #   print(json.dumps(employees))
  #  return json.dumps(employees)

if __name__ == '__main__':
    app.run()