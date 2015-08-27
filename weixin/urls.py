from django.conf.urls import include, url
from . import views

urlpatterns = [
   url(r'^freelancer$', views.freelancerView),
   url(r'^freelancer/add',views.add_freelancer_eva),
   url(r'^client$', views.clientView),
   url(r'^client/add',views.add_client_eva),
]
