from django.shortcuts import render
from functools import wraps
from django.contrib.auth.decorators import login_required
from .decorates import basicauth
from django.http import HttpResponseRedirect,HttpResponse  
from .models import Freelancer_eva, Client_eva
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
# Create your views here.

@basicauth
def freelancerView(request):
    if 'page' in request.GET:
        page = int(request.GET["page"])
        print page
        if page < 1:
            page = 1
        evas = Freelancer_eva.objects.order_by("-add_time")
        p = Paginator(evas,10)  # page_size = 10
        if p.count == 0:
            sub_evas=[]
            return render(request,'evaluation/freelancer_data.html',{"sub_evas":sub_evas,"page":page, "max_page":p.num_pages })
        try:
            sub_evas = p.page(page)
        except EmptyPage:
            page = p.num_pages
            sub_evas = p.page(page) 
        except PageNotAnInteger,InvalidPage:
            page = 1
            sub_evas = p.page(1)
        print page
        return render(request,'evaluation/freelancer_data.html',{"sub_evas":sub_evas,"page":page, "max_page":p.num_pages })
    else :
        page = 1
        evas = Freelancer_eva.objects.order_by("-add_time")
        p = Paginator(evas,10)  # page_size = 10
        sub_evas = []
        if p.count > 0:
            sub_evas = p.page(1)
        return render(request,'evaluation/freelancer.html',{"sub_evas":sub_evas,"page":1, "max_page":p.num_pages})
            

@basicauth
def add_freelancer_evaluation(request):
    name = request.POST['name']
    projectname = request.POST['projectname']
    if name == "" or projectname == "" or  bool(Freelancer_eva.objects.filter(name=name,projectname=projectname)):
        return render(request,"evaluation/add_fail.html",{"url":"/evaluation/freelancer"})
    eva = Freelancer_eva(name=name, projectname=projectname, eva_requirement=0, eva_management=0, eva_communication=0, eva_content="")
    eva.save()
    return HttpResponseRedirect("/evaluation/freelancer")
@basicauth
def delete_freelancer_evaluation(request):
    id = int(request.GET['id'])
    Freelancer_eva.objects.filter(id=id).delete()
    res = freelancerView(request)
    return res



@basicauth
def clientView(request):
    if 'page' in request.GET:
        page = int(request.GET["page"])
        print page
        if page < 1:
            page = 1
        evas = Client_eva.objects.order_by("-add_time")
        p = Paginator(evas,10)  # page_size = 10
        if p.count == 0:
            sub_evas=[]
            return render(request,'evaluation/client_data.html',{"sub_evas":sub_evas,"page":page, "max_page":p.num_pages })
        try:
            sub_evas = p.page(page)
        except EmptyPage:
            page = p.num_pages
            sub_evas = p.page(page) 
        except PageNotAnInteger,InvalidPage:
            page = 1
            sub_evas = p.page(1)
        return render(request,'evaluation/client_data.html',{"sub_evas":sub_evas,"page":page, "max_page":p.num_pages })
    else :
        page = 1
        evas = Client_eva.objects.order_by("-add_time")
        p = Paginator(evas,10)  # page_size = 10
        sub_evas = []
        if p.count > 0:
            sub_evas = p.page(1)
        return render(request,'evaluation/client.html',{"sub_evas":sub_evas,"page":1, "max_page":p.num_pages})

@basicauth
def add_client_evaluation(request):
    name = request.POST['name']
    projectname = request.POST['projectname']
    if name == "" or projectname == "" or  bool(Client_eva.objects.filter(name=name,projectname=projectname)): 
        return render(request,"evaluation/add_fail.html",{"url":"/evaluation/client"})
    eva = Client_eva(name=name, projectname=projectname, eva_progress=0, eva_quality=0, eva_service=0, eva_content="")
    eva.save()
    return HttpResponseRedirect("/evaluation/client")


@basicauth
def delete_client_evaluation(request):
    id = int(request.GET['id'])
    Client_eva.objects.filter(id=id).delete()
    res = clientView(request)
    return res
