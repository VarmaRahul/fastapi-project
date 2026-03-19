🚀 Ultimate FastAPI GitOps Platform
A production-grade FastAPI application designed to demonstrate Senior DevOps and SRE principles, including modular architecture, containerization, stateless authentication, and observability.

🛠️ Tech Stack & Tools
Backend: FastAPI (Python 3.12+), Pydantic v2

Security: JWT (Stateless Auth), Password Hashing (passlib + bcrypt)

Database: PostgreSQL 16 (Relational Mapping via SQLAlchemy)

Containerization: Docker & Docker Compose (Multi-container orchestration)

Observability: Health & Readiness Probes (SRE standard)

📁 Project Structure
Plaintext
├── app/
│   ├── main.py            # App entry point & Lifespan handlers
│   ├── database.py        # Connection pooling & Session logic
│   ├── config.py          # Pydantic Settings & Env validation
│   ├── oauth2.py          # JWT authentication middleware
│   ├── models/            
│   │   ├── models.py      # SQLAlchemy DB Models (Users, Orders)
│   │   └── schemas.py     # Pydantic Schemas (Request/Response)
│   └── router/            # Modular API routes
├── Dockerfile             # Multi-stage optimized build
├── docker-compose.yml     # Orchestration with resource limits
├── .env                   # Environment secrets (Git-ignored)
├── requirements.txt       # Frozen dependencies
└── README.md
⚙️ Local Development (The DevOps Way)
1. Environment Configuration
Create a .env file in the root directory:

Plaintext
DB_USER=rahul_admin
DB_PASSWORD=yourpassword
DB_NAME=ultimate_platform
SECRET_KEY=your_64_bit_secret
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
2. Run with Docker Compose (Recommended)
This launches the API and PostgreSQL in an isolated network with resource limits (CPU: 0.5, RAM: 256MB).

Bash
docker compose up -d --build
API: http://localhost:8000

Swagger Docs: http://localhost:8000/docs

Health Check: http://localhost:8000/health

3. Manual Setup (Virtual Env)
Bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
📡 Core API Endpoints
POST /users/ - Create a new user (hashed passwords).

POST /login - Returns JWT bearer token.

GET /users/me - Protected profile route.

POST /orders/ - Create a relational order (mapped to current user).

GET /health - Liveness probe.

GET /ready - Readiness probe (checks DB connectivity).

📈 Project Roadmap
[x] Phase 1: Project Initialization & Modular Routing.

[x] Phase 2: Database Integration (PostgreSQL & SQLAlchemy Relationships).

[x] Phase 3: Containerization (Docker, Docker Compose, & Healthchecks).

[ ] Phase 4: Testing & CI (Pytest & GitHub Actions).

[ ] Phase 5: Kubernetes Fundamentals (EKS Deployment).

[ ] Phase 6: Infrastructure as Code (Terraform for RDS/EKS).

[ ] Phase 7: GitOps & Deployment (ArgoCD/Helm).

[ ] Phase 8: Monitoring & SRE (Prometheus/Grafana).