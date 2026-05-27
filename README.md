# AI-Powered DevOps Log Analyzer

## Project Overview
This is a beginner-level DevOps project built using Flask and Docker.  
The application simulates AI-based log analysis for DevOps environments.

It analyzes infrastructure logs and provides:
- Issue explanation
- Possible cause
- Suggested fix

---

## Technologies Used
- Python
- Flask
- Docker
- Git
- GitHub

---

## Features
- Random DevOps log generation
- Automated troubleshooting suggestions
- Flask web application
- Docker container support

---

## Docker Commands

### Build Docker Image
```bash
docker build -t ai-devops-log-analyzer .
```

### Run Docker Container
```bash
docker run -p 5000:5000 ai-devops-log-analyzer
```

---

## Project Structure

ai-devops-log-analyzer/
│
├── app.py
├── Dockerfile
├── requirements.txt
├── templates/
│   └── index.html
└── README.md

---

## Future Improvements
- Jenkins CI/CD integration
- Kubernetes deployment
- Monitoring dashboard
- Real AI API integration

---

## Author
Abhinav Singh