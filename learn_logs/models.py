from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#表
class Topic(models.Model):
    #字段
    text = models.CharField(max_length=200)
    date_added = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.text

class Entry(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.text[:50] + '...'
class Addfile(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    date_added = models.DateField(auto_now_add=True)
    upload = models.FileField(upload_to='uploads/%Y%m%d')
class Person(models.Model):
    name = models.CharField(max_length=120)

class Group(models.Model):
    name = models.CharField(max_length=120)
    member = models.ManyToManyField(Person)
'''
class Membership(models.Model):
    person = models.ForeignKey(Person,on_delete=models.CASCADE)
    group = models.ForeignKey(Group,on_delete=models.CASCADE)
    join_date = models.DateField()
'''




