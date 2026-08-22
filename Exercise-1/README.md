# Exercise 1: Kubernetes Getting Started (Hello Pod)

## Overview & Business Problem
Simulate deploying a lightweight storefront and delivery status web application (Zepto storefront simulation) on Kubernetes using the official `nginx` image. This hands-on lab introduces local Kubernetes cluster provisioning with Minikube, deploying standalone Pods, inspecting runtime states, exposing services via NodePort, and verifying external accessibility.

## Architecture
- **Cluster**: Minikube Single-Node Local Cluster (Docker driver)
- **Workload**: Pod `hello-k8s` running `nginx:latest` on port 80
- **Service**: NodePort service routing traffic from host node port to container port 80

## Files Included
- `hello-pod.yaml`: Kubernetes Pod declarative definition
- `hello-service.yaml`: Kubernetes Service NodePort definition
- `screenshots/`: Terminal execution proof captures

## Execution Steps
1. **Start Minikube**:
   ```bash
   minikube start --driver=docker
   ```
2. **Deploy Pod**:
   ```bash
   kubectl apply -f hello-pod.yaml
   # or
   kubectl run hello-k8s --image=nginx --port=80
   ```
3. **Verify Pod Status**:
   ```bash
   kubectl get pods -o wide
   ```
4. **Expose as NodePort Service**:
   ```bash
   kubectl apply -f hello-service.yaml
   # or
   kubectl expose pod hello-k8s --type=NodePort --port=80
   ```
5. **Access and Verify**:
   ```bash
   minikube service hello-k8s-service --url
   curl http://127.0.0.1:30080
   ```

## Execution Proof (Screenshots)
- `screenshots/01-minikube-start.png`: Cluster startup and node readiness
- `screenshots/02-pod-create-verify.png`: Pod creation and running status
- `screenshots/03-service-expose.png`: Service binding and NodePort allocation
- `screenshots/04-service-access-proof.png`: HTTP curl response returning Nginx welcome page
