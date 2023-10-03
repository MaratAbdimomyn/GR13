from django.contrib import admin
from django.urls import path, re_path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', CarView.as_view(), name='home'),
    re_path(r'^about/(?P<id>\d+)/$', AboutCar.as_view(), name='about')
    ]
