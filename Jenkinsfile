// Jenkinsfile
pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                // Pull code from your Git repository
                git 'https://github.com/your-username/my-python-app.git'
            }
        }

        stage('Build') {
            steps {
                script {
                    // Build Docker image
                    sh 'docker build -t my-python-app .'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Run unit tests (if any are available)
                    sh 'python -m unittest discover -s src/tests'
                }
            }
        }

        stage('Deploy to Container') {
            steps {
                deploy adapters: [
                    tomcat9(credentialsId: 'your-credentials-id', 
                            path: '', 
                            url: 'http://localhost:8081/')
                ],
                contextPath: 'my-python-app',
                war: 'target/my-python-app.war'
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'target/*.war', allowEmptyArchive: true
            junit 'target/test-results/*.xml'
        }
        success {
            echo 'Deployment successful!'
        }
        failure {
            echo 'Deployment failed!'
        }
    }
}
