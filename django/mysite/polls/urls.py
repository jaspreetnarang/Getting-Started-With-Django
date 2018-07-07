from django.conf.urls import url
from . import views
from django.contrib.auth.views import login,logout

urlpatterns=[
url(r'^$',views.home),
url(r'^login/$', login , {'template_name': 'polls/login.html'}),
url(r'^logout/$', logout , {'template_name': 'polls/logout.html'}),
url(r'^signup/$', views.signup, name='signup'),
url(r'^profile/$', views.profile, name='profile')
]
