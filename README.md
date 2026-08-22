# DevOps Laboratory Exercises Portfolio

**Author**: Kishan M Dev  
**Email**: kishankeerthidev@gmail.com  
**Repository**: [https://github.com/KishanMDev/Devops.git](https://github.com/KishanMDev/Devops.git)

---

## Overview

This repository contains the complete implementation, configuration manifests, source code, and verified terminal execution proofs for all 10 DevOps Laboratory exercises. Each exercise is structured in its own self-contained directory containing implementation code, declarative configuration files, architecture documentation, and execution proof screenshots.

---

## Exercises Index

| Exercise | Module / Topic | Core Technologies | Primary Artifacts & Manifests | Proof of Execution |
| :--- | :--- | :--- | :--- | :--- |
| [**Exercise-1**](./Exercise-1) | Kubernetes Getting Started (Hello Pod) | Kubernetes, Minikube, Nginx | `hello-pod.yaml`, `hello-service.yaml` | `screenshots/` (Pod run, NodePort, Curl) |
| [**Exercise-2**](./Exercise-2) | Containerized Flask Deployment on Minikube | Docker, Python Flask, Kubectl | `app.py`, `Dockerfile`, `flask-deployment.yaml` | `screenshots/` (Build, Deploy, Logs, Curl) |
| [**Exercise-3**](./Exercise-3) | Horizontal Scaling with ReplicaSets (Flash Sale) | Kubernetes, ReplicaSets, Gunicorn | `app.py`, `Dockerfile`, `flask-sale-deployment.yaml` | `screenshots/` (Scaling to 5, Load Balancing) |
| [**Exercise-4**](./Exercise-4) | Docker Multi-Container Bridge Networking | Docker Engine, MySQL, Redis, Flask | `app.py`, `Dockerfile`, `docker-compose.yml` | `screenshots/` (Bridge net, DNS Ping, API) |
| [**Exercise-5**](./Exercise-5) | Docker Security Hardening with AppArmor | Linux Security, AppArmor MAC, Docker | `docker-profile-secure`, `test_security.py` | `screenshots/` (Profile parse, Security tests) |
| [**Exercise-6**](./Exercise-6) | Real-Time Telemetry & Alerting | Python, Prometheus, Grafana | `delivery_metrics.py`, `prometheus.yml`, `alerts_rules.yml` | `screenshots/` (Metrics stream, Alerts, UI) |
| [**Exercise-7**](./Exercise-7) | Continuous Integration Server Setup | Jenkins LTS, Docker, Named Volumes | `docker-compose.yml`, `run-jenkins.sh` | `screenshots/` (Deploy, Admin password, UI) |
| [**Exercise-8**](./Exercise-8) | Jenkins Hello World Pipeline Job | Jenkins Declarative Pipeline, Bash, Git | `hello-world.sh`, `Jenkinsfile` | `screenshots/` (Git commit, Pipeline, Console) |
| [**Exercise-9**](./Exercise-9) | Multi-Stage CI/CD Pipeline (Build, Test, Deploy) | Jenkins, Python `unittest`, Mock Staging | `app.py`, `test_app.py`, `Jenkinsfile` | `screenshots/` (Unit tests, Stage View, Logs) |
| [**Exercise-10**](./Exercise-10) | Multi-Node Multi-App Distributed Cluster | Minikube 3-Node, Microservices, Affinity | `product_catalog.py`, `shopping_cart.py`, YAMLs | `screenshots/` (3-node, Anti-Affinity, Endpoints) |

---

## Repository Structure

```text
Devops/
├── README.md                                  # Repository overview and master index
├── Exercise-1/                                # Kubernetes Getting Started (Hello Pod)
│   ├── hello-pod.yaml
│   ├── hello-service.yaml
│   ├── README.md
│   └── screenshots/
├── Exercise-2/                                # Minikube Kubectl Flask App
│   ├── app.py
│   ├── Dockerfile
│   ├── flask-deployment.yaml
│   ├── README.md
│   └── screenshots/
├── Exercise-3/                                # Scaling with ReplicaSets (Flash Sale)
│   ├── app.py
│   ├── Dockerfile
│   ├── flask-sale-deployment.yaml
│   ├── README.md
│   └── screenshots/
├── Exercise-4/                                # Docker Networking
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── README.md
│   └── screenshots/
├── Exercise-5/                                # Docker Security with AppArmor
│   ├── app.py
│   ├── Dockerfile
│   ├── docker-profile-secure
│   ├── test_security.py
│   ├── README.md
│   └── screenshots/
├── Exercise-6/                                # Prometheus & Grafana Monitoring
│   ├── delivery_monitoring/
│   │   ├── delivery_metrics.py
│   │   ├── prometheus.yml
│   │   ├── alerts_rules.yml
│   │   └── Jenkinsfile
│   ├── docker-compose.yml
│   ├── README.md
│   └── screenshots/
├── Exercise-7/                                # Jenkins CI Server Installation
│   ├── docker-compose.yml
│   ├── run-jenkins.sh
│   ├── README.md
│   └── screenshots/
├── Exercise-8/                                # Jenkins Hello World Job
│   ├── hello-world.sh
│   ├── Jenkinsfile
│   ├── README.md
│   └── screenshots/
├── Exercise-9/                                # Jenkins Multi-Stage Pipeline
│   ├── app.py
│   ├── requirements.txt
│   ├── test_app.py
│   ├── Jenkinsfile
│   ├── README.md
│   └── screenshots/
└── Exercise-10/                               # Multi-Node Multi-App Deployment
    ├── product_catalog.py
    ├── shopping_cart.py
    ├── Dockerfile.catalog
    ├── Dockerfile.cart
    ├── product-catalog-deployment.yaml
    ├── shopping-cart-deployment.yaml
    ├── README.md
    └── screenshots/
```

---

## Verification & Execution Proof

Each individual exercise folder contains an enclosed `screenshots/` directory showcasing terminal logs, container statuses, pod scheduling distributions, and curl endpoint tests providing end-to-end verification of successful execution.
