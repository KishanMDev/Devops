# Exercise 3: Scaling Flask App on Single Node using ReplicaSets

## Real-Life Tech Use Case: E-Commerce Flash Sale
During a flash sale event on platforms like Flipkart or Amazon, baseline traffic spikes instantaneously from 100 requests/minute to tens of thousands. Running a single Pod causes severe resource exhaustion and system crashes. By leveraging Kubernetes ReplicaSets and Deployments, our application horizontally scales out from 1 to 5 or more identical worker Pods. Kubernetes distributes inbound traffic across all healthy Pod replicas. Once the spike subsides, the cluster scales back down.

## Architecture
- **Application**: Python 3.11 / Flask / Gunicorn production WSGI server
- **Endpoints**:
  - `/`: Storefront landing banner with serving pod hostname
  - `/buy`: Simulated checkout transaction assigning products and identifying serving replica
  - `/health`: Health and readiness probe
- **Horizontal Scaling**: Scaled from 1 replica to 5 replicas dynamically via `kubectl scale`

## Files Included
- `app.py`: Flash sale microservice
- `Dockerfile`: Production image build specification with Gunicorn
- `flask-sale-deployment.yaml`: Deployment & NodePort Service manifest
- `screenshots/`: Execution proof logs

## Execution Steps
1. **Build Container Image**:
   ```bash
   docker build -t flashsale:1.0 .
   ```
2. **Deploy Initial Single-Replica Workload**:
   ```bash
   kubectl apply -f flask-sale-deployment.yaml
   ```
3. **Scale Deployment to 5 Replicas**:
   ```bash
   kubectl scale deployment flash-sale-app --replicas=5
   ```
4. **Observe Pod Distribution and Status**:
   ```bash
   kubectl get pods -l app=flash-sale-app -o wide
   kubectl get replicasets
   ```
5. **Simulate Concurrent Flash Sale Purchases & Verify Load Balancing**:
   ```bash
   1..10 | ForEach-Object { curl.exe -s http://127.0.0.1:32000/buy }
   ```

## Execution Proof (Screenshots)
- `screenshots/01-initial-single-replica-deploy.png`: Initial 1-replica deployment running
- `screenshots/02-scaling-replicas-to-5.png`: Scaling command and replica count update
- `screenshots/03-verify-replica-distribution.png`: All 5 Pods healthy and active in ReplicaSet
- `screenshots/04-curl-load-distribution-proof.png`: Successive requests handled by distinct Pod hostnames
