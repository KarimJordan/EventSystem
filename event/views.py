from rest_framework import viewsets, renderers
from rest_framework.decorators import action
from rest_framework.response import Response

from django.shortcuts import render

from .serializers import EventSerializer
from .models import Event


# view for Event utilizing model viewset from DRF
class EventsViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    template_name = None

    name = 'event'

    html = True

    # returns the list of event
    def list(self, request, *args, **kwargs):
        print(self.name)
        if self.template_name is None:
            self.template_name = self.name + '/' + self.name + '_list.html'
        response = super(EventsViewSet, self).list(request, *args, **kwargs)
        return response

    # override default renderer to HTMLRenderer()
    def get_renderers(self):
        # can be configured to use either JSONRenderer() or TemplateHTMLRenderer()
        render_classes = [renderers.TemplateHTMLRenderer()]
        return render_classes
