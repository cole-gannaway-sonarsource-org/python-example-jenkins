pipeline {
    agent any
    stages {
        stage('SCM') {
            scm checkout
        }
        stage('Build') {
            steps {
                echo 'Hello, World!'
            }
        }
    }
}