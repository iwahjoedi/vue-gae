import time
from flask import Flask
from flask import render_template
from flask import request
from flask import send_from_directory
from flask import jsonify
from flask import json
from flask import abort
from flask import Response
from flask import make_response
from flask_httpauth import HTTPBasicAuth

# RESOURCE IMPORT
from api.controllers.user import UserController 


# DEFINE APP GENERAL PATH
appname = 'api'
version = 'v1.0'
apimainpath = "/" + appname + "/" + version


# DEFINE RESOURCE
usercontroller = UserController()


app = Flask(__name__, static_url_path='')
auth = HTTPBasicAuth()

@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory('dist/static', path)
    

##################### RESOURCE: #####################

#### Resource: User
@app.route(apimainpath + "/user", methods=['GET'])
# @auth.login_required
def user_get():
    return usercontroller.get(None)

@app.route(apimainpath + "/user/<userid>", methods=['GET'])
# @auth.login_required
def user_getid(userid):
    result = usercontroller.get(userid) 
    if result is not None:
        return result
    else:
        return Response(status=204)

@app.route(apimainpath + "/user", methods=['POST'])
def user_post():
    # print "\n\n\n@main.user_post()"
    # Ensure post's Content-Type is supported
    # if request.headers['content-type'] == 'application/json':
    #     # Ensure data is a valid JSON
    #     try:
    #         user_submission = json.loads(request.data)
    #     except ValueError:
    #         return Response(status=401)

    user = {
        "username": request.json['username'],
        "realname": request.json['realname'],
        "password": request.json['password'],
        "group": request.json['group'],
    }
    
    if usercontroller.post(user) is True:
        return jsonify({"msg":user['username'] + " is stored"})
    else:
        return Response(status=409)  # 409 - Conflict
    

@app.route(apimainpath + "/user", methods=['PUT'])
def user_put():
    user = {
        "username": request.json['username'],
        "realname": request.json['realname'],
        "password": request.json['password'],
        "group": request.json['group'],
    }
    if usercontroller.put(user) is True:
        return jsonify({"msg": user['username'] + " is updated"})
    else:
        return Response(status=204)  # 204 - No Content

@app.route(apimainpath + "/user/<userid>", methods=['DELETE'])
def user_delete(userid):
    
    if usercontroller.delete(userid) is True:
        return jsonify({"msg": userid + " is deleted"})
    else:
        return Response(status=204) # 204 - No Content
        
#### Resource: ServiceCategory




################################################################################

if __name__ == "__main__":
    # app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
    # raise SystemExit(0) #for debugging
    app.run()
