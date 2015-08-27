from django.conf.urls import include, url

from . import views
#
urlpatterns = [
    url(r'^freelancer$', views.freelancerView),        
    url(r'^freelancer/add$', views.add_freelancer_evaluation),
    url(r'^freelancer/delete$', views.delete_freelancer_evaluation),
    url(r'^client$', views.clientView),        
    url(r'^client/add$', views.add_client_evaluation),
    url(r'^client/delete$', views.delete_client_evaluation),
    
]
