from flask import render_template
from flask import request
from app import app
from forms import html_to_json_purser
from flask import json



@app.route('/')
def upload_file_mainpage():
    return render_template('index.html')


@app.route('/uploader', methods=['GET', 'POST'])
# In this part the response of the function return as json file also as prints json as reponse
# the data kept in out.json file
def upload_file():
    if request.method == 'POST':
        new_file = request.files['file']
        response = json.dumps(html_to_json_purser(new_file))
        outfile = open('out.json', 'w')
        with outfile as outfile:
            outfile.write(response)
            return response, 200



