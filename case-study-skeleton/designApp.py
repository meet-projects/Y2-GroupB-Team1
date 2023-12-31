from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase


config = {
  "apiKey": "AIzaSyD7KwDBguJLTFBjh8ysizEGtou-4bv7-V0",
  "authDomain": "travlerpack-c53e3.firebaseapp.com",
  "projectId": "travlerpack-c53e3",
  "storageBucket": "travlerpack-c53e3.appspot.com",
  "messagingSenderId": "167060716254",
  "appId": "1:167060716254:web:f135ccf81d19241c60604f",
  "databaseURL": "https://travlerpack-c53e3-default-rtdb.firebaseio.com/"
};




firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

app = Flask(__name__, template_folder='templates',static_folder='static')

slides = [
    {'image':"https://images.squarespace-cdn.com/content/v1/596d5a0b6b8f5b88b9eb4437/1682011748937-9DR04ZBG2CIYM02STIVQ/image-asset.jpeg?format=750w",'text':'image1', 'url': 'https://www.instagram.com/p/CrQ7mZNrKJp/'},
    {'image':"https://images.squarespace-cdn.com/content/v1/596d5a0b6b8f5b88b9eb4437/1681942977089-WT41RNR6DCVNRB7WTP25/image-asset.jpeg?format=750w",'text':'image2','url':'https://www.instagram.com/p/CrOUFdzrtrf/'},
    {'image':"https://images.squarespace-cdn.com/content/v1/596d5a0b6b8f5b88b9eb4437/1681856698840-FQYNZG6YOK8IHBITKLO5/image-asset.jpeg?format=500w",'text':'image3','url':'https://www.instagram.com/p/CrMV5Sfv0sV/'},
    {'image':"https://images.squarespace-cdn.com/content/v1/596d5a0b6b8f5b88b9eb4437/1681619039201-F13DAZ93FLN5D7IZLJA2/image-asset.jpeg?format=500w",'text':'image4','url':'https://www.instagram.com/p/CrFU8ucOwmI/'},
    {'image':"https://images.squarespace-cdn.com/content/v1/596d5a0b6b8f5b88b9eb4437/1681619039769-DXV8OI7U6EOIMLJLSHIE/image-asset.jpeg?format=500w",'text':'image5','url':'https://www.instagram.com/p/CrEhLyrvYW9/'},
    {'image':"https://images.squarespace-cdn.com/content/v1/596d5a0b6b8f5b88b9eb4437/1681619040414-LW367S8SK9RHM8TXIBZJ/image-asset.jpeg?format=500w",'text':'image6','url':'https://www.instagram.com/p/CrBV_TSxct7/'},
    {'image':"https://images.squarespace-cdn.com/content/v1/596d5a0b6b8f5b88b9eb4437/1681619041088-EFHBBZ0HZRIFMTO30DCV/image-asset.jpeg?format=500w",'text':'image7','url':'https://www.instagram.com/p/Cq6nARKv3is/?img_index=1'},
    {'image':"https://images.squarespace-cdn.com/content/v1/596d5a0b6b8f5b88b9eb4437/1681619042246-36GMZYYS49G3WEM96RX8/image-asset.jpeg?format=500w",'text':'image8','url':'https://www.instagram.com/p/Cq5qz3ovYNn/'}
]

@app.route('/', methods = ["POST", "GET"])
def deign():
    num_slides = len(slides)  # Calculate the number of slides
    return render_template('design.html', slides=slides, num_slides=num_slides)

@app.route('/design')
def productdesign():
    return render_template('product_design.html')

@app.route('/about', methods = ["POST", "GET"])
def timeline():
    return render_template('aboutpage_gabby.html')

@app.route('/contact', methods = ["POST", "GET"])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['comment']
        username = request.form['username']

        # Save the feedback to Firebase
        feedback_data = {
            'name': name,
            'email': email,
            'message': message,
            'username' : username,
        }
        # db.child('feedback').push(feedback_data)

        db.child("users").child(username).set(feedback_data)
        info = db.child("users").child(username).get().val()
        n = info['name']
        return render_template('contact.html', b = True, name = n) 
    return render_template('contact.html', b = False) 

# @app.route('/submit_feedback', methods=['GET','POST'])
# def submit_feedback():
    
#         return redirect(url_for('contact'))


if __name__ == '__main__':
    app.run(debug=True)
