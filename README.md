#Team Members 
Sravya Divakarla, 
Jordan Carlile, 
Aakash Prabhu, 
Arjun Bharadwaj


#Inspiration
Mental health is a large problem which goes relatively unnoticed because it is very difficult to: identify, analyze, and treat. We wanted a way for everyone to obtain easy access to monitor their mental wellbeing. Journaling is a very common practice that psychologists use to treat their patients. However, it becomes very tedious to go through all the entries, so we wanted to automate this process.

#What it does
Patients type their journal entry for the day.
The system analyzes and generates data visualization for monthly and daily reports.
How we built it
API's used IBM Watson (AlchemyAPI) for sentimental/emotional analysis

##Backend Flask and Python frameworks were used to render html webpages and interact with IBM Watson API. The result was then rendered.

##Frontend Data visualizations were performed with D3.js. Using HTML, CSS, JS, we integrated it with backend.

#Challenges we ran into
##Backend Challenges We first started using Ruby on Rails and Node.js to connect and develop via the IBM Watson API. However, there were problems with compatibilities and gem issues. So we decided to switch to Flask, which is a lightweight Python framework for web apps and we faced less issues in terms of web dev after switching.

##Frontend Challenges Scalability of Data Visualizations and event integrations. Rendering the JSON files which was given to the frontend by the backend. Having multiple visualizations collectively use the same input data.

##Misc. Problems Problems with exploring new frameworks

Accomplishments that we're proud of
We are proud of the following things:

Use multiple aspects of the IBM Watson API (emotion and sentiment functions).
Bridging the gap between Watson and D3.js
Perform complex and interactive Data Visualization on the frontend using D3.js.
What we learned
We learned the following things:

Using IBM Watson API to accomplish powerful tools to help patients.
Using flask and python to develop fully functional webapps.
Using D3.js and Javascript to provide simple yet dynamic monitoring system.
What's next for Mind Your Mind
Run the app to analyze text messages and emails that you send to the bot.
Emails or Texts: When the mood is on the extremes, it would send an email to the doctor the patient's mental condition.
Mood detection based on images.
Turn it into a medical product which allows for inexpensive treatment and easy access.