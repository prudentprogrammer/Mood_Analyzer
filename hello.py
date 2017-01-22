"""Cloud Foundry test"""
from flask import Flask, render_template, request, redirect
import cf_deployment_tracker
import os
import json
from os.path import join, dirname
from watson_developer_cloud import AlchemyLanguageV1
from api_key import SUPERSECRETKEY

# Bootstrap libraries
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, BooleanField


# Emit Bluemix deployment event
cf_deployment_tracker.track()

app = Flask(__name__)
Bootstrap(app)

# On Bluemix, get the port number from the environment variable PORT
# When running this app on the local machine, default the port to 8080
port = int(os.getenv('PORT', 8080))


@app.route('/') 
def hello_world():
  return render_template('index.html')
  #return 'Contents of dump is: ' + dump

@app.route('/display', methods=['GET', 'POST'])
def dump():

  if request.method == 'GET':
    return render_template('display.html')
  else:
    # Show the form
    journal_contents = request.form['content']
    print('CONTENTS OF JOURNAL: ' + journal_contents)
    alchemy_language = AlchemyLanguageV1(api_key=SUPERSECRETKEY)
    dumpa = json.dumps( alchemy_language.emotion(text=journal_contents, language='english'), indent=2)
    return render_template('results.html', dumpa = dumpa)
    #return render_template('results.html')

#@app.route('/results/<content_string>')
#def displayResults():
#  return render_template('results.html', dumpa = content_string)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
