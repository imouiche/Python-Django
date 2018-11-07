from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views  # import view from current directory
app_name='music'

#log possible urls/paths that will be requested by user from the app'sview
urlpatterns = [
	# /music/
    path('', views.IndexView.as_view(), name='index'), #define the default home page called index
# /music/712
##url(r'^$', views.IndexView.as_view(), name='index'),
# extract the album id as a variable. The + is going to add any following integer
	#path('(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
	#path('<int:album_id>/', views.DetailView.as_view(), name = 'detail' ),

	#whenever we use a view it expets the primary key
	path('<int:pk>/', views.DetailView.as_view(), name = 'detail' ),
	#url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
	
# /music/<album_id>/favorite => to select a favorite song
	#url(r'^(?P<album_id>[0-9]+)/favorite', views.favorite, name='favorite'),
	#path('<int:album_id>/favorite', views.favorite, name = 'favorite'),
 # add url for the create Album class
 # music/album/add, no pk as we want to create a new album so no pk yet
   path('album/add/', views.AlbumCreate.as_view(), name='album-add'),
   # url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),
]
