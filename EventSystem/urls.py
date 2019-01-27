from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls import url
from django.conf import settings

from event.views import EventsViewSet

from rest_framework import routers

if settings.USE_DEBUG_TOOLBAR:
    import debug_toolbar

# used for routing the views within the each class viewset
router = routers.SimpleRouter()
router.register(r'events', EventsViewSet)

urlpatterns = [

    path('admin/', admin.site.urls),
    url(r'^$', EventsViewSet.as_view({'get': 'list'})),
    url(r'^', include(router.urls)),
]

if settings.USE_DEBUG_TOOLBAR:
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
