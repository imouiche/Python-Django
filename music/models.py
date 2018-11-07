from django.db import models
#from django.core.urlresolvers import reverse
from django.urls import reverse

# Create your models here. The model is the blueprint
#of our data that will be stored in the database
## Each album is going to have its uniq PrimaryKey set auto by Django
class Album(models.Model):
	#column in the database
	artist = models.CharField(max_length=250) # define var of type char with lenght 250
	album_title = models.CharField(max_length=500)
	genre = models.CharField(max_length=100)
	album_logo = models.CharField(max_length=10000)

	def get_absolute_url(self):
		return reverse('music:detail', kwargs={'pk':self.pk})
	#let's define the rendered information
	def __str__(self):
		return self.album_title + ' ' + self.artist 

class Song(models.Model):
	album = models.ForeignKey(Album, on_delete=models.CASCADE)
	file_type= models.CharField(max_length=10)
	song_title= models.CharField(max_length=250)
	is_favorite = models.BooleanField(default=False)
	
	def __str__(self):
		return self.song_title 
		
