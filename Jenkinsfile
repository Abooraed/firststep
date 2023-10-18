pipeline {
    agent any

    stages {
        stage('Build and Push Docker Image') {
            steps {
                script {
                    // Construire l'image Docker
                    sh 'docker build -t mslimane78/insert.py:tag .'

                    // Connexion à Docker Hub
                    sh 'docker login -u mslimane78 -p Raedsalah_08'

                    // Poussez l'image vers Docker Hub
                    sh 'docker push mslimane78/insert.py:tag'
                }
            }
        }
    }
}