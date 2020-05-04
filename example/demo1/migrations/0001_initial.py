# Generated by Django 3.0.3 on 2020-05-04 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10, unique=True)),
                ('password', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('status', models.IntegerField(choices=[(0, '申请中'), (1, '已通过')], verbose_name='审核状态')),
                ('active_code', models.CharField(max_length=20, verbose_name='验证码')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
