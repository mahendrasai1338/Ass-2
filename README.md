# CI/CD Pipeline with Environment-Based Deployment and Health Checks

## Project Overview
This project demonstrates a CI/CD pipeline for a containerized FastAPI application with basic environment separation and deployment validation.

The application exposes:
- `/` → main endpoint
- `/health` → health check endpoint

The solution supports:
- automatic CI execution on code push
- Docker image build and push
- health-based validation
- separate dev and prod environments
- manual production promotion
- rollback using a previous image tag

---

## Tech Stack
- Python FastAPI
- Docker
- GitHub Actions
- Docker Hub

---

## Project Structure

```text
.
├── .github/
│   └── workflows/
│       ├── ci-cd.yml
│       ├── promote-prod.yml
│       └── rollback.yml
├── app/
│   ├── __init__.py
│   └── main.py
├── tests/
│   └── test_app.py
├── Dockerfile
├── docker-compose.dev.yml
├── docker-compose.prod.yml
├── .env.dev
├── .env.prod
├── requirements.txt
└── README.md

Application Endpoints
/
Returns a basic response showing the environment and version.
/health
Returns the health status of the application.
Example response:
JSON
{
  "status": "ok",
  "environment": "dev",
  "version": "dev-latest"
}

Functional Requirements Covered
This project implements the assignment requirements:

simple application with one API and /health
Dockerfile for containerized execution
CI pipeline on every push
dev and prod environment separation
automatic validation after dev deployment
manual promotion to production
reuse of the same tested image version for prod
rollback using a previous image tag
environment variables with separate config files

Dockerization
The application is containerized using Docker.

Build the image locally
docker build -t sample-app .
Run with dev configuration
docker run --env-file .env.dev -p 8000:8000 sample-app
Run with prod configuration
docker run --env-file .env.prod -p 8002:8000 sample-app
Environment Configuration
.env.dev

Used for development settings.

.env.prod

Used for production settings.

This avoids hardcoded values and keeps configuration environment-specific.

CI/CD Pipeline Flow
1. Code Push

Whenever code is pushed to the configured branch, the GitHub Actions workflow starts automatically.

2. Install Dependencies

The workflow installs Python packages from requirements.txt.

3. Run Tests

Basic tests are executed using pytest.

4. Build Docker Image

The workflow builds a Docker image for the application.

5. Version Handling

The Docker image is tagged using the Git commit SHA.

Example:

sample-app:87d86606736c382ecad51bd946d73754e7d5c

This ensures every build has a unique version.

6. Push Docker Image

The image is pushed to Docker Hub with:

commit SHA tag
latest tag
7. Health Validation

After the build, the workflow runs the application and validates it using:

/health

If the health check fails, the pipeline stops.

Promotion Logic
Development
validated automatically through the CI workflow after every push
Production
production deployment is manual
triggered using promote-prod.yml
requires an image_tag input
pulls the same already-tested image from Docker Hub
does not rebuild the image

This ensures production uses the exact version that was already validated.

Version Handling

Versioning is based on Git commit SHA.

Benefits:

each build has a unique version
easy traceability between code and image
same version can be promoted to production
rollback becomes simple using older tags

Example image:

<dockerhub-username>/sample-app:<commit-sha>
Rollback Logic

Rollback is handled using rollback.yml.

manual trigger
user provides a previous image_tag
workflow pulls that image from Docker Hub
application is started again with production configuration
/health is checked to verify rollback success
Local Development
Create virtual environment
python -m venv venv
Activate virtual environment (Git Bash)
source venv/Scripts/activate
Install dependencies
python -m pip install -r requirements.txt
Run the app locally
python -m uvicorn app.main:app --reload --port 8001
Run tests
python -m pytest
GitHub Actions Workflows
ci-cd.yml

Handles:

install
test
Docker build
Docker push
health validation
promote-prod.yml

Handles:

manual production promotion
deployment of the same tested image tag
rollback.yml

Handles:

manual rollback to a previous image version
