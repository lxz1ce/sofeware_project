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