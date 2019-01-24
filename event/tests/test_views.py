import datetime

from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate, APIClient

from event.models import Event
from event.serializers import EventSerializer
from event.views import EventsViewSet


class EventViewTestCase(APITestCase):
    '''
    Overall Django based unit testing for views used within the custom Event model view set.
    '''

    def setUp(self):
        self.user = User.objects.get(pk=1)
        self.client_test.login(username=self.user.username, password='karimpassord')
        self.factory = APIRequestFactory()

        today = datetime.date.today()

        self.event = Event.objects.create(
            name='Test Event',
            venue='Test Venue',
            no_of_guest=200,
            start_date=today,
            end_date=today,
            created_by=self.user,
            created=today,
            modified_by=self.user,
            modified=today
        )

        self.data = {
            'name': 'Name',
            'venue': 'Venue',
            'no_of_guest': 123,
            'start_date': today,
            'end_date': today
        }

    def test_create_event(self):
        url = reverse('event-list')
        response = self.client_test.post(url, self.data)
        self.assertEqual(Event.objects.latest('id').name, "Name")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_event(self):
        url = reverse('event-detail', args=[self.event.id])
        response = self.client_test.delete(url)
        self.assertEqual(len(Event.objects.all()), 0)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_read_contact(self):
        url = reverse('event-detail', args=[self.event.id])
        response = self.client_test.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_contacts(self):
        url = reverse('event-list')
        response = self.client_test.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_contact(self):
        url = reverse('event-detail', args=[self.event.id])
        request = self.factory.get(url)
        data = EventSerializer(self.event, context={'request': request}).data
        data.update({'name': 'Update Name'})
        request = self.factory.put(url, data, format='json')
        force_authenticate(request, user=self.user)
        view = EventsViewSet.as_view({'put': 'update'})
        response = view(request, pk=data['id'])
        self.assertEqual(Event.objects.get(id=data['id']).name, 'Update Name')
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
