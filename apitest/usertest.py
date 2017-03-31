import time
import unittest
import requests
from flask import json

class UserTestCase(unittest.TestCase):
    path_system = "http://gae-python-ijoewahjoedi1.c9users.io"
    # path_system = "http://suntech-kalian.appspot.com"
    path_app    = "/api/v1.0"
    path_resource = "/user"

    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    # GET
    def test_get(self):
        print "GET"
        r = requests.get(self.path_system + self.path_app + self.path_resource)
        # print r.text
        self.assertEqual(r.status_code, 200)
        
    # def test_get_byid_notexist(self):
        userid = "noa"
        r = requests.get(self.path_system + self.path_app + self.path_resource+ "/" + userid)
        self.assertEqual(r.status_code, 204)
    
    # def test_get_byid_exist(self): 
        userid = "joe"
        r = requests.get(self.path_system + self.path_app + self.path_resource+ "/" + userid)
        # print r.text
        self.assertEqual(r.status_code, 200)
    
    # POST
    def test_post(self):
        print "POST"
    # def test_post_notexist(self):
        # Using Non Exist Entity
        r = requests.post(self.path_system + self.path_app + self.path_resource, headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}, data = json.dumps({"username":"dhoeh","realname":"Jam Boe","password":"passoo","group":"TECH"}))
        # print r.text
        self.assertEqual(r.status_code, 200)
        
    # def test_post_exist(self):
        # Using Exist Entity
        r = requests.post(self.path_system + self.path_app + self.path_resource, headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}, data = json.dumps({"username":"joe","realname":"Joe","password":"passoo","group":"TECH"}))
        self.assertEqual(r.status_code, 409)
         
    # PUT
    def test_put(self):
        print "PUT"
    # def test_put_exist(self):
        # Using Exist Entity
        r = requests.put(self.path_system + self.path_app + self.path_resource, headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}, data = json.dumps({"username":"joe","realname":"Jam Boe BOEL","password":"passoo","group":"TECH"}))
        print r.text
        self.assertEqual(r.status_code, 200)
        
    
    # def test_put_notexist(self):
        # Using Exist Entity
        r = requests.put(self.path_system + self.path_app + self.path_resource, headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}, data = json.dumps({"username":"bussssbue","realname":"Jam Boe","password":"passoo","group":"TECH"}))
        print r.text
        self.assertEqual(r.status_code, 204)
    
    # DELETE
    def test_delete(self):
        print "DELETE"
    # def test_delete_exist(self):
        # Using Exist Entity
        r = requests.delete(self.path_system + self.path_app + self.path_resource + "/serieh", headers = {'Content-type': 'application/json', 'Accept': 'text/plain'} )
        print r.text
        self.assertEqual(r.status_code, 200)
        
    
    # def test_delete_notexist(self):
        # Using Exist Entity
        r = requests.delete(self.path_system + self.path_app + self.path_resource + "/cermassi31", headers = {'Content-type': 'application/json', 'Accept': 'text/plain'} )
        print r.text
        self.assertEqual(r.status_code, 204)
    
    
if __name__ == '__main__':
    unittest.main()