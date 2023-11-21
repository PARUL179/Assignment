from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Organization, Service, Relationship
from .serializers import OrganizationSerializer, ServiceSerializer, RelationshipSerializer

class OnboardingAPITestCase(TestCase):
    def setUp(self):
        # Create sample data for testing
        self.organization_data = {'name': 'TestOrg', 'contact_info': 'test@example.com'}
        self.service_data = {'name': 'TestService', 'description': 'Description for testing'}

        self.organization = Organization.objects.create(**self.organization_data)
        self.service = Service.objects.create(**self.service_data)

        self.relationship_data = {'organization': self.organization, 'service': self.service}
        self.relationship = Relationship.objects.create(**self.relationship_data)

        # Create a test client
        self.client = APIClient()

    def test_create_organization(self):
        url = '/api/create_organization/'
        response = self.client.post(url, self.organization_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verify that the organization is created in the database
        organization = Organization.objects.get(name=self.organization_data['name'])
        self.assertIsNotNone(organization)

    def test_get_organization(self):
        url = f'/api/get_organization/{self.organization.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verify that the retrieved data matches the organization in the database
        self.assertEqual(response.data['name'], self.organization.name)
        self.assertEqual(response.data['contact_info'], self.organization.contact_info)

    def test_list_services(self):
        url = '/api/list_services/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verify that at least one service is listed
        self.assertGreater(len(response.data), 0)

    def test_associate_services(self):
        url = f'/api/associate_services/{self.organization.id}/'
        response = self.client.post(url, {'service_id': self.service.id}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verify that the relationship is created in the database
        relationship = Relationship.objects.get(organization=self.organization, service=self.service)
        self.assertIsNotNone(relationship)

    def test_invalid_associate_services(self):
        # Test associating a service to a non-existing organization
        url = '/api/associate_services/999/'
        response = self.client.post(url, {'service_id': self.service.id}, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
