from django import forms
from .model import Artist, Album

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name']

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        field = ['title', 'artist', 'album_release']