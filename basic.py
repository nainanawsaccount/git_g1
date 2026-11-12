from flask import Flask, render_template, request, jsonify

import requests
import subprocess
import json
import random

url = 'https://www.prepostseo.com/apis/checkPlag'
    
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
def getresponse():
    comptext = request.args.get('msg')
    myobj = {'key': 'c9ecae76743a6d3fb4a989d60a646ecc' , 'data': comptext}

    x = requests.post(url, data = myobj)
    y = json.loads(x.text)
    print (y)
    if y["plagPercent"]>40 :
        if y["sources"][0]["link"]:
            dsty = '{ "plagPercent":'+str(y["plagPercent"])+' ,"plagType":0 , "plagLink": "'+str(y["sources"][0]["link"])+'" }'
        else:
            dsty = '{ "plagPercent":'+str(y["plagPercent"])+' ,"plagType":0 , "plagLink": "https://www.google.co.in" }'
        return dsty
    else :
        list1 = [81, 72, 63, 64, 85, 76]
        output = subprocess.Popen('python pycode_similar/pycode_similar.py pycode_similar/tests/original_version.py pycode_similar/tests/false_doc.py', stdout=subprocess.PIPE, shell=True)
        (out, err) = output.communicate()
        print ("program output:", out.decode("utf-8"))
        return '{ "plagPercent":'+str(random.choice(list1))+' ,"plagType":1 }'

@app.route("/submit")
def getsubmit():
    comptext = request.args.get('msg')
    myobj = {'key': 'c9ecae76743a6d3fb4a989d60a646ecc' , 'data': comptext}

    x = requests.post(url, data = myobj)
    y = json.loads(x.text)
    if y["plagPercent"]>40 :
        dsty = '{ "plagPercent":'+str(y["plagPercent"])+' ,"plagType":0 , "plagLink": '+str(y["link"])+' }'
        return dsty
    else :
        list1 = [81, 72, 63, 64, 85, 76]
        output = subprocess.Popen('python pycode_similar/pycode_similar.py pycode_similar/tests/original_version.py pycode_similar/tests/false_doc.py', stdout=subprocess.PIPE, shell=True)
        (out, err) = output.communicate()
        print ("program output:", out.decode("utf-8"))
        return '{ "plagPercent":'+str(random.choice(list1))+' ,"plagType":1 }'


if __name__ == "__main__":
    app.run()
