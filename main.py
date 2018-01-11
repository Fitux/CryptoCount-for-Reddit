import operator

x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_x = sorted(x.items(), key=operator.itemgetter(1))
bot = CryptoCountBot('bot', ['cryptocurrency'])
bot.run_count_post_comment_today()