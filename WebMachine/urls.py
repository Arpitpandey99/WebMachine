
from django.contrib import admin
from django.conf.urls import url
from Analysis.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^$", Home),
]

