from flask import Flask, render_template, request, redirect
import cf_deployment_tracker
import os
import json
from os.path import join, dirname
from secret_constants import secret_dictionary
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
  import Features, EmotionOptions, SentimentOptions
import pprint

# Emit Bluemix deployment event
cf_deployment_tracker.track()

app = Flask(__name__, static_url_path="/static", static_folder="static")

# On Bluemix, get the port number from the environment variable PORT
# When running this app on the local machine, default the port to 8080
port = int(os.getenv('PORT', 8080))

#Render the index page
@app.route('/') 
def hello_world():
  return render_template('index.html')

# Display takes care of form and the results page
@app.route('/display', methods=['GET', 'POST'])
def handleMoodLogging():
  # Display the form
  if request.method == 'GET':
    return render_template('index.html')
  else:
    # Validate using credentials
    natural_language_understanding = NaturalLanguageUnderstandingV1(
      username=secret_dictionary['username'],
      password=secret_dictionary['password'],
      version='2018-03-16'
    )
    
    # Grab the text from the user
    journal_contents = request.form['journal_content']
    #print('journal contents: ', journal_contents.encode('ascii', 'ignore'))

    # Make a call to the API with the text passed in
    alchemy_results = natural_language_understanding.analyze(
    text = journal_contents.encode('ascii', 'ignore'),
       features=Features(emotion = EmotionOptions(), sentiment=SentimentOptions()))

    #print 'Writing results to a file:'
    fo = open('static/mockresponses/emotion_response.json', 'w+')
    fo.write(json.dumps(alchemy_results, indent=2))
    fo.close()
    return render_template('gauge.html')

@app.route('/test2.html')
def test2render():
  return render_template('test2.html')

# @app.route('/templates/1stvis/liquidFillGauge.js')
# def renderPage1():
#     return render_template('1stvis/liquidFillGauge.js')

# @app.route('/templates/1stvis/emotion.json')
# def renderPage2():
#     return render_template('1stvis/emotion.json')

# @app.route('/templates/1stvis/sentiment.json')
# def renderPage3():
#     return render_template('1stvis/sentiment.json')

# @app.route('/templates/2vis/test2.html')
# def renderPage4():
#     return render_template('2vis/test2.html')

# @app.route('/templates/2vis/test_subset.json')
# def renderPage5():
#     return render_template('2vis/test_subset.json')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
