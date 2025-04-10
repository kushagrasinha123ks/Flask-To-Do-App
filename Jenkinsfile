pipeline {
    agent any

    environment {
        IMAGE_NAME = "2002kush19/jenkins-flask-to-do"
        DOCKERHUB_CREDENTIALS = "dockerhub"
    }

    stages {
        stage('Clone Repo') {
            steps {
                echo "Cloning repository..."
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    def tag = "v${BUILD_NUMBER}"
                    sh "docker build -t $IMAGE_NAME:$tag ."
                    sh "docker tag $IMAGE_NAME:$tag $IMAGE_NAME:latest"
                }
            }
        }

        stage('Login to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', "${DOCKERHUB_CREDENTIALS}") {
                        echo "Logged in to DockerHub"
                    }
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    def tag = "v${BUILD_NUMBER}"
                    sh "docker push $IMAGE_NAME:$tag"
                    sh "docker push $IMAGE_NAME:latest"
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    sh "docker rm -f flask-todo || true"
                    sh "docker run -d -p 5000:5000 --name flask-todo $IMAGE_NAME:latest"
                }
            }
        }
    }
}
