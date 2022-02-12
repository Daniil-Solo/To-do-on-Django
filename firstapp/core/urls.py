from django.urls import path
from .views import *

urlpatterns = [
    path('home/', NoteHome.as_view(), name='home'),
    path('archive/', NoteArchive.as_view(), name='archive'),
    path('new_note/', NoteNew.as_view(), name='new_note'),
]