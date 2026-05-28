pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/Abhinavsingh6557/ai-devops-log-analyzer.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t ai-devops-log-analyzer .'
            }
        }

        stage('Run Docker Container') {
            steps {
                bat 'docker stop ai-container || exit 0'
                bat 'docker rm ai-container || exit 0'
                bat 'docker run -d -p 5000:5000 --name ai-container ai-devops-log-analyzer'
            }
        }
    }
}