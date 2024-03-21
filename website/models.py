from django.db import models


    
class Record(models.Model):
	
	name = models.CharField(max_length=50)
	email = models.EmailField(max_length=50)
	image =  models.ImageField(upload_to='images/')
	title = models.CharField(max_length=100)
	description = models.TextField()
	vlog_image = models.ImageField(upload_to='vlogs/')
	def __str__(self):
		return(f"{self.name}")
