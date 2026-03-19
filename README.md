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
├── .github/workflows/           # DevSecOps Pipeline (ci.yml)
├── .venv/                       # Python Virtual Environment
├── __pycache__/                 # Python Cache (Ignore)
├── app/                         # Core FastAPI Application
│   ├── __init__.py              # Package init
│   ├── __pycache__/             # App cache
│   ├── config.py                # Pydantic Settings
│   ├── database.py              # DB Connection pooling
│   ├── main.py                  # App entry point
│   ├── models/                  # SQLAlchemy Models
│   │   ├── __init__.py          # Package init
│   │   ├── __pycache__/         # Models cache
│   │   ├── models.py            # Base models
│   │   └── schemas.py           # Pydantic schemas
│   ├── oauth2.py                # JWT Auth middleware
│   ├── router/                  # API Routes
│   │   ├── __init__.py          # Package init
│   │   ├── __pycache__/         # Router cache
│   │   ├── auth.py              # Auth endpoints
│   │   ├── orders.py            # Orders endpoints
│   │   └── users.py             # Users endpoints
│   └── utils.py                 # Utility functions
├── tests/                       # Pytest suite
├── .env                         # Local environment secrets
├── .env.example                 # Env template
├── .git/                        # Git repository
├── .gitignore                   # Git ignore rules
├── docker-compose.yml           # Docker orchestration
├── Dockerfile                   # Multi-stage build
├── LICENSE                      # Project license
├── README.md                    # Documentation
└── requirements.txt             # Python dependencies

```

## ⚙️ Local Development
**1. Environment Configuration** <br>
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

**API: http://localhost:8000** <br>
**Swagger Docs: http://localhost:8000/docs** <br>
**Health Checks: /health (Liveness) & /ready (Readiness)** <br>

## 📈 Project Roadmap <br>
**[x] Phase 1: Project Initialization & Modular Routing.** <br>
**[x] Phase 2: Database Integration (PostgreSQL & SQLAlchemy).** <br>
**[x] Phase 3: Containerization (Docker, Compose & Resource Limits).** <br>
**[x] Phase 4: DevSecOps & CI (Pytest, CodeQL, Trivy, Docker Hub).** <br>
**[ ] Phase 5: Kubernetes Fundamentals (Deployment, Services, Ingress).** <br>
**[ ] Phase 6: Infrastructure as Code (Terraform for AWS/EKS).** <br>
**[ ] Phase 7: GitOps & Continuous Deployment (ArgoCD/Helm).** <br>
**[ ] Phase 8: Monitoring & SRE (Prometheus/Grafana).** <br>