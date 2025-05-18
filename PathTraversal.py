 import os
from flask import Flask, request, send_from_directory, abort

app = Flask(__name__)
FILES_DIR = './files'

@app.route('/download')
def download():
    filename = request.args.get('file')
    if not filename:
        abort(400, description="Missing 'file' parameter")
    
    # Prevent directory traversal
    safe_filename = os.path.basename(filename)
    file_path = os.path.join(FILES_DIR, safe_filename)
    
    if not os.path.isfile(file_path):
        abort(404, description="File not found")
    
    return send_from_directory(FILES_DIR, safe_filename, as_attachment=True)