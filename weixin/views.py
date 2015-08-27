from django.shortcuts import render
from django.http import HttpResponse 
from manage.models import Freelancer_eva,Client_eva
# Create your views here.
def freelancerView(request):
    try:
        id = int(request.GET['id'])
    except KeyError:
        try:
            name = request.GET['name'].encode("utf8")
            projectname = request.GET['projectname'].encode("utf8")
            
        except KeyError:
            response = HttpResponse()
            response.status_code = 400
            return response
        print name,projectname
        eva = Freelancer_eva.objects.filter(name=name,projectname=projectname)
        if bool(eva):
            eva = eva[0]
            context = {"name":eva.name,"projectname":eva.projectname,"eva_requirement":eva.eva_requirement,"eva_management":eva.eva_management,"eva_communication":eva.eva_communication,"eva_content":eva.eva_content}
        else:
            context = {"name":name,"projectname":projectname}
        return render(request,"weixin/freelancer.html",context)

    eva = Freelancer_eva.objects.filter(id=id)
    if bool(eva) :
        eva = eva[0]
        context = {"name":eva.name,"projectname":eva.projectname,"eva_requirement":eva.eva_requirement,"eva_management":eva.eva_management,"eva_communication":eva.eva_communication,"eva_content":eva.eva_content}
        return render(request,"weixin/freelancer.html",context)
    else :
            response = HttpResponse()
            response.status_code = 400
            return response

def add_freelancer_eva(request):
    name = request.POST['name']
    projectname = request.POST['projectname']
    eva_requirement = int(request.POST['eva_requirement'])
    eva_management = int(request.POST["eva_management"])
    eva_communication = int(request.POST["eva_communication"])
    eva_content = request.POST['eva_content']
    eva_content = eva_content.replace("\n","\\n")
    if name == "" or projectname == "" or  eva_content == "" or not 1 <= eva_requirement <= 5 or not 1 <= eva_management <=5 or not 1 <= eva_communication <= 5 : 
        return HttpResponse("fail")
    eva = Freelancer_eva.objects.filter(name=name,projectname=projectname)
    if bool(eva):
        eva = eva[0]
        eva.eva_requirement = eva_requirement
        eva.eva_management = eva_management
        eva.eva_communication = eva_communication
        eva.eva_content = eva_content
        eva.save()
    else:
        eva = Freelancer_eva(name=name, projectname=projectname, eva_requirement=eva_requirement, eva_management=eva_management, eva_communication=eva_communication, eva_content=eva_content)
        eva.save()
    return HttpResponse("ok")

def clientView(request):
    try:
        id = int(request.GET['id'])
    except KeyError:
        try:
            name = request.GET['name'].encode("utf8")
            projectname = request.GET['projectname'].encode("utf8")
            
        except KeyError:
            response = HttpResponse()
            response.status_code = 400
            return response
        print name,projectname
        eva = Client_eva.objects.filter(name=name,projectname=projectname)
        if bool(eva):
            eva = eva[0]
            context = {"name":eva.name,"projectname":eva.projectname,"eva_progress":eva.eva_progress,"eva_quality":eva.eva_quality,"eva_service":eva.eva_service,"eva_content":eva.eva_content}
        else:
            context = {"name":name,"projectname":projectname}
        return render(request,"weixin/client.html",context)

    eva = Client_eva.objects.filter(id=id)
    if bool(eva) :
        eva = eva[0]
        context = {"name":eva.name,"projectname":eva.projectname,"eva_progress":eva.eva_progress,"eva_quality":eva.eva_quality,"eva_service":eva.eva_service,"eva_content":eva.eva_content}
        return render(request,"weixin/client.html",context)
    else :
            response = HttpResponse()
            response.status_code = 400
            return response

def add_client_eva(request):
    for i in request:
        print i
    name = request.POST['name']
    projectname = request.POST['projectname']
    eva_progress = int(request.POST['eva_progress'])
    eva_quality = int(request.POST["eva_quality"])
    eva_service = int(request.POST["eva_service"])
    eva_content = request.POST['eva_content']
    eva_content = eva_content.replace("\n","\\n")
    if name == "" or projectname == "" or  eva_content == "" or not 1 <= eva_progress <= 5 or not 1 <= eva_quality <=5 or not 1 <= eva_service <= 5 : 
        return HttpResponse("fail")
    eva = Client_eva.objects.filter(name=name,projectname=projectname)
    if bool(eva):
        eva = eva[0]
        eva.eva_progress = eva_progress
        eva.eva_quality = eva_quality
        eva.eva_service = eva_service
        eva.eva_content = eva_content
        eva.save()
    else:
        eva = Client_eva(name=name, projectname=projectname, eva_progress=eva_progress, eva_quality=eva_quality, eva_service=eva_service, eva_content=eva_content)
        eva.save()
    return HttpResponse("ok")





