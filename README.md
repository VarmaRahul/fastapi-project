# 🚀 Ultimate FastAPI GitOps Platform

A production-grade FastAPI application demonstrating **Senior DevOps and SRE principles**. This project features a high-performance modular architecture, multi-container orchestration, and a **"Shift-Left" DevSecOps pipeline**.

## 🛠️ Tech Stack & Tools
* **Backend:** FastAPI (Python 3.12+), Pydantic v2
* **Security:** JWT (Stateless Auth), `passlib` + `bcrypt`
* **Database:** PostgreSQL 16 (SQLAlchemy ORM)
* **Containerization:** Docker (Multi-stage builds) & Docker Compose
* **DevSecOps:** Gitleaks, Hadolint, CodeQL, Trivy, `pip-audit`
* **Observability:** Structured Logging, Health & Readiness Probes

## 🛡️ DevSecOps Pipeline (CI/CD)
The project utilizes GitHub Actions to enforce a strict security and quality gate before any image is pushed to Docker Hub:
1.  **Linting:** Python (Ruff) & Dockerfile (Hadolint).
2.  **Security Scans:** * **Gitleaks:** Detects hardcoded secrets in Git history.
    * **CodeQL (SAST):** Static analysis for code vulnerabilities.
    * **pip-audit:** Scans dependencies for known CVEs.
3.  **Functional Testing:** Pytest running against a PostgreSQL sidecar service.
4.  **Container Audit:** **Trivy** scans the final image for OS-level vulnerabilities.
5.  **Distribution:** Automated push to Docker Hub upon successful validation.

## 📁 Project Structure
```text
├── .github/workflows/      # DevSecOps Pipeline (ci.yml)
├── app/
│   ├── main.py            # App entry point & Lifespan handlers
│   ├── database.py        # Connection pooling & Session logic
│   ├── config.py          # Pydantic Settings (Env validation)
│   ├── oauth2.py          # JWT authentication middleware
│   ├── models/            # SQLAlchemy Models (Users, Orders)
│   ├── router/            # Modular API routes (Auth, Users, Orders)
│   └── schemas/           # Pydantic Request/Response schemas
├── tests/                 # Pytest suite
├── Dockerfile             # Multi-stage optimized & linted build
├── docker-compose.yml     # Orchestration with resource limits
└── .env                   # Environment secrets (Git-ignored)
```

## ⚙️ Local Development
**1. Environment Configuration**
Create a .env file (see .env.example for reference):

```text
DB_USER=rahul_admin
DB_PASSWORD=securepassword
DB_NAME=ultimate_platform
SECRET_KEY=your_64_bit_secret
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

**2. Run with Docker Compose**
```bash
docker compose up -d --build
```

### API: http://localhost:8000
### Swagger Docs: http://localhost:8000/docs
### Health Checks: /health (Liveness) & /ready (Readiness)

## 📈 Project Roadmap
### [x] Phase 1: Project Initialization & Modular Routing.
### [x] Phase 2: Database Integration (PostgreSQL & SQLAlchemy).
### [x] Phase 3: Containerization (Docker, Compose & Resource Limits).
### [x] Phase 4: DevSecOps & CI (Pytest, CodeQL, Trivy, Docker Hub).
### [ ] Phase 5: Kubernetes Fundamentals (Deployment, Services, Ingress).
### [ ] Phase 6: Infrastructure as Code (Terraform for AWS/EKS).
### [ ] Phase 7: GitOps & Continuous Deployment (ArgoCD/Helm).
### [ ] Phase 8: Monitoring & SRE (Prometheus/Grafana).