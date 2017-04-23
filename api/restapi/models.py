from __future__ import unicode_literals

from django.db import models

#id is being automatically generated therefore there is no need for it
#we can retrive that data from that id itself
class Names(models.Model):
    names=models.CharField(max_length=100)
#Deleting roll number also since it is not required. Tring to be professional
#Anyways

    def __str__(self):
        return self.names
