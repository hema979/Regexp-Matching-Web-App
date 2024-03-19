 
from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    test_string = request.form['test_string']
    regex_pattern = request.form['regex_pattern']
    matches = re.finditer(regex_pattern, test_string, re.MULTILINE)
    match_info = []

    for match in matches:
        start = match.start()
        end = match.end()
        if start > 0 and test_string[start - 1] == '\n':
            start -= 1
        match_info.append({
            'span': (start, end),
            'text': match.group()
        })

    if not match_info:
        return render_template('no_match.html')
    else:
        return render_template('results.html', match_info=match_info)

@app.route('/validate_email', methods=['POST'])
def validate_email():
    email = request.form['email']
    regex_pattern = r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'
    is_valid = re.match(regex_pattern, email) is not None
    return render_template('email_validation.html', email=email, is_valid=is_valid)

if __name__ == '__main__':
    app.run(debug=True)
