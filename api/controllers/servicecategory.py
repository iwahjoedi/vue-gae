# TEST
# =========
# Routes
# GET	/UserService/users	Get list of users	Read Only
# 2	GET	/UserService/users/1	Get User with Id 1	Read Only
# 3	PUT	/UserService/users/2	Insert User with Id 2	Idempotent
# 4	POST	/UserService/users/2	Update User with Id 2	N/A
# 5	DELETE	/UserService/users/1	Delete User with Id 1	Idempotent
# 6	OPTIONS	/UserService/users	List the supported operations in web service	Read Only

### CONTROLLER ###
from flask import jsonify

class ServiceCategory():
    # /servicecategories
    def get_servicecategories(self):
        return jsonify(name='GET - ServiceCategory')
    
    def get_servicecategorybyid(self,idservicecategory):
        return jsonify(name='GET by id - ServiceCategory', id=idservicecategory)
    
    def new_servicecategory(self,servicecategory):
        return jsonify(msg='Stored')

    def update_servicecategory(self,servicecategory):
        return jsonify(msg='Stored')


    def delete_servicecategory(self, idservicecategory):
        return jsonify(msg='Deleted')