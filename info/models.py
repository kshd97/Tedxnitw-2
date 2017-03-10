from __future__ import unicode_literals

from django.db import models
import datetime

# Create your models here.

def get_speakerpic_path(instance,filename):
	return 'speakers/{0}/{1}'.format(instance.name,filename)

def get_memberpic_path(instance,filename):
	return 'members/{0}/{1}'.format(instance.member_name,filename)

def get_logo_path(instance,filename):
	return 'partners/{0}/{1}'.format(instance.name,filename)

class Speaker(models.Model):
	YEAR_CHOICES = []
	for r in range(1980, (datetime.datetime.now().year+1)):
	    YEAR_CHOICES.append((r,r))

	name = models.CharField(max_length=200)
	year = models.IntegerField(('year'), max_length=4, choices=YEAR_CHOICES, default=datetime.datetime.now().year)
	picture = models.ImageField(upload_to=get_speakerpic_path,null=True,blank=True)
	about = models.TextField(null=True, blank=True)
	facebook = models.CharField(max_length = 300, null=True,blank=True)
	email = models.CharField(max_length = 300,null=True,blank=True)
	contact = models.CharField(max_length=20,null=True,blank=True)
	linkedin = models.CharField(max_length=200,null=True,blank=True)

	def __unicode__(self):
		return (self.name)

class Partner(models.Model):
	YEAR_CHOICES = []
	for r in range(1980, (datetime.datetime.now().year+1)):
	    YEAR_CHOICES.append((r,r))

	name = models.CharField(max_length=200)
	year = models.IntegerField(('year'),max_length=4, choices=YEAR_CHOICES, default=datetime.datetime.now().year)
	logo = models.ImageField(upload_to=get_logo_path,null=True,blank=True)
	category = models.CharField(max_length=200)

	def __unicode__(self):
		return (self.name)

class TeamMember(models.Model):
	member_name = models.CharField(max_length=200)
	team_name = models.CharField(max_length=200)
	pic = models.ImageField(upload_to=get_memberpic_path,null=True,blank=True)
	facebook = models.CharField(max_length = 300, null=True,blank=True)
	email = models.CharField(max_length = 300,null=True,blank=True)
	contact = models.CharField(max_length=20,null=True,blank=True)
	linkedin = models.CharField(max_length=200,null=True,blank=True)

	def __unicode__(self):
		return (self.member_name)
