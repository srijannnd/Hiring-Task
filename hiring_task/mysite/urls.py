# MYSITE URLS.PY
from django.conf.urls import url
from . import views

app_name = 'mysite'

urlpatterns = [
    url(r'^$', views.index, name='index'),
]