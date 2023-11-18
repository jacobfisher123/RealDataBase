from django.db import models 
from django.shortcuts import render
from django import forms

class GrdClsA_news(models.Model):
	Title=models.CharField(max_length=200)
	Subtitle=models.CharField(max_length=50)
	Desc=models.TextField(max_length=500)
	Due_Date=models.DateTimeField()
	posted_date=models.DateTimeField(verbose_name='posted_date', auto_now_add=True)
	def __str__(self):
		return "{}-{}".format(self.Title, self.posted_date)

