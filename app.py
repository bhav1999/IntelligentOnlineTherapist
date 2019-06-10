from flask import Flask, request, redirect, url_for , render_template
import json
from flask import Response
import depression_detection_tweets




app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route('/sentiment_analysis', methods = ['GET'])
def sentiment_analysis():
    val= depression_detection_tweets.func("I am happy")
    print(val)
    data = {
        "score":val
    }
    js = json.dumps(data)

    resp = Response(js, status=200, mimetype='application/json')


    return resp

#@app.route('/employee',methods = ['GET'])
#def employee()
 #   print(json.dumps(employees))
  #  return json.dumps(employees)

if __name__ == '__main__':
    app.run()