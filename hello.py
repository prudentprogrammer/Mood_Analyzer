"""Cloud Foundry test"""
from flask import Flask, render_template
import cf_deployment_tracker
import os
import json
from os.path import join, dirname
from watson_developer_cloud import AlchemyLanguageV1
from api_key import SUPERSECRETKEY

# Bootstrap libraries
from flask_bootstrap import Bootstrap




# Emit Bluemix deployment event
cf_deployment_tracker.track()

app = Flask(__name__)

# On Bluemix, get the port number from the environment variable PORT
# When running this app on the local machine, default the port to 8080
port = int(os.getenv('PORT', 8080))


@app.route('/') 
def hello_world():
  return render_template('index.html')
  #return 'Contents of dump is: ' + dump

@app.route('/display')
def dump():
  alchemy_language = AlchemyLanguageV1(api_key=SUPERSECRETKEY)
  dumpa = json.dumps( alchemy_language.targeted_sentiment(text='I love cats! Dogs are smelly.',
                      targets=['cats', 'dogs'],
                      language='english'), indent=2)
  return render_template('display.html', dumpa = dumpa)

if __name__ == '__main__':
    Bootstrap(app)

  
    app.run(host='0.0.0.0', port=port)
