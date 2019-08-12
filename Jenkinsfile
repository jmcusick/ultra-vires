pipeline {
    agent { dockerfile true }
    stages {
        stage('build') {
            steps {
                sh 'whoami'
                sh 'hostname'
                sh 'ls'
                sh 'pwd'
                sh 'pipenv run python3 -m pytest .'
            }
        }
    }
}
