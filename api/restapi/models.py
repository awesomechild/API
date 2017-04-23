from __future__ import unicode_literals

from django.db import models


class Names(models.Model):
    student_id=models.IntegerField()
    names=models.CharField(max_length=100)
    roll=models.CharField(max_length=10)

    def __str__(self):
        return self.names + '     '+self.roll
