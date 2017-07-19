from __future__ import unicode_literals
from django.db import models


class Node(models.Model):
	node_name=models.CharField(max_length=100)
	description=models.CharField(max_length=100)
	def __str__(self):
		return "{}:{}:{}".format(self.id, self.node_name, self.description)

class Record(models.Model):
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)
	node=models.ForeignKey(Node, on_delete=models.CASCADE)
	value=models.FloatField(default=0.0)


class Attribute(models.Model):
	attribute=models.CharField(max_length=100)
	description=models.CharField(max_length=100)






