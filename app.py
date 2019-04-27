from flask import Flask, render_template

class User:
	balance = 10000
	stocks_value = 5000

app = Flask(__name__)

@app.route('/')
@app.route('/home')

def home():
	# default directory for home page
	return render_template("Home.html", title = "Welcome Back")

@app.route('/stocks')

def stocks():
	# directing user to page 2 (list of stocks)
	return render_template("Stocks.html", title = "Stocks Listing")

@app.route('/portfolio')

def holdings():
	# directing user to page 3 (portfolio / list of stocks purchased / history)
	return render_template("Portfolio.html", title = "Stocks Portfolio / Holdings")

if __name__ == '__main__':
	app.run(debug=True)
