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
import pprint

# Emit Bluemix deployment event
cf_deployment_tracker.track()

app = Flask(__name__, static_url_path="/static", static_folder="static")
Bootstrap(app)

# On Bluemix, get the port number from the environment variable PORT
# When running this app on the local machine, default the port to 8080
port = int(os.getenv('PORT', 8080))

# Render the index page
@app.route('/') 
def hello_world():
  return render_template('index.html')

# Display takes care of form and the results page
@app.route('/display', methods=['GET', 'POST'])
def dump():
  # Display the form
  if request.method == 'GET':
    return render_template('display.html')
  else:
    print 'ENTERING HERE'
    # Show the results page
    journal_contents = request.form['content']
    alchemy_language = AlchemyLanguageV1(api_key=SUPERSECRETKEY)
    
    # Emotion json
    alchemy_results = json.dumps( alchemy_language.emotion(text=journal_contents, language='english'), indent=2)
    fo = open('templates/1stvis/emotion.json', 'w')
    fo.write(alchemy_results)
    
    pprint.pprint(alchemy_results)
    fo.close()
    
    # Write to sentiment json
    alchemy_results = json.dumps(
    alchemy_language.sentiment(text=journal_contents, language='english'), indent=2)
    fo = open('templates/1stvis/sentiment.json', 'w')
    fo.write(alchemy_results)
    
    print 'SENTIMENTS --> '
    pprint.pprint(alchemy_results)
    fo.close()
    
    return render_template('1stvis/gauge.html')

@app.route('/templates/1stvis/liquidFillGauge.js')
def renderPage1():
    return render_template('1stvis/liquidFillGauge.js')

@app.route('/templates/1stvis/emotion.json')
def renderPage2():
    return render_template('1stvis/emotion.json')

@app.route('/templates/1stvis/sentiment.json')
def renderPage3():
    return render_template('1stvis/sentiment.json')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
