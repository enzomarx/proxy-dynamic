# Dynamic Proxy with Python

This project implements a dynamic proxy using Python, Docker, and Nginx. The proxy can route requests between different servers and ports. Includes a web interface for managing and configuring rules.

## Features
- Dynamic routing of requests
- Web management interface
- Loggin and monitoring
- HTTPS support
- Access control

### Use Cases

1. Local Development: Use Docker to create an isolated, replicable development environment.
2. Production Deployment: Use Docker and Nginx for a robust and scalable solution for traffic forwarding.
3. **Simplified Management**: The web interface allows for easy configuration and monitoring of routing rules.

### Future Improvements

- Security: Add security settings in Nginx and HTTPS support.
- Monitoring: Integrate monitoring and alerting tools.
- Scalability: Configure multiple instances of the 'proxy_server' for increased capacity.

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/usuario/proxy-dinamico.git

2. Navigate to the project directory:
````
cd proxy-dinamico
````
3.Build and launch containers using Docker Compose:
````
docker-compose up --build
````

## Execution
Access the web interface in http://127.0.0.1:5000 to manage routing rules.

Nginx will act as a reverse proxy on port 80 and forward the requests to the dynamic proxy on port 8000.
