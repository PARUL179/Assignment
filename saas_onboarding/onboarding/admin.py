from django.contrib import admin

# Register your models here.
from onboarding.models import Organization, Service  # Import your Service model

admin.site.register(Service)
admin.site.register(Organization)