from django.db import models

class Test(models.Model):
    name = models.CharField(max_length=20)
class InterTest(models.Model):
    pid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    method = models.CharField(max_length=20)
    url = models.CharField(max_length=64)
    params=models.CharField(max_length=1000,default='1')
    intername = models.CharField(max_length=64)
    creatdate = models.DateTimeField(auto_now_add=True)
    updatedate= models.DateTimeField(auto_now=True)

class Person(models.Model):
    name=models.CharField(max_length=32)
    age=models.IntegerField()
    location=models.CharField(max_length=200)
class Cars(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=64)
    displacement=models.FloatField()   #≈≈¡ø
    price=models.FloatField()
