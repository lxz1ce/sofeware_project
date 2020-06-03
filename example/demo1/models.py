import os

from django.db import models

# Create your models here.


class User(models.Model):
	username = models.CharField(max_length = 10, unique = True)
	password = models.CharField(max_length = 15)
	email = models.EmailField()
	status_choice = [(0, '申请中'), (1, '已通过')]
	status = models.IntegerField(choices=status_choice, verbose_name='审核状态')
	active_code = models.CharField(max_length=20, verbose_name='验证码')

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
	pic_num = models.IntegerField(default=0)
	status_choice = [(0, '申请中'), (1, '已出租'), (2, '空闲')]
	status = models.IntegerField(choices=status_choice, verbose_name='审核状态', default=2)

	def __str__(self):
		return str(self.house_id)

	class Meta:
		ordering = ['house_id']


class Application(models.Model):
	apply_id = models.AutoField(primary_key=True)
	username = models.CharField(max_length=10)
	house_id = models.IntegerField()
	is_allowed = models.BooleanField(default=False)
	is_paid = models.BooleanField(default=False)
	allowed_by = models.CharField(max_length=10)
	rent_type = models.CharField(max_length=10)
	s_y = models.IntegerField()
	s_m = models.IntegerField()
	s_d = models.IntegerField()
	duration = models.IntegerField()

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


class Technician(models.Model):
	username = models.CharField(max_length=10, unique=True)
	password = models.CharField(max_length=15)
	contact_number = models.CharField(max_length=15)

	def __str__(self):
		return self.username

	class Meta:
		ordering = ['id']


class Repairing(models.Model):
	repair_id = models.AutoField(primary_key=True)
	username = models.CharField(max_length=10)
	house_id = models.IntegerField()
	is_allow = models.BooleanField(default=False)
	repair_technician = models.CharField(max_length=10)
	content = models.CharField(max_length=200)
	picture = models.ImageField('照片', upload_to='demo1/', blank=True, null=True)
	pic_num = models.IntegerField(default=0)

	def __str__(self):
		return str(self.repair_id)

	class Meta:
		ordering = ['repair_id']


class Reporting(models.Model):
	report_id = models.AutoField(primary_key=True)
	username = models.CharField(max_length=10)
	apply_id = models.IntegerField()
	title = models.CharField(max_length=40)
	content = models.CharField(max_length=200)
	picture = models.ImageField('照片', upload_to='demo1/', blank=True, null=True)
	pic_num = models.IntegerField(default=0)
	status_choice = [(0, '待处理'), (1, '已处理')]
	status = models.IntegerField(choices=status_choice, verbose_name='处理状态', default=0)
	handled_by = models.CharField(max_length=10, blank=True, null=True)
	handled_content = models.CharField(max_length=200, blank=True, null=True)

	def __str__(self):
		return str(self.report_id)

	class Meta:
		ordering = ['report_id']


class Message(models.Model):
	message_id = models.AutoField(primary_key=True)
	username = models.CharField(max_length=10)
	house_id = models.IntegerField()
	content = models.CharField(max_length=200)

	def __str__(self):
		return str(self.message_id)

	class Meta:
		ordering = ['message_id']


class MyMessage(models.Model):
	my_message_id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=20)
	context = models.CharField(max_length=200)
	sender = models.CharField(max_length=10)
	receiver = models.CharField(max_length=10)
	status_choice = [(0, '已读'), (1, '未读')]
	status = models.IntegerField(choices=status_choice, verbose_name='阅读状态')

	def __str__(self):
		return str(self.my_message_id)

	class Meta:
		ordering = ['my_message_id']