from django.conf import settings
from django.db import models
from items.models import Item
from people.models import Person

class Action(models.Model):
	"""docstring for Action"""

	#Actions
	NOTHING = 'NO'
	LIKE = 'LK'
	SHARE = 'SH'
	REPOST = 'RP'
	FAVOR = 'FV'
	FOLLOW = 'FL'
	BUY = 'BY'
	ACTIONS_TYPES = (
		(NOTHING, 'Nothing'),
		(LIKE, 'Like'),
		(SHARE, 'Share'),
		(REPOST, 'Repost'),
		(FAVOR, 'Favor'),
		(FOLLOW, 'Follow'),
		(BUY, 'Buy'),
		)

	person = models.ForeignKey(settings.AUTH_USER_MODEL)
	action = models.CharField(max_length=2, choices=ACTIONS_TYPES, default=NOTHING)
	item = models.ForeignKey(Item)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return '%s - %s - %s' % (self.person, self.action, self.item)

