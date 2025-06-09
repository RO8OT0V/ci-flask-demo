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
                docker-compose down || true
                docker image prune -f
                '''
            }
        }

        stage('Build and Deploy') {
            steps {
                sh 'docker-compose up --build -d'
            }
        }
	stage('Show logs') {
    	    steps {
        	sh 'docker-compose logs --tail=30'
    	    }
	}
    }
}

