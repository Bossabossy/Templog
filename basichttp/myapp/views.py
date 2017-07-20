from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from myapp.models import Record, Attribute, Node
#from myapp.models import Room
#http://localhost:8000/access_room/?temp=25.0&humi=80.0
def access_room(request):
	if request.method == 'GET':
		#print "GET: %s"%request.GET
		_temp=float(request.GET.get("temp",0))
		_humi=float(request.GET.get("humi",0))
		
		print ('temperature:{}'.format('_temp'))
		print ('humidity:{}'.format ('_humi'))

		Room.objects.create(temp=_temp, humi=_humi)
	else:
		print ("Not GET method")
	return HttpResponse("Hello")

def home(request):
	return render(request, 'home.html', {'key': "value" })
def access_room(request):
	return render(request, 'room.html', {'key': "value" })

def get_data(request):
	data = [{"time": str(i.created), i.attr.attribute:i.value} for i in Record.objects.all() ]
	return JsonResponse(data, safe=False)