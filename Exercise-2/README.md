# Exercise 2: Deploy Flask App on Minikube using Kubectl and YAML

## Objective
Containerize a custom Python Flask web server and deploy it onto a local Kubernetes cluster using declarative YAML manifests. This exercise explores container builds directly within Minikube's Docker daemon, configuring `imagePullPolicy: Never` for local images, setting up Service port mappings (`port`, `targetPort`, `nodePort`), and accessing the service.

## Architecture
- **Language/Framework**: Python 3.8 / Flask
- **Application Port**: 15000
- **Container Registry Policy**: `imagePullPolicy: Never` (utilizes locally cached build)
- **Kubernetes Resources**:
  - `Deployment`: `flask-app` managing 1 replica
  - `Service`: `flask-app-service` exposing Port 15000 mapped to Container TargetPort 15000 and NodePort 31500

## Files Included
- `app.py`: Flask application source code
- `Dockerfile`: Multi-stage Docker container specification
- `flask-deployment.yaml`: Combined Deployment and NodePort Service manifest
- `screenshots/`: Execution logs and terminal proofs

## Execution Steps
1. **Configure Docker environment to Minikube daemon**:
   ```bash
   & minikube -p minikube docker-env --shell powershell | Invoke-Expression
   ```
2. **Build Docker Image**:
   ```bash
   docker build -t flask-app:latest .
   ```
3. **Deploy Application Manifest**:
   ```bash
   kubectl apply -f flask-deployment.yaml
   ```
4. **Inspect Deployment, Pods, and Logs**:
   ```bash
   kubectl get deployments
   kubectl get pods -l app=flask-app
   kubectl logs -l app=flask-app
   ```
5. **Verify Endpoint Accessibility**:
   ```bash
   minikube service flask-app-service --url
   curl http://127.0.0.1:31500
   ```

## Q&A Summary
- **Why `imagePullPolicy: Never`?** Prevents Kubernetes from querying DockerHub/remote registries for an image built strictly on the local daemon.
- **Port vs TargetPort**: `port` is the service's internal cluster port, while `targetPort` corresponds to the actual port where the containerized Flask app listens (15000).
- **Service Type NodePort**: Exposes the service on each node's IP at a static port.

## Execution Proof (Screenshots)
- `screenshots/01-docker-build-image.png`: Docker image build log
- `screenshots/02-kubectl-apply-deployment.png`: Deployment and service creation
- `screenshots/03-verify-deployment-and-pods.png`: Deployment status, running pods, and logs
- `screenshots/04-service-curl-verification.png`: Successful HTTP curl verification
