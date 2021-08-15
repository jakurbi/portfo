from flask import Flask, render_template, redirect, request
import os
import csv

app = Flask(__name__)

@app.route('/')
def my_home():
    return redirect('/index.html')

@app.route('/<string:page>')
def html_page(page):
    return render_template(page)

def write_to_file(data):
    with open('venv\database.txt', 'a') as database:
        fullname = data['full_name']
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{fullname},{email},{subject},{message}')

def write_to_csv(data):
    with open('venv\database.csv', 'a', newline='') as database2:
        fullname = data['full_name']
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([fullname,email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thanks.html')
        except:
            return 'something wrong'
    else:
        return 'Fail!'