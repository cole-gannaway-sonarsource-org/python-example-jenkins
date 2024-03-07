pipeline {
  stages {
    stage('SCM') {
      steps {
        checkout scm
      }
    }
    stage('SonarQube Analysis') {
      steps {
        def scannerHome = tool 'sonar-scanner-cli';
        withSonarQubeEnv() {
          sh "${scannerHome}/bin/sonar-scanner"
        }
      }
    }
  }
}