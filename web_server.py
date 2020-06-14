from flask import Flask, render_template, request
import csv

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
        try:
            data = request.form
            write_to_csv(data)
            return render_template('thank_you.html', value=data['name'])
        except IOError:
            return "Error. Didn't save to database."
    else:
        return "Something went wrong. Try again!"


def write_to_csv(data):
    with open('database.csv', mode='a+', newline='') as csv_db:
        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(csv_db, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, subject, message])
