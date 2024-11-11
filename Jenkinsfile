pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                // Pull code from your Git repository
                git branch: 'main', url: 'https://github.com/simranmehta26/DevOps-8.git'
            }
        }

        stage('Build') {
            steps {
                script {
                    bat 'docker --version' // Check if Docker is accessible
                    bat 'docker build -t mera-python-app .' // Build Docker image
                }
            }
        }

        stage('Deploy to Container') {
            steps {
                script {
                    // Deploy Docker container to your environment
                    bat 'docker run -d -p 5000:5000 mera-python-app'  // Adjust as necessary
                }
            }
        }
    }

    post {
        always {
            // Adjust artifact archiving to something relevant (e.g., logs, build output)
            archiveArtifacts artifacts: '**/*.log', allowEmptyArchive: true  // Archive logs or other relevant files
            
        }
        success {
            echo 'Deployment successful!'
        }
        failure {
            echo 'Deployment failed!'
        }
    }
}
