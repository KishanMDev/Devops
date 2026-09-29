# Exercise 7: Introduction to CI/CD and Jenkins Installation

## Continuous Integration (CI) Overview
Continuous Integration is an industry-standard software engineering practice where developers frequently merge code commits into a central repository. Automated build, static analysis, and automated test suites execute on every push, catching bugs early, improving developer velocity, and maintaining pristine code quality.

## Jenkins Setup & Containerization
Jenkins is an open-source automation server supporting hundreds of plugins for building, testing, and deploying containerized applications. In this exercise, Jenkins LTS is installed and orchestrated using Docker with named persistent volume storage (`jenkins_home`).

## Architecture & Ports
- **Jenkins Controller Container**: `jenkins/jenkins:lts`
- **Web UI & REST API Port**: `8080`
- **Inbound Agent Listener Port (JNLP)**: `50000`
- **Persistent Storage**: Docker named volume `jenkins_home` mounted to `/var/jenkins_home`

## Files Included
- `docker-compose.yml`: Declarative compose file for Jenkins
- `run-jenkins.sh`: Quick start shell utility
- `screenshots/`: Execution proof captures

## Execution Steps
1. **Pull and Launch Jenkins Container**:
   ```bash
   docker run -d --name jenkins -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts
   ```
2. **Inspect Container Status**:
   ```bash
   docker ps -f name=jenkins
   ```
3. **Retrieve Initial Administrator Password**:
   ```bash
   docker exec -it jenkins cat /var/jenkins_home/secrets/initialAdminPassword
   ```
4. **Access Jenkins Web Interface**:
   Open browser at `http://localhost:8080` to complete plugin setup and unlock Jenkins.

## Execution Proof (Screenshots)
- `screenshots/01-jenkins-docker-run.png`: Container pull, startup, and port mapping
- `screenshots/02-jenkins-admin-password.png`: Extraction of secure initial administrator password
- `screenshots/03-jenkins-dashboard-ready.png`: HTTP 200 health check and active Jenkins controller
