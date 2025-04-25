from flask import Flask, render_template, request, url_for
import os
from werkzeug.utils import secure_filename
import word as key

filepath=0
app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'txt', 'png', 'jpg', 'jpeg', 'gif'}

# Create uploads folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return render_template('index.html', error='No file part')
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            return render_template('index.html', error='No selected file')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            filepath=file_path
            # key.main(file_path)

            print(f'File uploaded to: {file_path}')
            render_template('index.html', success=f'File {filename} uploaded successfully!')  # Print the path of the uploaded file
            print(f'File uploaded to: {filepath}') 
            filepass=key.main(file_path) # Print the path of the uploaded file
            render_template('index.html', success=f'File {filename} uploaded successfully!')
            # return render_template('index.html', success=f'File {filename} uploaded successfully!')
            return render_template('index.html', success=f'File password is {filepass} ')
        
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)