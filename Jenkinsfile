pipeline {
    agent { dockerfile true }
    stages {
        stage('build') {
            steps {
                sh 'pipenv run python3 -m pytest .'
            }
        }
    }
}
