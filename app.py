from flask import Flask, render_template, request
import requests
import json

r=requests.get("https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-detail?region=US&lang=en&symbol=AAPL",
			   headers={"X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com",
						"X-RapidAPI-Key": "0587951f5fmshda844c78f376736p116ba0jsne32933f75ab2"})
apiData = r.json()

openPrice = apiData["price"]["regularMarketOpen"]["raw"]
closedPrice = apiData["price"]["regularMarketPreviousClose"]["raw"]

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
	closed_price = round(closedPrice, 2)
	target_price = round(closedPrice * 1.2, 2)
	stop_loss_price = round(closedPrice * 0.95, 2)
	return render_template("Portfolio.html", title = "Stocks Portfolio / Holdings", closed_price = closed_price,
						   target_price=target_price, stop_loss_price = stop_loss_price)

@app.route('/purchase')
def purchase():
	# directing user to page 4 (portfolio / list of stocks purchased / history)
	return render_template("Purchase.html", title = "Purchase Screen")


@app.route('/purchase-check')
def purchasecheck():
	# directing user to page 4 (portfolio / list of stocks purchased / history)
	return render_template("Purchase-check.html", title = "Purchase Screen")


if __name__ == '__main__':
	app.run(debug=True)
