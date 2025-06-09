pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/RO8OT0V/ci-flask-demo'
            }
        }

        stage('Stop and Clean') {
            steps {
                sh '''
                docker stop flask-app || true
                docker rm flask-app || true
                docker image rm flask-app || true
                docker image prune -f
                '''
            }
        }

        stage('Build Image') {
            steps {
                sh 'docker build -t flask-app .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d --name flask-app -p 5000:5000 flask-app'
            }
        }
    }
}

