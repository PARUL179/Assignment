
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from onboarding.models import Organization, Service  # Import your models
from onboarding.api.v1.serializers import OrganizationSerializer, ServiceSerializer

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title= 'Onboarding API')

class GetOrganizationAPIView(APIView):
    def get(self, request, org_name):
        # Retrieve organization by org_id or return a 404 response if not found
        organization = get_object_or_404(Organization, org_name=org_name)
        service_list = organization.service.all()
        organization_data = {
            'org_id': organization.org_id,
            'org_name': organization.org_name,
            'org_email': organization.org_email,
            'org_phone': organization.org_phone,
            'service': service_list.values()
        }
        # Return a JSON response with the organization data
        return Response(organization_data, status=status.HTTP_200_OK)

class CreateOrganizationAPIView(APIView):
    def post(self, request):
        # Deserialize the request data using the serializer
        serializer = OrganizationSerializer(data=request.data)

        # Validate the data
        if serializer.is_valid():
            # Save the organization to the database
            serializer.save()

            # Return a success response
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Return a response with errors if the data is not valid
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListServicesAPIView(APIView):
    def get(self, request):
        # Retrieve all services from the database
        services = Service.objects.all()

        # Serialize the services data
        serializer = ServiceSerializer(services, many=True)

        # Return a JSON response with the serialized services data
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class RemainingServicesAPIView(APIView):
    def get(self, request, org_name):
        try:
            organization = Organization.objects.get(org_name=org_name)
            all_services = Service.objects.all()
            remaining_services = all_services.exclude(organization=organization)

            serializer = ServiceSerializer(remaining_services, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Organization.DoesNotExist:
            return Response({'detail': 'Organization not found'}, status=status.HTTP_404_NOT_FOUND)
        
class EditOrganizationServicesAPIView(APIView):
    def put(self, request, org_name):
        try:
            organization = Organization.objects.get(org_name=org_name)

            # Get the list of service IDs from the request data
            service_names = request.data.get('service',[])

            # Set the organization's services to the selected services
            organization.service.set(service_names)

            # Save the changes
            organization.save()

            return Response({'detail': 'Services updated successfully'}, status=status.HTTP_200_OK)
        except Organization.DoesNotExist:
            return Response({'detail': 'Organization not found'}, status=status.HTTP_404_NOT_FOUND)


class AddServiceAPIView(APIView):
    def post(self, request):
        serializer = ServiceSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)