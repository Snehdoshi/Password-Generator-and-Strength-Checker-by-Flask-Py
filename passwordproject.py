from flask import Flask, render_template, request, jsonify
import string
import random
import re

app = Flask(__name__)

def generate_password(length, include_uppercase, include_numbers, include_special):
    if length < (include_uppercase + include_numbers + include_special):
        return None

    password = ''
    if include_uppercase:
        password += random.choice(string.ascii_uppercase)
    if include_numbers:
        password += random.choice(string.digits)
    if include_special:
        password += random.choice(string.punctuation)

    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    for _ in range(length - len(password)):
        password += random.choice(characters)

    password_list = list(password)
    random.shuffle(password_list)
    return ''.join(password_list)

def check_password_strength(password):
    strength = 0
    if len(password) >= 8:
        strength += 1
    if re.search('[a-z]', password):
        strength += 1
    if re.search('[A-Z]', password):
        strength += 1
    if re.search('[0-9]', password):
        strength += 1
    if re.search('[@#$%+=!]', password):
        strength += 1

    levels = {
        5: "Very Strong",
        4: "Strong",
        3: "Medium",
        2: "Weak",
        1: "Very Weak",
        0: "Very Weak"
    }
    return levels[strength]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    length = int(data['length'])
    include_uppercase = data['uppercase']
    include_numbers = data['numbers']
    include_special = data['special']
    password = generate_password(length, include_uppercase, include_numbers, include_special)
    if not password:
        return jsonify({'error': 'Password length too short for selected options.'})
    strength = check_password_strength(password)
    return jsonify({'password': password, 'strength': strength})

@app.route('/check', methods=['POST'])
def check():
    data = request.json
    password = data['password']
    strength = check_password_strength(password)
    return jsonify({'strength': strength})

if __name__ == '__main__':
    app.run(debug=True)
