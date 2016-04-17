from django.shortcuts import render, render_to_response, get_object_or_404
from locations.models import BjjLocation


# Create your views here.
def location(request):
	return render_to_response('location.html', {
		'locations': BjjLocation.all()	})
