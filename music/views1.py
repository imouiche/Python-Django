#from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
#from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Album

# Create your views here.
def index(request):
	# database API
	all_albums = Album.objects.all()
	#template = loader.get_template('music/index.html') # to load and return the template
	#infos that my template needs as a dcitionary
	context = {'all_albums': all_albums} #how we want to display index.html file
	#return HttpResponse(template.render(context, request))
	return render(request, 'music/index.html', context)
	# html = ''
	# for album in all_albums:
	# 	url = '/music/' + str(album.id) + '/'  # build the url for each album
	# 	#url = 'music'
	# 	html += '<a href=" '+url+' ">' + album.album_title + '</a><br>'
	
	
#call detail function whenever the request /music/ID path
def detail(request, album_id):
	#return HttpResponse("<h2> detail for album id: " + str(album_id) + " </h2>")
	# try:
	# 	album = Album.objects.get(pk=album_id)
	# except Album.DoesNotExist:
	# 	raise Http404("Album does " + str(album_id) + " not exist")
	album = get_object_or_404(Album, pk=album_id)
	return render(request, 'music/detail.html', {'album': album})

#define favorite page
def favorite(request, album_id):
	album = get_object_or_404(Album, pk=album_id)

	try:
		#get the ID of the selected song
		selected_song = album.song_set.get(pk=request.POST['song'])
	except (keyError, SongDoesNotExist):
		return render(request, 'music/detail.html',{
			'album':album,
			'error_message': "No valid song is selected"
			})
	else:
		#if everything is fine then save the selected song in the DB
		selected_song.is_favorite = True
		selected_song.save()
		return render(request, 'music/detail.html',{'album': album})



	""" <!-- <form action="{% url 'music:' album.id %}" method="post"> 
	{% csrf_token %} 
	{% for song in album.song_set.all %}
		<input type="radio" id="song{{forloop_counter}}" name="song" value="{{song.id}}">

		<label for="song{{forloop_counter}}">
			{{song.song_title}}
			{% if song.is_favorite %}
			<img src="http://i.imgur.com/b9b13Rd.png">
			{% endif %}
		</label><br>

	{% endfor %}
	<input type="submit" value="Favorite">
	</form> --> """






