# Self-Healing Service

A sandbox project for learning and demonstrating core DevOps concepts hands-on.

## What this covers
- **Containerization** — Dockerized Python service with health check endpoint
- **CI/CD** — Automated build and deploy pipeline via GitHub Actions
- **Cloud Deployment** — Hosted on GCP Cloud Run with auto-scaling
- **Observability** — `/health` endpoint exposing uptime and version info

## Stack
Python · Flask · Docker · GitHub Actions · GCP Cloud Run

## Endpoints
- `GET /` — Service info
- `GET /health` — Health status + uptime
