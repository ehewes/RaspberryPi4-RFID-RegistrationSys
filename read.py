from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import time
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json


uri = "UR-URI-STRING"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    
mydb = client["database_student"]
mycol = mydb["students"]
  

reader = SimpleMFRC522()

def get_students_rfid():
        for x in mycol.find({}, {"_id": 0, "name": 1, "rfid_tag": 1, "presence": 1}):
            print(x)
            
        dump_json = json.dumps(x)
        student_itt = json.loads(dump_json)
        
        students_db_name = student_itt["name"]
        students_db_rfid = student_itt["rfid_tag"]
        students_db_presence_status = student_itt["presence"]
        
        print(students_db_presence_status)
        
def sign_in():
    
    # Useable ID with Mongodb
    new_id = json.dumps(id)
    
    # Search for RFID_Tag
    myquery = {"rfid_tag": new_id}
    
    # Update Presence values
    new_values_in = {"$set": {"presence": "IN"}}
    new_values_out = {"$set": {"presence": "OUT"}}

    # Find Presence in Mongodb with RFID_Tag
    find_pupil = mycol.find_one(myquery)
    pupils_presence_status = find_pupil["presence"]
    print(pupils_presence_status)
         
    
    # Set time Values
    current_time_without_dump = time.ctime()
    new_time = json.dumps(current_time_without_dump)
    new_value_time_regi = {"$set": {"time_registered": new_time}}
    
    # Register In Operation
    if pupils_presence_status == "OUT":
        mycol.update_one(myquery, new_values_in)
        mycol.update_one(myquery, new_value_time_regi)
        
    # Register Out Operation
    if pupils_presence_status == "IN":
        mycol.update_one(myquery, new_values_out)
        
    if pupils_presence_status == "N/A":
        mycol.update_one(myquery, new_values_in)
        mycol.update_one(myquery, new_value_time_regi)
        
        
        
    
    
def scan_rfid():
    global id
    try:
        print("Scan Your RFID Card")
        id = reader.read()[0]
        print ("The ID for this card is: ", id)
    finally:
        GPIO.cleanup()
        sign_in()
        time.sleep(3)
        scan_rfid()

scan_rfid()
