from flask import Flask
from flask import request
from flask import send_from_directory
from flask import  jsonify
from flask import abort
from flask import Response
from flask_httpauth import HTTPBasicAuth

# Resources
# Resource import module
from api.controllers.user import UserController 

#GLOBAL
class AppHead:
    # global appinstance     
    # global auth 
    
    appname = 'api'
    version = 'v1.0'
    apimainpath = "/" + appname + "/" + version

    def __init__(self,app):
        app.add_url_rule(self.apimainpath + '/user', 'index', self.index)

    def index():
        return "INI INDEX"
    
    def loadresource(self):
        # User
        usercontroller = UserController(self.app, self.apimainpath)
    
    def run(self):
        
        # @appinstance.route('/static/<path:path>')
        # def send_js(path):
        #     return send_from_directory('dist/static', path)
        
        self.loadresource()
