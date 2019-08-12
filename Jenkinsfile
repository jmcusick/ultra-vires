pipeline {
    agent { dockerfile true 
            args '-u root:sudo'
          }
    stages {
        stage('build') {
            steps {
                sh """pwd
                hostname
                ls
                whoami"""
                sh 'pipenv run python3 -m pytest .'
            }
        }
    }
}
