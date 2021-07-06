from django.db import models

#Create three models classes as - Name, ID, Contact, Address and migrate
#them into the database and at the end populate them with 30 random values.

# The wording is ambiguous: "Name, ID, Contact, Address" There are four things here.
# I am going to assume those are the FOUR fields of the THREE models each having
# same fields

class ModelOne(models.Model):
    name = models.CharField(max_length=30)
    id = models.CharField(max_length=30, primary_key=True)
    address = models.CharField(max_length=60)
    contact = models.IntegerField()

class ModelTwo(models.Model):
    name = models.CharField(max_length=30)
    id = models.CharField(max_length=30, primary_key=True)
    address = models.CharField(max_length=60)
    contact = models.IntegerField()

class ModelThree(models.Model):
    name = models.CharField(max_length=30)
    id = models.CharField(max_length=30, primary_key=True)
    address = models.CharField(max_length=60)
    contact = models.IntegerField()
