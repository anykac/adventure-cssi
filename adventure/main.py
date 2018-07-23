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

#Options from Jump In
class AcceptJumpIn(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('templates/acceptjump.html')
        self.response.write(template.render())

class RejectJumpIn(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('templates/rejectjump.html')
        self.response.write(template.render())




class ListenToCar(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('templates/listentocar.html')
        self.response.write(template.render())

class RunAway(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('templates/runaway.html')
        self.response.write(template.render())

app = webapp2.WSGIApplication([
    ("/", MainPage),
    ("/jumpincar", JumpInCar),
    ("/run", Run),
    ("/contactcssi", ContactCSSI),
    ("/ignorecar", IgnoreCar),
    #Jump In
    ("/accept", AcceptJumpIn),
    ("/reject", RejectJumpIn),

    ("/listentocar", ListenToCar),
    ("/runaway", RunAway),
], debug=True)
