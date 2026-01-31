pipeline {
    agent any 
    stages {

        stage('checkout scm') {
            steps {
                git url: 'https://github.com/MohitGupta1010/Project-1.git', branch: 'master'
            }
        }
        stage('Execute docker compose'){
            steps {
		withCredentials([string(credentialsId: 'password', variable: 'pass')]) {
                sh '''
                 cd $WORKSPACE/code
                 echo $pass | docker login -u mg25436@gmail.com --password-stdin
                 docker compose down || true
                 docker compose up -d --build
                '''
		}
            }
        }
    }
}
