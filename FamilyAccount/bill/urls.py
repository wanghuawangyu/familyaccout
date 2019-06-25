from django.conf.urls import url
from bill import views

urlpatterns = [

    url(r'^home$', views.Home.as_view()),

]