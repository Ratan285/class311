from flask import Flask, render_template
app = Flask(__name__)
@app.route("/ratan")
def student_webpage():
 name='ratan'
 return render_template('index.html',student_name = name)
app.run(debug = True)

