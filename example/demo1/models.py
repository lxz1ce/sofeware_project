import os

from django.db import models

# Create your models here.


class User(models.Model):
	username = models.CharField(max_length = 10, unique = True)
	password = models.CharField(max_length = 15)
	email = models.EmailField()
	status_choice = [(0, '申请中'), (1, '已通过')]
	status = models.IntegerField(choices = status_choice, verbose_name = '审核状态')
	active_code = models.CharField(max_length = 20, verbose_name = '验证码')

	def __str__(self):
		return self.username

	class Meta:
		ordering = ['id']

class House(models.Model):
	house_id = models.AutoField(primary_key=True)
	house_name = models.CharField(max_length=50)
	short_leasing = models.BooleanField(default=False)
	short_leasing_fee = models.IntegerField(null=True, blank=True)
	long_leasing = models.BooleanField(default=False)
	long_leasing_fee = models.IntegerField(null=True, blank=True)
	house_type_choice = [(0, '单人间'), (1, '双人间'), (2, '四人间')]
	house_type = models.IntegerField(choices=house_type_choice, verbose_name='房间类型', blank=True, null=True)
	district = models.CharField(max_length=10, blank=True, null=True)
	address = models.CharField(max_length=100, blank=True, null=True)
	contact_number = models.CharField(max_length=15, default='未知', blank=True, null=True)
	picture = models.ImageField('照片', upload_to='demo1/', blank=True, null=True)

	def __str__(self):
		return str(self.house_id)

	class Meta:
		ordering = ['house_id']


class Application(models.Model):
	apply_id = models.AutoField(primary_key=True)
	username = models.CharField(max_length=10)
	house_id = models.IntegerField()
	is_allow = models.BooleanField(default=False)
	def __str__(self):
		return str(self.apply_id)

	class Meta:
		ordering = ['apply_id']


class Customerserver(models.Model):
	username = models.CharField(max_length=10, unique=True)
	password = models.CharField(max_length=15)

	def __str__(self):
		return self.username

	class Meta:
		ordering = ['id']