from flask import Flask, render_template, request
import requests
import json

def get_market_price(API):
	link = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-detail?region=US&lang=en&symbol=" + API

	r = requests.get(link, headers={"X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com",
									"X-RapidAPI-Key": "0587951f5fmshda844c78f376736p116ba0jsne32933f75ab2"})
	apiData = r.json()
	closed_price = apiData["price"]["regularMarketPreviousClose"]["raw"]
	return closed_price

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
	apple = get_market_price("AAPL")

	apple_purchase = round(apple, 2)
	apple_target = round(apple * 1.2, 2)
	apple_loss = round(apple * 0.95, 2)

	fb = get_market_price("FB")

	fb_purchase = round(fb, 2)
	fb_target = round(fb * 1.1, 2)
	fb_loss = round(fb * 0.95, 2)

	dropbox = get_market_price("DBX")

	dbx_purchase = round(dropbox, 2)
	dbx_target = round(dropbox * 2, 2)
	dbx_loss = round(dropbox * 0.5, 2)


	return render_template("Portfolio.html", title = "Stocks Portfolio / Holdings",
						   apple_purchase=apple_purchase, apple_target=apple_target, apple_loss=apple_loss,
						   fb_purchase=fb_purchase, fb_target=fb_target, fb_loss=fb_loss,
						   dbx_purchase=dbx_purchase, dbx_target=dbx_target, dbx_loss=dbx_loss)

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
