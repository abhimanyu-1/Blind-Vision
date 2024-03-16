from flask import Flask, render_template, request, redirect, flash
import os
from lap import cam
from phone import camera

app = Flask(__name__)

# Define the upload folder
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Set the secret key for flashing messages
app.secret_key = 'your_secret_key_here'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/System/', methods=['POST'])
def start_system():
    # Call the cam() function from lap.py
    cam()
    # Flash message indicating the system action
    flash('System action initiated', 'info')
    return redirect('/')

@app.route('/Mobile/', methods=['POST'])
def start_mobile():
    # Call the camera() function from phone.py
    camera()
    # Flash message indicating the mobile action
    flash('Mobile action initiated', 'info')
    return redirect('/')

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        if 'ocr_file' not in request.files:
            return redirect(request.url)
        file = request.files['ocr_file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # Optionally, you can do further processing with the uploaded file here
            message = 'File uploaded successfully!'
            return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
