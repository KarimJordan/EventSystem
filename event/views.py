from rest_framework import viewsets, renderers, status
from rest_framework.response import Response
from rest_framework.decorators import action

from django.shortcuts import render

from .serializers import EventSerializer
from .models import Event


# view for Event utilizing model viewset from DRF
class EventsViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    template_name = None
    app_name = 'event'

    html = True

    # returns the list of event
    def list(self, request, *args, **kwargs):
        if self.template_name is None:
            self.template_name = self.app_name + 's/' + self.app_name + '_list.html'
        response = super(EventsViewSet, self).list(request, *args, **kwargs)
        return response

    def create(self, request, *args, **kwargs):
        self.template_name = self.name + '/' + self.name + '_form.html'
        context = {}
        response = Response(context)
        return response

    def dispatch(self, request, *args, **kwargs):
        if hasattr(request.resolver_match, 'namespaces'):
            if 'html' in request.resolver_match.namespaces:
                self.html = True
            return super(EventsViewSet, self).dispatch(request, *args, **kwargs)

    # override default renderer to HTMLRenderer()
    # can be configured to use either JSONRenderer() or TemplateHTMLRenderer()
    def get_renderers(self):
        if self.html:
            renderers_classes = [renderers.TemplateHTMLRenderer()]
        else:
            renderers_classes = [renderers.BrowsableAPIRenderer()]
        return renderers_classes
