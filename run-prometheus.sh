# Create prometheus config file
mkdir -p ~/prometheus-config
cat > ~/prometheus-config/prometheus.yml << EOL
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'flask-app'
    static_configs:
      - targets: ['flask-app:5000']
EOL

# Run Prometheus in a separate container connected to the same network
docker run -d \
  --name prometheus \
  --network app-monitoring \
  -p 8101:9090 \
  -v ~/prometheus-config/prometheus.yml:/etc/prometheus/prometheus.yml \
  prom/prometheus
