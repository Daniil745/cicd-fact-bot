# CI/CD Pipeline for Fact Bot

<div align="center">

[![Jenkins](https://img.shields.io/badge/Jenkins-CI%2FCD-D24939?style=for-the-badge&logo=jenkins&logoColor=white)](https://www.jenkins.io/)
[![Docker](https://img.shields.io/badge/Docker-24.x-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Ubuntu](https://img.shields.io/badge/Ubuntu-22.04_LTS-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)](https://ubuntu.com/)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)
[![Telegram](https://img.shields.io/badge/Telegram-Notifications-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)](https://telegram.org/)
[![Docker Hub](https://img.shields.io/badge/Docker_Hub-Registry-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://hub.docker.com/)

<h3>CI/CD Pipeline for Fact Bot - Automated deployment with health checking and rollback capabilities</h3>
Report Bug · Request Feature

</div>

## Overview

![image alt](https://github.com/Daniil745/cicd-fact-bot/blob/4e418fa5287a0d1a536000352638ce032970db18/screenshots/uml-diagramm.png)

This project demonstrates a complete CI/CD pipeline for a microservice (Flask fact bot) with automated deployment, health checking, and rollback capabilities.

## Architecture

```
[User] -> [GitHub] -> [Jenkins] -> [Docker Hub] -> [Target Server]
                                              |
                                              v
                                       [Telegram Bot]
```

## Components

| Component | Technology | Purpose |
|-----------|------------|---------|
| Application | Python + Flask | REST API with /health endpoint |
| Containerization | Docker | Multi-stage build |
| CI/CD Server | Jenkins | Pipeline orchestration |
| Container Registry | Docker Hub | Image storage |
| Target Server | Ubuntu + Docker | Production environment |
| Notifications | Telegram API | Deployment status alerts |

## Features

- Automated Docker image build on git push
- Multi-stage Dockerfile for optimized image size
- Push to Docker Hub registry
- SSH-based deployment to remote server
- Healthcheck endpoint with automated rollback
- Telegram notifications for build status
- Poll SCM trigger (no public webhook required)

## Pipeline Stages

1. Checkout - Clone repository from GitHub
2. Build - Create Docker image with version tag
3. Push - Upload image to Docker Hub
4. Deploy - Pull and run container on target server
5. Healthcheck - Verify service is responding

## Quick Start

### Prerequisites

- Two Ubuntu servers (or VMs) with Docker installed
- Jenkins server with Docker and Git plugins
- Docker Hub account
- Telegram bot token and chat ID

### Environment Setup

```bash
# Clone repository
git clone https://github.com/Daniil745/cicd-fact-bot.git
cd cicd-fact-bot

# Build and test locally
cd app
docker build -t fact-bot:test .
docker run -d -p 5000:5000 fact-bot:test
curl http://localhost:5000/health
```

### Jenkins Configuration

1. Create new Pipeline job
2. Set SCM to Git with repository URL
3. Set Script Path to Jenkinsfile
4. Configure credentials:
   - Docker Hub (username/password)
   - Target server SSH key
   - Telegram bot token
   - Telegram chat ID
5. Enable Poll SCM with schedule: `* * * * *` (Since ngrok is not supported)

## API Endpoints

| Endpoint | Method | Response |
|----------|--------|----------|
| `/` | GET | Random fact about server |
| `/health` | GET | Service health status (200/500) |
| `/metrics` | GET | JSON with service metrics |

## Troubleshooting

| Issue | Solution |
|-------|----------|
| SSH connection failed | Regenerate RSA key with -m PEM format |
| Healthcheck timeout | Check BUG_MODE environment variable |
| Docker push failed | Verify Docker Hub credentials |
| Container not starting | Check logs: `docker logs fact-bot` |

## Future Improvements

- Add Ansible for infrastructure provisioning
- Integrate Prometheus + Grafana monitoring
- Deploy to Kubernetes cluster

Results screenshot in CMD:

---
![image alt](https://github.com/Daniil745/cicd-fact-bot/blob/4e418fa5287a0d1a536000352638ce032970db18/screenshots/cmd-results.png)
---

Telegram notifications:

---
![image alt](https://github.com/Daniil745/cicd-fact-bot/blob/4e418fa5287a0d1a536000352638ce032970db18/screenshots/notifications-tg.jpg)
---

Docker Hub screenshots:

---
![image alt](https://github.com/Daniil745/cicd-fact-bot/blob/4e418fa5287a0d1a536000352638ce032970db18/screenshots/dockerhub.png)
---

##  Author

**Daniil**
- GitHub: [@Daniil745](https://github.com/Daniil745)
- Project Link: [https://github.com/Daniil745/cicd-fact-bot](https://github.com/Daniil745/cicd-fact-bot)

##  License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">
  <sub>If you found this project helpful, please give it a star :)!</sub>
  <br>
  <sub>Built with ❤️ for the DevOps community</sub>
</div>
