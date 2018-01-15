from CountBot import CountBot, MentionType, TimeInterval
from coinmarketcap import Market
import praw
import time
import operator

class CryptoCountBot(CountBot):
	__currencies = {}
	__words = []
	__coinMarketCap = None 

	def __init__(self, config, subreddits):
		self.__coinmarketcap = Market()
		tickers = self.__coinmarketcap.ticker()

		for ticker in tickers:
			self.__currencies[ticker['symbol'].lower()] = ticker['name'].lower()
			self.__words.append(ticker['symbol'].lower())
			self.__words.append(ticker['name'].lower())			

		print self.__words

		super(CryptoCountBot, self).__init__(config, subreddits, self.__words)

		return

	def print_cryptos_by_popularity(self, mentiontype=MentionType.POST, timeinterval=TimeInterval.DAY):
		resultdict = self.run_count_post_comment(mentiontype = mentiontype, timeinterval = timeinterval)

		postdict = resultdict[MentionType.POST]
		commentdict = resultdict[MentionType.COMMENT]

		cryptoresults = {}

		for word in postdict:
			if(word in self.__currencies):
				cryptoresults[self.__currencies[word]] = cryptoresults.get(self.__currencies[word], 0) + postdict[word]
			else:
				cryptoresults[word] = cryptoresults.get(word, 0) + postdict[word]

		for word in commentdict:
			if(word in self.__currencies):
				cryptoresults[self.__currencies[word]] = cryptoresults.get(self.__currencies[word], 0) + commentdict[word]
			else:
				cryptoresults[word] = cryptoresults.get(word, 0) + commentdict[word]

		sortedcryptos = sorted(cryptoresults.items(), key=operator.itemgetter(1), reverse=True)

		for crypto,result in sortedcryptos:
			print(crypto + ": " + str(result))

		return
