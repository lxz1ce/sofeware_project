from django.db import models

# Create your models here.
class User(models.Model):
	username = models.CharField(max_length=10, unique=True)
	password = models.CharField(max_length=15)

	def __str__(self):
		return self.username

	class Meta:
		ordering = ['id']