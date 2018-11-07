from django.views import generic #import generic 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Album

#create two generic views

class IndexView(generic.ListView):
	template_name = 'music/index.html' # use index,html to display the album
	#you can use object_list var instead of all_albums and comment the next line
	context_object_name = 'all_albums' 

	"""docstring for IndexView"""
	# def __init__(self, arg):
	# 	super(IndexView, self).__init__()
	# 	self.arg = arg
	def get_queryset(self):
		return Album.objects.all()

class DetailView(generic.DetailView):
	model = Album
	template_name = 'music/detail.html'

# class to create an album on the webpage
class AlbumCreate(CreateView):
	model = Album
	#fields = '__all__'
	fields = ['artist', 'album_title', 'genre', 'album_logo']
		
