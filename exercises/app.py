from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home_page():
	list1 = ["or","orr","orrr"]
	{% for i in list1 %}
	{% endfor %}
	return render_template("index.html")

if __name__ == '__main__':
   app.run(debug = True)