# SaaS Onboarding Project

This Django project provides APIs for onboarding organizations to our SaaS product.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Database Setup](#database-setup)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Documentation](#documentation)
- [Version Control](#version-control)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- Pip (Python package installer)
- Virtualenv (optional but recommended)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/saas-onboarding.git


## API Endpoints

### Get Organization
Endpoint: `/organization/<str:org_name>/`

- **Method**: GET
- **Description**: Retrieve details for a specific organization.
- **Example**: `/organization/acme-corp/`

### Create Organization
Endpoint: `/create-organization/`

- **Method**: POST
- **Description**: Create a new organization.
- **Example**: `/create-organization/`

### List Services
Endpoint: `/list-services/`

- **Method**: GET
- **Description**: List available services.
- **Example**: `/list-services/`

### Remaining Services
Endpoint: `/remaining-services/<str:org_name>/`

- **Method**: GET
- **Description**: List remaining services for a specific organization.
- **Example**: `/remaining-services/acme-corp/`

### Edit Organization Services
Endpoint: `/edit-organization-services/<str:org_name>/`

- **Method**: PUT
- **Description**: Edit services for a specific organization.
- **Example**: `/edit-organization-services/acme-corp/`

### Add Service
Endpoint: `/add-service/`

- **Method**: POST
- **Description**: Add a new service.
- **Example**: `/add-service/`

## Usage

To interact with these API endpoints, you can use tools like `curl` or any API client of your choice. Make sure to include the necessary parameters and handle the responses appropriately.

### Example using `curl`

```bash
# Retrieve details for a specific organization
curl -X GET http://example.com/organization/acme-corp/

# Create a new organization
curl -X POST -d "org_name=acme-corp&..." http://example.com/create-organization/

# List available services
curl -X GET http://example.com/list-services/

# List remaining services for a specific organization
curl -X GET http://example.com/remaining-services/acme-corp/

# Edit services for a specific organization
curl -X PUT -d "services=[...]" http://example.com/edit-organization-services/acme-corp/

# Add a new service
curl -X POST -d "service_name=new-service&..." http://example.com/add-service/


## How to run the Project
- Git clone the project with ``` git clone https://github.com/Laxmika1401/RESTAPI_task.git```
- Create your virtualenv with `Pipenv` or `virtualenv` and activate it.
- Install Requirements.txt using this command: `pip install -r requirements.txt`
- Run the Application using this command: `python manage.py runserver` 
- API Documentation: `http://localhost:8000/docs/`

