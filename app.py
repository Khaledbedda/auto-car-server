from flask import Flask, request, jsonify
from PIL import Image 
import cv2
import numpy as np
import math
import cv



app = Flask(__name__)




directions =  {"direction": "F"}
steer_angle = 90

@app.route('/')
def hello_world():
    return 'Welcome to our server'
    
@app.route("/frame", methods=["POST"])
def process_image():
    file = request.files['image']
    file.save('im.jpg')
    x = cv.get_angle()
    # Read the image via file.stream
    # img = Image.open(file.stream)
    if x > 90 :
     directions.update({"direction": "L"})
    elif x < 90 : 
        directions.update({"direction": "R"}) 
    else : 
        directions.update({"direction": "F"}) 
    return jsonify({'msg': 'success'})

@app.route('/get_directions', methods=['GET'])
def get_directions():
        return jsonify(directions)



if __name__ == "__main__":
    app.run(debug=True)