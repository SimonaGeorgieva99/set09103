from flask import Flask, url_for
app = Flask(__name__)

@app.route("/")
def root():
	return "Default root. Go to /hello or /goodbye or /img"

@app.route("/hello/")
def hello():
	return "Hello Napier!!!"

@app.route("/img/")
def img():
	start = '<img src="'
	url = url_for('static', filename='vmask.jpg')
	end = '">'
	return start+url+end, 200

@app.route("/goodbye/")
def goodbye():
	return "Goodbye cruel world"

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
