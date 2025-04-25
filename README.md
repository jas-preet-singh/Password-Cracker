<h1>File Upload and Processing Web Application</h1>
This is a simple web application built using Flask that allows users to upload files (PDF, TXT, PNG, JPG, JPEG, GIF) and processes them to extract information, such as generating a password for the uploaded file. The application provides a user-friendly interface for file uploads and displays relevant success or error messages.

<b>#Features</b>
File Upload: Users can upload files of specified formats (PDF, TXT, PNG, JPG, JPEG, GIF).
Validation: The application checks for valid file uploads and ensures that files are not empty.
Secure Handling: Uploaded files are saved securely using werkzeug's secure_filename method.
File Processing: The application integrates with a custom module (word) to process the uploaded files and generate a password.
User Feedback: Displays success or error messages based on the upload status.
Technologies Used
Python
Flask
HTML/CSS
Werkzeug
Installation
Clone the repository:
bash
Insert Code
Edit
Copy code
git clone https://github.com/SJaspreet01/Password_Cracker
Navigate to the project directory:
bash
Insert Code
Edit
Copy code
cd repository-name
Install the required packages:
bash
Insert Code
Edit
Copy code
pip install Flask
Run the application:
bash
Insert Code
Edit
Copy code
python app.py
Open your web browser and go to http://127.0.0.1:5000/.
Usage
Navigate to the home page.
Use the file upload form to select and upload a file.
After uploading, the application will display the generated password for the file.
