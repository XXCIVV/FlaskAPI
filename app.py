from flask import Flask, request, jsonify
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET', 'POST'])
def index(): 
    return "BU PROJECT MDT TESTING"

@app.route('/uploads', methods=['GET'])
def upload_file():
    file = request.files['file']  # Get the file from the request

    # Save the file to the UPLOAD_FOLDER
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)  # Save file to disk

    return jsonify({"message": "File uploaded successfully", "file_path": file_path}), 200

if __name__ == '__main__':
    app.run(debug=True)

    
