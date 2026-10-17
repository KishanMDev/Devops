# Exercise 10: Multi-Node Kubernetes Cluster with Multiple Applications and ReplicaSets

## Objective & Storyboard
Build and deploy a distributed e-commerce architecture across a 3-node Kubernetes cluster (`devops-multinode`). The architecture consists of two microservices:
1. **Product Catalog (AppA)**: 2 replicas distributed across worker nodes.
2. **Shopping Cart (AppB)**: 3 replicas distributed across worker nodes.

Using Kubernetes `podAntiAffinity`, pods from each application are scheduled across distinct cluster nodes, providing high availability and zero downtime even if an entire node goes offline.

## Architecture
- **Cluster**: 3-Node Minikube Profile (`devops-multinode`, `devops-multinode-m02`, `devops-multinode-m03`)
- **Image Registry**: Minikube local registry addon on port 32775
- **High Availability**: Pod anti-affinity rules topology key `kubernetes.io/hostname`
- **Services**:
  - `product-catalog-service` on NodePort 30091
  - `shopping-cart-service` on NodePort 30092

## Files Included
- `product_catalog.py` & `Dockerfile.catalog`: Product Catalog microservice
- `shopping_cart.py` & `Dockerfile.cart`: Shopping Cart microservice
- `product-catalog-deployment.yaml`: Deployment & Service manifest with Pod Anti-Affinity
- `shopping-cart-deployment.yaml`: Deployment & Service manifest with Pod Anti-Affinity
- `screenshots/`: Execution proof captures

## Execution Steps
1. **Provision 3-Node Cluster**:
   ```bash
   minikube start --nodes 3 -p devops-multinode --force
   ```
2. **Enable Internal Container Registry**:
   ```bash
   minikube -p devops-multinode addons enable registry
   ```
3. **Build and Push Images to Local Registry**:
   ```bash
   docker build -t localhost:32775/product-catalog:latest -f Dockerfile.catalog .
   docker push localhost:32775/product-catalog:latest
   docker build -t localhost:32775/shopping-cart:latest -f Dockerfile.cart .
   docker push localhost:32775/shopping-cart:latest
   ```
4. **Deploy Microservices**:
   ```bash
   kubectl apply -f product-catalog-deployment.yaml
   kubectl apply -f shopping-cart-deployment.yaml
   ```
5. **Verify Pod Distribution Across All 3 Nodes**:
   ```bash
   kubectl get pods -o wide
   ```
6. **Test Microservice Endpoints**:
   ```bash
   curl http://127.0.0.1:30091/products
   curl http://127.0.0.1:30092/cart
   ```

## Execution Proof (Screenshots)
- `screenshots/01-multinode-cluster-start.png`: 3-node cluster startup and node readiness
- `screenshots/02-multinode-registry-addon.png`: Minikube registry addon activation
- `screenshots/03-multi-app-deployment-apply.png`: Deployment and service creation
- `screenshots/04-pods-distribution-across-nodes.png`: Verification that replicas are scheduled across m01, m02, and m03
- `screenshots/05-curl-endpoints-verification.png`: Functional validation of JSON responses
