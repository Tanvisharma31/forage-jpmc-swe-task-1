################################################################################
#
#  Permission is hereby granted, free of charge, to any person obtaining a
#  copy of this software and associated documentation files (the "Software"),
#  to deal in the Software without restriction, including without limitation
#  the rights to use, copy, modify, merge, publish, distribute, sublicense,
#  and/or sell copies of the Software, and to permit persons to whom the
#  Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
#  OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.

import json
import random
import urllib.request

# Server API URLs
QUERY = "http://localhost:8080/query?id={}"

# 500 server request
N = 500


def getDataPoint(quote):
    """ Produce all the needed values to generate a datapoint """
    """ ------------- Update this function ------------- """
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])
    price = (bid_price + ask_price) / 2  # Calculate price as the average of bid and ask prices
    return stock, bid_price, ask_price, price



def getRatio(price_a, price_b):
    """ Get ratio of price_a and price_b """
    """ ------------- Update this function ------------- """
    if price_b != 0:
        return price_a / price_b
    else:
        return float('inf') if price_a != 0 else 1.0




# Main
if __name__ == "__main__":
    # Query the price once every N seconds.
    for _ in iter(range(N)):
        quotes = json.loads(urllib.request.urlopen(QUERY.format(random.random())).read())

        # Dictionary to store stock prices
        prices = {}

        # Populate prices dictionary with data points
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            print("Quoted %s at (bid:%s, ask:%s, price:%s)" % (stock, bid_price, ask_price, price))
            prices[stock] = price  # Store price for each stock

        # Calculate and print the ratio
        for stock, price in prices.items():
            # Get the ratio of each stock with every other stock
            for other_stock, other_price in prices.items():
                if stock != other_stock:  # Avoid calculating ratio with itself
                    ratio = getRatio(price, other_price)
                    print("Ratio %s/%s: %s" % (stock, other_stock, ratio))

