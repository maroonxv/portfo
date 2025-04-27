from flask import Flask, render_template, url_for, request
import csv
app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template('index.html', )

@app.route("/works/")
def works():
    return render_template('works.html',)

@app.route("/about/")
def about():
    return render_template('about.html',)

@app.route("/work/")
def work():
    return render_template('work.html',)

@app.route("/contact/")
def contact():
    return render_template('contact.html',)

@app.route('/contact/submit_form', methods=['POST', 'GET'])
def submit_form():

    # the code below is executed if the request method
    # was GET or the credentials were invalid

    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        write_to_csv(data)
    return render_template('thankyou.html',)

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

