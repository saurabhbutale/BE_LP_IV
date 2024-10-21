# app.py

from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os
from summarizer import summarize_pdf

app = Flask(__name__)

# Folder to store uploaded files
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Allowed extensions for file upload
ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route to render the main page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle file upload and summarization
@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if a file is uploaded+
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    
    file = request.files['file']

    # Check if file has a valid filename and is a PDF
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    
    if file and allowed_file(file.filename):
        # Save the uploaded file
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Summarize the PDF
        summary = summarize_pdf(file_path, word_limit=200)

        # Return the summary to the frontend
        return render_template('index.html', summary=summary)

    flash('Allowed file type is PDF')
    return redirect(request.url)

if __name__ == '__main__':
    app.secret_key = 'supersecretkey'
    app.run(debug=True)
