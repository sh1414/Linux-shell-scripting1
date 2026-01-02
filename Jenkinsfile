pipeline {
    agent any

    environment {
        IMAGE_NAME = "ks:${GIT_COMMIT}"
        CONTAINER_NAME = "ks_app"
    }

    stages {

        stage('Git Checkout') {
            steps {
                git url: 'https://github.com/sh1414/Linux-shell-scripting1.git',
                    branch: 'main'
            }
        }

        stage('Docker Build') {
            steps {
                sh '''
                docker build -t ${IMAGE_NAME} .
                '''
            }
        }
        stage('Run Container') {
            steps {
                sh '''
                docker run -d --name ${CONTAINER_NAME} -p 8080:8080 ${IMAGE_NAME}
                '''
            }
        }
    }
}
