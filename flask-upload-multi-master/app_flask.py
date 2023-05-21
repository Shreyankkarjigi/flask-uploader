import os
import zipfile
from extractor import extract_zipfiles
from flask import Flask, request, redirect, url_for, flash, render_template
from werkzeug.utils import secure_filename
app = Flask(__name__)
#accept files using upload tool
@app.route("/Home")
def Home():
    # return render_template('index.html')
    return render_template('index.html')
    
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No File Part"
    file = request.files['file']
    if file.filename == '':
        return 'No file selected'
    file.save(file.filename)
    # extract_zipfiles(file.filename,"./outputs/")
    #run metcal script here
    return 'File uploaded successfully'



if __name__ == "__main__":
    app.run(debug=True)