from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response

def home( request ) :
	return render_to_response( 'home.html', locals() )