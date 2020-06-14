from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        name = request.form.get('name')
        data = request.form
        write_to_db(data)
        return render_template('thank_you.html', value=name)
    else:
        return "Something went wrong. Try again!"


def write_to_db(data):
    with open('database.txt', 'a+') as db:
        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']
        db.write(f"\n{name}, {email}: {subject}, {message}")