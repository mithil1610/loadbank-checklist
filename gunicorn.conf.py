# gunicorn.conf.py
import multiprocessing

# Timeout settings
timeout = 120  # Increased from default 30s
graceful_timeout = 120
keepalive = 5

# Worker settings
workers = 2
worker_class = 'sync'
worker_connections = 1000
max_requests = 1000
max_requests_jitter = 50

# Logging
accesslog = '-'
errorlog = '-'
loglevel = 'info'

# Preload app for faster worker startup
preload_app = True
