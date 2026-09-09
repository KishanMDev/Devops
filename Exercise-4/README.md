# Exercise 4: Docker Networking with Multiple Containers

## Objective
Understand Docker networking fundamentals by isolating and connecting a multi-container stack (Flask Web Server, MySQL Database, and Redis Cache) over a custom bridge network (`my-bridge-net`). Containers on the same user-defined bridge network resolve each other by container name via embedded Docker DNS.

## Scenario & Services
- **Flask REST API**: Web layer listening on port 5001 (`/about` endpoint)
- **MySQL Container**: Relational database running on port 3306
- **Redis Container**: In-memory cache running on port 6379
- **Network**: Custom bridge network `my-bridge-net` with isolated subnet `172.18.0.0/16`

## Files Included
- `app.py`: Flask REST API code
- `requirements.txt`: Python package dependencies
- `Dockerfile`: Container image specification
- `docker-compose.yml`: Multi-container composition definition
- `screenshots/`: Execution proof captures

## Execution Steps
1. **Create Custom Bridge Network**:
   ```bash
   docker network create --driver bridge my-bridge-net
   ```
2. **Inspect Network Configuration**:
   ```bash
   docker network inspect my-bridge-net
   ```
3. **Build Flask API Image**:
   ```bash
   docker build -t flask-api .
   ```
4. **Launch Containers Attached to Network**:
   ```bash
   docker run -d --name mysql --net=my-bridge-net -e MYSQL_ROOT_PASSWORD=secret mysql:8.0
   docker run -d --name redis --net=my-bridge-net redis:alpine
   docker run -d --name flask --net=my-bridge-net -p 5001:5001 flask-api
   ```
5. **Test Cross-Container Connectivity (DNS & Ping)**:
   ```bash
   docker exec -it flask ping -c 3 mysql
   docker exec -it flask ping -c 3 redis
   curl http://localhost:5001/about
   ```

## Q&A Summary
- **Purpose of `--net` flag**: Connects container network namespace to a specific Docker bridge or overlay network.
- **Inter-container communication**: Built-in Docker DNS resolves container names directly to their bridge IP addresses.
- **Bridge vs Host Network**: A bridge provides an isolated virtual subnet with port mapping, while host mode binds the container directly to the host's network interfaces.

## Execution Proof (Screenshots)
- `screenshots/01-create-and-inspect-bridge-network.png`: Network creation and subnet details
- `screenshots/02-docker-build-flask-api.png`: Flask API image build log
- `screenshots/03-launch-containers-on-network.png`: Running containers attached to `my-bridge-net`
- `screenshots/04-container-connectivity-ping-proof.png`: Ping verification and curl API response
