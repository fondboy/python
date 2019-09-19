from django.db import models

# Create your models here.
class Test(models.Model):
	name	= models.CharField(max_length=20);
	memo	= models.CharField(max_length=40);
	
class test_table2(models.Model):
	name	= models.CharField(max_length=10);
	
