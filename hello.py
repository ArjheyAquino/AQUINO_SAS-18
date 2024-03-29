from flask import Flask 
from flask import jsonify 
from flask import request 
  
app = Flask(_name_) 
empDB = [ 
     { 
         'id': '101', 
         'name': 'Dorry Britz', 
         'title': 'Technical Leader', 
     }, 
     { 
         'id': '102', 
         'name': 'Ice', 
         'title': 'Software Engineer', 
     } 
 ] 
  
  
@app.route("/") 
def hello(): 
     return "Hello World!" 
  
  
@app.route('/empdb/employee/', methods=['GET']) 
def getAllEmp(): 
     return jsonify({'emp': empDB}) 
  
  
@app.route('/empdb/employee/<empId>', methods=['GET']) 
def getEMP(empId): 
     usr = [emp for emp in empDB if (emp['id'] == empId)] 
     return jsonify({'emp': usr}) 
  
  
if _name_ == "_main_": 
     app.run()
