import praw
import time
from enum import Enum

class TimeInterval(Enum)
	HOUR = 60 * 60
	DAY = 60 * 60 * 24
	WEEK = 60 * 60 * 24 * 7
	MONTH = 60 * 60 * 24 * 30
	YEAR =  60 * 60 * 24 * 365

class MentionType(Enum)
	POST = 'post'
	COMMENT = 'comment'
	POST_COMMMENT = 'post_comment'

class CountBot(object):
	__reddit = None
	__config = None
	__subs = []
	__words = []
	__subseparator = '+'
	__wordseparator = ' OR '

	def __init__(self, config, subreddits, words):
		self.__config = config
		self.__subs = subreddits
		self.__words = words

		self.__reddit = praw.Reddit(self.__config)

		return

	def run_count_post_comment(self, subreddits=self.__subs, words=self.__words, mentiontype=MentionType.POST, timeinterval=TimeInterval.DAY):
		current_timestamp = time.time()
		word_dict_post = {}
		word_dict_comments = {}
		last_timestamp = timeinterval

		subsStr = self.__subseparator.join(subreddits)
		words = self.__words

		subreddit = self.__reddit.subreddit(subsStr)

		for word in words:
			word_dict_post[word] = 0
			word_dict_comments[word] = 0

		for submission in subreddit.submissions(start=last_timestamp, end=current_timestamp):
			submissiontxt = submission.selftext.lower()
			for word in words:
				if(word in submissiontxt):
					word_dict_post[word] = word_dict_post[word] + 1
			
			if('comment' in mentiontype)
				for comment in submission.comments:
					commenttxt = comment.body.lower()
					for word in words:
						if(word in commenttxt):
							word_dict_comments[word] = word_dict_comments[word] + 1

		return {MentionType.POST : word_dict_post, MentionType.COMMENT : word_dict_comments}
