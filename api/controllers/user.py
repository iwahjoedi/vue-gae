# modul api.controllers.user
import time

from flask import jsonify

from api.models.user import UserModel
from api.daos.user import UserDao

class UserController():
    usermodel = UserModel()
    userdao = UserDao()
    
    def get(self, userid):
        if userid is None:
            # return a list of users
            user = {
                "username": "myuser1",
                "realname": "My Real Name",
                "password": "mypass",
                "group": "mygroup",
            }
            
            users = self.userdao.getAllUser()
            return jsonify (users)

        else:
            # expose a single user
            if self.userdao.isUserExist(userid) is True:
                return jsonify(self.userdao.getUserById(userid))
            else:
                return None
            
    def post(self, user):
        # create a new user
        
        if self.userdao.addUser(user) is True:
            return True
        else:
            return False
            
    def put(self, user):
        # update a single user
        
        if self.userdao.updateUser(user) is True:
            return True
        else:
            return False
        
    def delete(self, userid):
        # delete a single user
        if self.userdao.deleteUser(userid) is True:
            return True
        else: 
            return False
