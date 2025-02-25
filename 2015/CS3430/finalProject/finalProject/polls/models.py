import datetime

from django.db import models
from django.utils import timezone


# Create your models here.

class Category(models.Model):
	description = models.CharField(max_length=20)

	def __unicode__(self):
		return self.description


class Item(models.Model):
	price = models.IntegerField(default=0)
	description = models.CharField(max_length=20)
	category = models.ForeignKey(Category)
	picture = models.CharField(max_length=50)
	# description = models.CharField(max_length=200)
	# myQ = models.ForeignKey(Question)

	def __unicode__(self):
		return self.description


# class User(models.Model):
# 	price = models.IntegerField(default=0)
# 	description = models.CharField(max_length=20)
# 	category = models.ForeignKey(Category)
# 	picture = models.CharField(max_length=50)
# 	# description = models.CharField(max_length=200)
# 	# myQ = models.ForeignKey(Question)

# 	def __unicode__(self):
# 		return self.description


# class Question(models.Model):
# 	question_text = models.CharField(max_length=200)
# 	pub_date = models.DateTimeField('date published')

# 	def __unicode__(self):
# 		return self.question_text

# 	def was_published_recently(self):
# 		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
# 	was_published_recently.admin_order_field = 'pub_date'
# 	was_published_recently.boolean = True
# 	was_published_recently.short_description = 'Published recently?'


# class Choice(models.Model):
# 	question = models.ForeignKey(Question)
# 	choice_text = models.CharField(max_length=200)
# 	votes = models.IntegerField(default=0)

# 	def __unicode__(self):
# 		return self.choice_text


	
