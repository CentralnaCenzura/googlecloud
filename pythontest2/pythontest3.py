#test3
runtime: python
env: flex
entrypoint: gunicorn -b :$PORT main:app

runtime_config:
    operating_system: ubuntu22
    
manual_scaling:
    instances: 1
resources:
    cpu: 1
    memory_gb: 0.5
    disk_size_gb: 10