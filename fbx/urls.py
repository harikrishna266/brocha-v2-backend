from django.urls import path
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'^$', views.listFbx.as_view(), name='listFbx')
]
