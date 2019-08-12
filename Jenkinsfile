pipeline {
    agent { dockerfile true }
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
