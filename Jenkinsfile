pipeline{
    agent any
    
    stages{
      stage('build'){
            steps{
                sh '''
                echo "this is my first pipeline....."
                uptime
                date
                '''
            }
      }
            stage('build1'){
                steps{
                sh '''
                echo "this is my 2nd  pipeline....."
                uptime
                date
                '''
            }
        }
         stage('build2'){
                steps{
                sh '''
                echo "this is my3nd  pipeline....."
                uptime
                date
                '''
            }
    }
}
}
