# Exercise 6: Real-Time Operations Monitoring and Alerting with Prometheus & Grafana

## Objective
Design and implement an end-to-end real-time observability pipeline for a quick-commerce fast delivery service (ZAPPTTO). The solution utilizes Python Prometheus client to generate custom application telemetry, Prometheus to scrape and evaluate alerting thresholds, and Grafana to visualize metrics on dynamic dashboards.

## Architecture
- **Metrics Generator**: Python script exposing `total_deliveries`, `pending_deliveries`, `on_the_way_deliveries`, and `average_delivery_time` via Prometheus HTTP endpoint on port 8000.
- **Metrics Scraper**: Prometheus server scraping target every 5 seconds.
- **Alerting Engine**: Configured rule `HighPendingDeliveries` evaluating `pending_deliveries > 15`.
- **Visualization**: Grafana dashboard showing live gauges, timeseries graphs, and alert states.

## Files Included
- `delivery_monitoring/delivery_metrics.py`: Metrics generator and HTTP server
- `delivery_monitoring/prometheus.yml`: Prometheus scrape config
- `delivery_monitoring/alerts_rules.yml`: Prometheus alert rules
- `delivery_monitoring/Jenkinsfile`: Pipeline automation script
- `docker-compose.yml`: Prometheus and Grafana stack definition
- `screenshots/`: Execution logs and dashboard captures

## Execution Steps
1. **Install Prometheus Client**:
   ```bash
   pip install prometheus-client
   ```
2. **Start Delivery Metrics Simulation**:
   ```bash
   python delivery_monitoring/delivery_metrics.py
   ```
3. **Verify Metrics Endpoint**:
   ```bash
   curl http://localhost:8000/metrics
   ```
4. **Launch Prometheus & Grafana**:
   ```bash
   docker-compose up -d
   ```
5. **Access Observability UIs**:
   - Prometheus Targets & Alerts: `http://localhost:9090`
   - Grafana Dashboards: `http://localhost:3000`

## Execution Proof (Screenshots)
- `screenshots/01-python-metrics-simulation.png`: Live telemetry simulation output
- `screenshots/02-prometheus-metrics-endpoint.png`: Raw Prometheus metrics exposition
- `screenshots/03-prometheus-targets-and-alerts.png`: Healthy scrape targets and alert evaluation
- `screenshots/04-grafana-realtime-dashboard.png`: Real-time operational dashboard visualization
