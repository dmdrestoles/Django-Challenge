from django.urls import path, include
from .views import *

urlpatterns = [
	path('', index, name='index'),
	path('delete/', deleteEntry, name='deleteEntry'),
	path('edit/', editEntry, name='editEntry')
]