from rest_framework import viewsets, renderers, status
from rest_framework.response import Response
from rest_framework.decorators import action

from django.contrib.auth.models import User

from django.shortcuts import render, redirect, reverse

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
            self.template_name = self.app_name + '/' + self.app_name + '_list.html'
        response = super(EventsViewSet, self).list(request, *args, **kwargs)
        return response

    def destroy(self, request, *args, **kwargs):
        super(EventsViewSet, self).destroy(request, *args, **kwargs)
        return redirect('event-list')

    # returns the detailed info per event
    def retrieve(self, request, *args, **kwargs):
        if self.template_name is None:
            self.template_name = self.app_name + '/' + self.app_name + '_detail.html'

        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        context = {'event': data}
        return Response(context)

    # insert data
    def create(self, request, *args, **kwargs):

        if self.template_name is None:
            self.template_name = self.app_name + '/' + self.app_name + '_form.html'
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():

            # if data submitted is valid based on serializer then insert to database
            self.perform_create(serializer)

            # redirect back to event list
            response = redirect('event-list')
        else:

            # if data is invalid then just redirect back to create form
            event = serializer.data
            context = {'event': event}
            response = Response(context)
        return response

    def perform_create(self, serializer):
        if self.request.user.id is None:
            temp_user = User.objects.get(pk=2)
            serializer.save(created_by=temp_user, modified_by=temp_user)
        else:
            serializer.save(created_by=self.request.user, modified_by=self.request.user)

    def update(self, request, *args, **kwargs):
        if self.template_name is None:
            self.template_name = self.app_name + '/' + self.app_name + '_form.html'

        # get object instance first
        instance = Event.objects.get(pk=kwargs.get('pk'))

        if 'name' not in request.data:

            # will populate data forms when edit is clicked
            serializer = self.get_serializer(instance)
            event = serializer.data
            context = {
                'event': event
            }
            response = Response(context)
        else:
            partial = kwargs.pop('partial', False)
            serializer = self.get_serializer(instance, data=request.data, partial=partial)

            if serializer.is_valid():
                # if update or save is clicked then perform update on the item and redirect to event details
                self.perform_update(serializer)
                response = redirect(reverse('event-detail', kwargs={'pk': kwargs['pk']}))
            else:
                # if data submitted is incorrect then it will redirect back to the form
                event = serializer.data
                context = {
                    'event': event
                }
                response = Response(context)
        return response

    def perform_update(self, serializer):
        if self.request.user.id is None:
            temp_user = User.objects.get(pk=2)
            serializer.save(modified_by=temp_user)
        else:
            serializer.save(modified_by=self.request.user)

    def get_queryset(self):
        query_set = super(EventsViewSet, self).get_queryset()
        if self.action == 'list':
            query_set = query_set.order_by('-end_date')
        return query_set

    def post(self, request, *args, **kwargs):
        # CRUD functions but only for POST method.
        if '_method' in request.data and request.data['_method'] == 'delete':
            response = self.destroy(request, *args, **kwargs)
        elif '_method' in request.data and request.data['_method'] == 'update':
            response = self.update(request, *args, **kwargs)
        else:
            response = super(EventsViewSet, self).post(request, *args, **kwargs)
        return response

    # override default renderer to HTMLRenderer()
    # can be configured to use either JSONRenderer() or TemplateHTMLRenderer()
    def get_renderers(self):
        if self.html:
            renderers_classes = [renderers.TemplateHTMLRenderer()]
        else:
            renderers_classes = [renderers.BrowsableAPIRenderer()]
        return renderers_classes
