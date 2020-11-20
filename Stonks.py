import yfinance as yf

def get_price(ticker_symbol):
	ticker = yf.Ticker(ticker_symbol)
	try:
		num_price = ticker.info['regularMarketPrice']
		price = f"The current market price of {ticker_symbol} is ${num_price}."
		return price
	
	except ValueError as e:
		e = str(e)
		if e == "No tables found":
			return "Pick a real ticker symbol you jackass!"
		else:
			return "Unknown ValueError detected"
	except KeyError as e:
		print(e)
		error_string = str(e).replace("'", "")
		if error_string == "regularMarketOpen":
			return "That market isn't open you jackass!  There's no price to be had."
		else:
			return "Unknown KeyError detected"
