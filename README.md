# DevSecOps Pipeline — CMPE58E Term Project

This repository demonstrates a complete **DevSecOps CI/CD pipeline** for a containerized Python web application (Flask), deployed to **Google Kubernetes Engine (GKE)** with integrated security scans and quality gates.

---

## Project Structure

```
.
├── src/                    # Flask application source code
│   └── app/
├── tests/                 # Unit tests
├── k8s/                   # Kubernetes deployment & service YAMLs
├── Dockerfile             # Docker image definition
├── requirements.txt       # Python dependencies
├── dev-requirements.txt   # Lint/test dependencies
├── sonar-project.properties
└── .github/workflows/
    └── devsecops-pipeline.yml
```

---

## CI/CD Pipeline Overview

The project is built around a **single GitHub Actions workflow** (`devsecops-pipeline.yml`) that runs the following stages sequentially:

| Stage              | Description                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| Checkout         | Pull source code from repo                                                  |
| Lint & Test       | Run `pylint` and Python `unittest`                                         |
| SonarQube Scan   | Static analysis for code quality and smells                                |
| Docker Build     | Build Docker image for the Flask app                                       |
| Trivy Scan       | Scan Docker image for vulnerabilities (HIGH/CRITICAL)                      |
| Artifact Push    | Push image to Google Artifact Registry                                     |
| GKE Deploy       | Apply Kubernetes manifests to deploy app                                   |

Each step must pass for the next to run — if any **test or scan fails**, deployment is blocked. ✅

---

## Security Tools Integrated

- **Trivy** — Docker image & Python package vulnerability scanning
- **SonarQube** — Static code analysis and quality gates
- **OPA Gatekeeper** — Kubernetes admission control to allow only trusted images

---

## Cloud Infrastructure

- **Artifact Registry** — Image storage (`europe-west3-docker.pkg.dev`)
- **Google Kubernetes Engine** — Production-grade Kubernetes cluster
- **GitHub Secrets** — CI credentials and sensitive variables

---

## Deployment

The application is deployed to a **Google Kubernetes Engine (GKE)** cluster using the following Kubernetes manifests:

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

Once deployed, the application is exposed via a **LoadBalancer** service. You can access the application using the external IP assigned to the service.

#### Example request:

```http
GET http://<EXTERNAL-IP>/hello
```

#### Example response:

```json
{ "message": "Hello, DevSecOps!" }
```

#### Example request:

```http
GET http://<EXTERNAL-IP>/bye
```

#### Example response:

```json
{ "message": "Bye, DevSecOps!" }
```
---

## Gatekeeper Policy

- Enforces that only images from:
  ```
  europe-west3-docker.pkg.dev/crack-willow-460419-n9/hello-app
  ```
  are allowed in the cluster

Blocked deployments show:
```
denied by only-allow-artifact-repo: image not in allowed repo list
```

---

## Requirements

- Python 3.10
- Docker
- Terraform (optional)
- GCP project with GKE + Artifact Registry
- GitHub Actions secrets:
  - `GCP_SA_KEY`
  - `GCP_PROJECT`
  - `GKE_CLUSTER`
  - `GKE_ZONE`
  - `SONAR_TOKEN`

---

## Author

**Yağmur Göktaş**  
Term Project for **CMPE 58E - Cloud & Edge Computing Security**  
Boğaziçi University, 2025

---