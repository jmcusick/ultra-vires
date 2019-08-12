pipeline {
    agent { dockerfile true }
    stages {
        stage('build') {
            steps {
                sh """pwd
                whoami
                hostname
                ls"""
                sh 'pipenv run python3 -m pytest .'
            }
        }
    }
}
