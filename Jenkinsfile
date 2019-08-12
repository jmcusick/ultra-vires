pipeline {
    agent { 
        dockerfile {
            args '-u root:sudo'
        }
    }
    stages {
        stage('build') {
            steps {
                sh """pwd
                hostname
                ls
                whoami
                env"""
                sh 'pipenv run python3 -m pytest .'
            }
        }
    }
}
