pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ai-devops-log-analyzer .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh 'docker stop ai-container || true'
                sh 'docker rm ai-container || true'
                sh 'docker run -d -p 5000:5000 --name ai-container ai-devops-log-analyzer'
            }
        }
    }
}