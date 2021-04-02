from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=250)
    age = models.IntegerField()


class Parent(models.Model):
    name = models.CharField(db_column='ParentName', max_length=200)
    modified = models.DateTimeField(db_column='Modified_on')
    child = models.ForeignKey('Student', models.DO_NOTHING)