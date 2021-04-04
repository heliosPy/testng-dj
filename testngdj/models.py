from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=250)
    age = models.IntegerField()


class Parent(models.Model):
    name = models.CharField(db_column='ParentName', max_length=200)
    child = models.ForeignKey('Student', models.DO_NOTHING)
    age = models.CharField(db_column='Age', max_length=10)
