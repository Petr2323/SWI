from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import re

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# User model with SQLAlchemy
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)

# Initialize DB
@app.before_first_request
def init_db():
    db.create_all()

# Simple email validation regex
EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")

def is_valid_email(email):
    return EMAIL_REGEX.match(email) is not None

def is_valid_name(name):
    # Check type and length
    if not isinstance(name, str):
        return False
    if not (2 <= len(name) <= 50):
        return False
    # Allow only letters, spaces, hyphens, apostrophes (basic sanitization)
    if not re.match(r"^[A-Za-z\s\-']+$", name):
        return False
    return True

@app.route('/save', methods=['POST'])
def save_user():
    try:
        data = request.get_json(force=True)  # force=True to ensure JSON is parsed or error

        name = data.get('name')
        email = data.get('email')

        if not name or not email:
            return jsonify({"error": "Missing 'name' or 'email'"}), 400

        if not is_valid_name(name):
            return jsonify({"error": "Invalid 'name'. Must be 2-50 characters and only letters, spaces, hyphens, apostrophes."}), 400

        if not is_valid_email(email):
            return jsonify({"error": "Invalid 'email' format."}), 400

        # Check for existing user with same email
        if User.query.filter_by(email=email).first():
            return jsonify({"error": "Email already exists."}), 409

        # Create and add user
        user = User(name=name.strip(), email=email.strip())
        db.session.add(user)
        db.session.commit()

        return jsonify({"message": "User saved successfully", "user_id": user.id}), 201

    except Exception as e:
        # Log the error in real app, but for now just send generic message
        return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    app.run(debug=True)
