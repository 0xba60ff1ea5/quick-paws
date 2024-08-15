from Links import *

class User:
	def __init__(self, username):
		"""
		Common User attributes
		"""
		self.username = username.replace(" ", "").lower()
		self.user = URL_USER(self.username)
		self.gallery = URL_GALLERY(self.username)
		self.scraps = URL_SCRAPS(self.username)
		self.favorites = URL_FAVORITES(self.username)
		self.journals = URL_JOURNALS(self.username)
		self.commissions = URL_COMMISSIONS(self.username)
		self.stats = URL_STATS(self.username)

	def __repr__(self):
		"""
		Export the instance as a JSON-formatted string
		"""
		username = f"\"username\":\"{self.username}\", "
		user = f"\"user\":\"{self.user}\", "
		gallery = f"\"gallery\":\"{self.gallery}\", "
		scraps = f"\"scraps\":\"{self.scraps}\", "
		favorites = f"\"favorites\":\"{self.favorites}\", "
		journals = f"\"journals\":\"{self.journals}\", "
		commissions = f"\"commissions\":\"{self.commissions}\", "
		stats = f"\"stats\":\"{self.stats}\""
		return "{" + username + user + gallery + scraps + favorites + journals + commissions + stats + "}"

	def __str__(self):
		"""
		Return a formatted string
		"""
		opening = 	f"\n"
		username = 	f"  username:     {self.username}\n"
		user = 		f"  user:         {self.user}\n"
		gallery = 	f"  gallery:      {self.gallery}\n"
		scraps = 	f"  scraps:       {self.scraps}\n"
		favorites = 	f"  favorites:    {self.favorites}\n"
		journals = 	f"  journals:     {self.journals}\n"
		commissions = 	f"  commissions:  {self.commissions}\n"
		stats = 	f"  stats:        {self.stats}\n"
		return opening + username + user + gallery + scraps + favorites + journals + commissions + stats
