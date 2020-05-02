from flask import Flask, render_template, send_from_directory, url_for, request, redirect
import os
import csv
os.chdir("/Users/W541/Desktop")
app = Flask(__name__)


@app.route('/')
def hello_world():

    return render_template("index.html")


@app.route('/<string:page_name>')
def home(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n email: {email}\n subject: {subject}\n message: {message}')

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer (database2, delimiter =',', quotechar="'", quoting= csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method== "POST":
        data = request.form.to_dict()

        write_to_csv(data)

        return redirect("/thanks.html")

    else:
        return "Try again"


# @app.route('/works.html')
# def works():
#     return render_template('works.html')
#
#
# @app.route('/about.html')
# def about_me():
#     return render_template('about.html')
#
# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')
#
# @app.route('/components.html')
# def components():
#     return render_template('components.html')