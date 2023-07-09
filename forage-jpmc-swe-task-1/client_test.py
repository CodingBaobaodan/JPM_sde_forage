import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):

  # check the functionality of function getDataPoint() under standard circumstances
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

  # check the functionality of function getDataPoint() when Bid price is greater than Ask price
  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))

  ### checking for the alternative function getRatio() that can throw exceptions
  # check the functionality of function getRatio() when the divisor is zero
  #def test_getRatio_calculateRatiozero(self):
  #  prices = [
  #    {'ABC': 0, 'DEF': 0},
  #    {'ABC': 20, 'DEF': 0}
  #  ]
  #  # check if the function raise the ZeroDivisionError exception
  #  for price in prices:
  #    self.assertRaises(ZeroDivisionError, getRatio, price['ABC'], price['DEF'])
    


  """ ------------ Add more unit tests ------------ """



if __name__ == '__main__':
    unittest.main()
