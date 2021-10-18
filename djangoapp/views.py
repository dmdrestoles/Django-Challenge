from django.shortcuts import render, redirect
from .models import *

def index(request):

	context = {
		'person': Person.objects.all()
	}
	if (request.method == 'POST'):
		name = request.POST['name']

		query = Person(name=name)
		query.save()
	return render(request, 'djangoapp/index.html', context)

def deleteEntry(request):

	if (request.method == 'POST'):
		id = request.POST['id']

		Person.objects.get(id=id).delete()

	return redirect('index')

def editEntry(request):
	if (request.method == 'POST'):
		id = request.POST['id']
		name = request.POST['name']

		query = Person.objects.get(id=id)
		query.name = name
		query.save()
	
	return redirect('index')

