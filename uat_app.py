from flask import Flask,render_template
from flaskext.mysql import MySQL

app = Flask(__name__)

myhome="HOME PAGE!Version2"


@app.route("/")		#http://127.0.0.1:5000
def get_home():
	return myhome

@app.route("/trainer")		#http://127.0.0.1:5000/contact
def trainer():
	return render_template("trainer_details.html")


if __name__ == "__main__":
	app.run(debug=True,host="0.0.0.0")



