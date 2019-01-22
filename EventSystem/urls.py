from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls import url

from event.views import EventsViewSet

from rest_framework import routers

# used for routing the views within the each class viewset
router = routers.SimpleRouter()
router.register(r'events', EventsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
]
