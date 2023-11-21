from django.urls import path
from onboarding.views import GetOrganizationAPIView, CreateOrganizationAPIView, ListServicesAPIView, RemainingServicesAPIView, EditOrganizationServicesAPIView, AddServiceAPIView


urlpatterns = [
    path('organization/<str:org_name>/', GetOrganizationAPIView.as_view(), name='get_organization_api'),
    path('create-organization/', CreateOrganizationAPIView.as_view(), name='create_organization_api'),
    path('list-services/', ListServicesAPIView.as_view(), name='list_services_api'),
    path('remaining-services/<str:org_name>/', RemainingServicesAPIView.as_view(), name='remaining_services_api'),
    path('edit-organization-services/<str:org_name>/', EditOrganizationServicesAPIView.as_view(), name='edit_organization_services_api'),
    path('add-service/', AddServiceAPIView.as_view(), name='add_service_api'),

]
