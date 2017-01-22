"""Cloud Foundry test"""
from flask import Flask
import cf_deployment_tracker
import os
import json
from os.path import join, dirname
from watson_developer_cloud import AlchemyLanguageV1
from api_key import SUPERSECRETKEY


# Emit Bluemix deployment event
cf_deployment_tracker.track()

app = Flask(__name__)

# On Bluemix, get the port number from the environment variable PORT
# When running this app on the local machine, default the port to 8080
port = int(os.getenv('PORT', 8080))


@app.route('/')
def hello_world():
  alchemy_language = AlchemyLanguageV1(api_key=SUPERSECRETKEY)
  url = 'https://developer.ibm.com/watson/blog/2015/11/03/price-reduction-for-watson-personality-insights/'
  dump = json.dumps( alchemy_language.targeted_sentiment(text='I love cats! Dogs are smelly.',
                      targets=['cats', 'dogs'],
                      language='english'), indent=2)
  return 'Contents of dump is: ' + dump

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
