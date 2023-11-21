# your_app/tests/test_views.py
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from onboarding.models import Organization, Service

class OnboardingGetAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.service = Service.objects.create(service_id=1, service_name='audit')
        # Create an organization and associate the service
        self.organization = Organization.objects.create(
            org_id=1,
            org_name='org1',
            org_phone='1234567890',
            org_email='org1@gmail.com'
        )
        self.organization.service.add(self.service)

    def test_get_service(self):
        BASE_URL='http://127.0.0.1:8000/api/v1/'
        url = BASE_URL+'list-services/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_organisation(self):
        BASE_URL='http://127.0.0.1:8000/api/v1/'
        org_name= 'org1'
        url = BASE_URL+'organization/'+org_name+'/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data['org_id'], self.organization.org_id)
        self.assertEqual(response.data['org_name'], self.organization.org_name)
        self.assertEqual(response.data['org_phone'], self.organization.org_phone)
        self.assertEqual(response.data['org_email'], self.organization.org_email)
        self.assertEqual(len(response.data['service']), 1)
        self.assertEqual(response.data['service'][0]['service_id'], self.service.service_id)
        self.assertEqual(response.data['service'][0]['service_name'], self.service.service_name)

    def test_create_organization_api(self):
        BASE_URL='http://127.0.0.1:8000/api/v1/'
        # Set up API endpoint URL
        api_url = BASE_URL+'create-organization/'

        # Set up organization data for the request
        organization_data = {
            'org_id': 2,
            'org_name': 'test org1',
            'org_phone': '1234567890',
            'org_email': 'testorg1@gmail.com',
            'service': [1]
        }

        print(organization_data,api_url)
        # Make a POST request to the API to create the organization
        response = self.client.post(api_url, organization_data, format='json')

        # Assert the response status code
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert that the organization was created in the database
        created_organization = Organization.objects.get(org_id=organization_data['org_id'])
        self.assertEqual(created_organization.org_name, organization_data['org_name'])
        self.assertEqual(created_organization.org_phone, organization_data['org_phone'])
        self.assertEqual(created_organization.org_email, organization_data['org_email'])

    def test_update_service_in_organization_api(self):
        BASE_URL='http://127.0.0.1:8000/api/v1/'
        org_name='org1'
        # Set up API endpoint URL
        api_url = BASE_URL+'edit-organization-services/'+org_name+'/'

        self.service = Service.objects.create(service_id=2, service_name='BVG')
        # Set up organization data for the request, including the updated service
        updated_organization_data = {
            'service_name':'BVG'
        }

        # Make a PUT request to the API to update the organization
        response = self.client.put(api_url, updated_organization_data, format='json')

        # Assert the response status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)