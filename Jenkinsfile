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
                dir("${WORKSPACE}") {
                    sh '''
                    echo "[CLEAN] Остановка и очистка"
                    docker-compose down -v || true
                    docker image prune -f || true
                    '''
                }
            }
        }

        stage('Build and Deploy') {
            steps {
                dir("${WORKSPACE}") {
                    sh '''
                    docker-compose down -v || true
                    docker-compose build --no-cache
                    docker-compose up -d
                    '''
                }
            }
        }

        stage('Show logs') {
            steps {
                dir("${WORKSPACE}") {
                    sh 'docker-compose logs --tail=30 || true'
                }
            }
        }
    }
}
