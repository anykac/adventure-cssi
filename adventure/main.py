# run: dev_appserver.py app.yaml

import webapp2
import jinja2
import os

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainPage(webapp2.RequestHandler):
    def get(self): #for a get request
        template = env.get_template('templates/start.html')
        self.response.write(template.render()) #the response

class JumpInCar(webapp2.RequestHandler):
    def get(self): #for a get request
        template = env.get_template('templates/jumpincar.html')
        self.response.write(template.render()) #the response

class Run(webapp2.RequestHandler):
    def get(self): #for a get request
        template = env.get_template('templates/run.html')
        self.response.write(template.render()) #the response

class ContactCSSI(webapp2.RequestHandler):
    def get(self): #for a get request
        template = env.get_template('templates/contactcssi.html')
        self.response.write(template.render()) #the response

class IgnoreCar(webapp2.RequestHandler):
    def get(self): #for a get request
        template = env.get_template('templates/ignorecar.html')
        self.response.write(template.render()) #the response

app = webapp2.WSGIApplication([
    ("/", MainPage),
    ("/jumpincar", JumpInCar),
    ("/run", Run),
    ("/contactcssi", ContactCSSI),
    ("/ignorecar", IgnoreCar),
], debug=True)
