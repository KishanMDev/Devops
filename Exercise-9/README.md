# Exercise 9: Jenkins Multi-Stage CI/CD Pipeline (Build, Test, Deploy)

## Objective
Implement and automate a complete **Multi-Stage CI/CD Pipeline** using Jenkins for a Python Flask application. The declarative pipeline enforces rigorous automated quality gates divided across three sequential lifecycle stages:
1. **Build Stage**: Sets up runtime dependencies from `requirements.txt`.
2. **Test Stage**: Executes automated unit testing (`test_app.py` via `unittest`) to validate application routes and response payloads.
3. **Deploy Stage**: Automates staging/production artifact release upon passing all test suites.

## Architecture
- **Web Framework**: Python Flask
- **Test Framework**: Python Standard Library `unittest`
- **CI/CD Controller**: Jenkins Declarative Pipeline
- **Quality Gate**: Test failure immediately halts progression to Deploy stage.

## Files Included
- `app.py`: Flask application source code
- `requirements.txt`: Package dependency manifest
- `test_app.py`: Automated unit test suite
- `Jenkinsfile`: Declarative 3-stage pipeline script
- `screenshots/`: Execution proof captures

## Execution Steps
1. **Run Unit Tests Locally**:
   ```bash
   python -m unittest test_app.py -v
   ```
2. **Verify Declarative Jenkinsfile**:
   Inspect stage declarations for Build, Test, and Deploy.
3. **Trigger Pipeline Execution in Jenkins**:
   Execute build job and monitor progress across stages.
4. **Verify Deployment Artifacts**:
   Inspect deployed target directory `/opt/deploy/python-flask-app`.

## Execution Proof (Screenshots)
- `screenshots/01-local-unit-tests-pass.png`: Execution of `unittest` suite returning `OK`
- `screenshots/02-jenkinsfile-pipeline-definition.png`: Pipeline script with Build, Test, Deploy stages
- `screenshots/03-jenkins-multistage-build-logs.png`: Jenkins console output executing all stages
- `screenshots/04-jenkins-stage-view-success.png`: Stage view dashboard showing all stages passed
