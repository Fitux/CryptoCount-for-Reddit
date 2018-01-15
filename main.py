from CryptoCountBot import CryptoCountBot
bot = CryptoCountBot(config='bot', subreddits=['cryptocurrency', 'cryptocurrencytrading'])
bot.print_cryptos_by_popularity()