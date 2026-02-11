pipeline {
    agent any 
    stages {
	stage('clean Workspace') {
		steps {
			cleanWs()
		}
	}

        stage('checkout scm') {
            steps {
                git url: 'https://github.com/MohitGupta1010/Project-1.git', branch: 'master'
            }
        }

        stage('Execute docker compose'){
            steps {
                sh '''
		withCredentials([usernamePassword(credentialsId: 'docker login', passwordVariable: 'PASS', usernameVariable: 'USER')]){
                 cd $WORKSPACE/
                 echo $PASS | docker login -u $USER --password-stdin
                 docker compose down || true
                 docker compose up -d --build
                '''
		}
            }
        }
    }
}
