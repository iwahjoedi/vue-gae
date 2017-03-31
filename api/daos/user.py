# modul api.daos.user


from google.appengine.ext import ndb
from api.models.user import UserModel

class UserDao:
    usermodel = UserModel()
    
    def getUserKey(self):
        return ndb.Key('SUNTECH', 'User')
        
    def getAllUser(self):
        # print self.getUserKey().urlsafe()
        # query = UserModel.query(ancestor=self.getUserKey())
        users = UserModel.query()
        # users = query.fetch()
        # users = query.fetch(10)
        results =  [p.to_dict() for p in users]

        # for user in users:
        #     print user._properties
        # print results
        # print users
        return results
        
    def addUser(self, user):
        # currentuser = UserModel(parent=self.getUserKey()) #User is a parent and has username as the key
        
        if self.isUserExist(user['username']) is not True:
            currentuser = UserModel()
            currentuser.key = ndb.Key(UserModel, user['username'])
            currentuser.username = user['username']
            currentuser.realname = user['realname']
            currentuser.password = user['password']
            currentuser.group = user['group']
            currentuser.put()
            return True
        else:
            return False
    
    def getUserById(self, userid):
        # print "req:"+ userid
        # query = ndb.GqlQuery("SELECT * UserModel WHERE username = mia ")
        
        # query = UserModel.query(UserModel.username == userid)
        query = UserModel.get_by_id(userid)
        # print query
        # user = query.get()
        # print user
        # users = query.fetch(1)
        # print users
        # results =  [p.to_dict() for p in users]
        return query.to_dict()
        
    def updateUser(self, user):
        
        if self.isUserExist(user['username']) is True:
            currentuser = ndb.Key(UserModel, user['username']).get()
            currentuser.username = user['username']
            currentuser.realname = user['realname']
            currentuser.password = user['password']
            currentuser.group = user['group']
            currentuser.put()
            
            return True
        else:
            return False
    
    def deleteUser(self, userid):
        
        if self.isUserExist(userid) is True:
            userkey = ndb.Key(UserModel, userid)
            userkey.delete()
            return True
        else:
            return False
        
    def isUserExist(self, userid):
        user = UserModel.get_by_id(userid)
        
        # print user
        if user is not None:
            return True
        else:
            return  False
