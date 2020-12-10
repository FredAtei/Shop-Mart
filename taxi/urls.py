from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.index, name='home'), 
    url(r'^taxis/', views.taxi, name='taxi'),  
    url(r'^profile/(?P<profile_id>\d+)', views.profile, name='profile'),
]