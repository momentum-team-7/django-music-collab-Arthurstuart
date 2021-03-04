from django.shortcuts import render, get_object_or_404
from .models import Album
from .models import Artist
from django.http import  HttpResponse

# Create your views here.
def album_search(request):
    albums = Album.objects.all()
    return render(request, 'index.html', {'albums': albums})

def artist_search(request):
    artists = Artist.objects.all()
    return render(request, 'artists.html', {'artists': artists})

def album_details(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'album-details.html', {'album': album})

def add_artist(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ArtistForm()
        return render(request, 'add-artist.html', {'form':form})

def edit_artist(request, pk):
    if request.method == 'POST':
        form = ArtistForm(request.PATCH, instance=artist)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('templates/edit-artist.html')
        else:
            form = ArtistForm()
            return render(request, 'templates/artist.html')

def delete_artist(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    artist.delete()
    return HttpResponseRedirect('/')

def edit_album(request, pk):
    if request.method == 'POST':
        form = AlbumForm(request.PATCH, instance=album)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('album.html')
        else:
            form = AlbumForm(instance=album)
        return render(request, templates/edit-album.html,{'form':form, album:album})

