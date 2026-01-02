pipeline {
    agent any

    environment {
        IMAGE_NAME = "ks:${GIT_COMMIT}"
        CONTAINER_NAME = "ks_app"
        APP_PORT = "8081"
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

        stage('Stop Old Container') {
            steps {
                sh '''
                docker stop ${CONTAINER_NAME} || true
                docker rm ${CONTAINER_NAME} || true
                '''
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker run -d \
                --name ${CONTAINER_NAME} \
                -p ${APP_PORT}:8080 \
                ${IMAGE_NAME}
                '''
            }
        }
    }
}
