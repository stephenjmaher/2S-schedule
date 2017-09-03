from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^form$', views.get_name, name='getname'),
    url(r'^thanks$', views.thank_you, name='thankyou'),
    ]
