from django.http import HttpResponse

def home(request):
	return HttpResponse ("Home de la mejor app de turismo")
