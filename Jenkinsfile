pipeline
{
    agent any
    environment
    {
        IMAGES_NAME='ks:$(GIT-COMMIT)'
    }
    stages
    {
    stage('git-checkout')
    {
        steps
        {
            git url: 'https://github.com/sh1414/Linux-shell-scripting1.git', branch: 'main'
        }
    }
    stage('build-stage')
    {
        steps
        {
            sh '''
            docker build -t $(IMAGES_NAME) .
            '''
        }
    }
    stage('run-stage')
    {
        steps{
            sh '''
            docker run -it -d -p 8080:8080 $(IMAGES_NAME)
            '''
        }
    }
}
}
