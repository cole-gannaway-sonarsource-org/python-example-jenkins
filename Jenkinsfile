pipeline {
  agent any
  stages {
    stage('SCM') {
      steps {
        checkout scm
      }
    }
    stage('SonarQube Analysis') {
      steps {
        def mvn = tool 'mvn'
        withSonarQubeEnv() {
          sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=cole-gannaway-sonarsource-org_python-example-jenkins_AY4awoK1E5YwdsA4sndN"
        }
      }
    }
    stage("Quality Gate") {
      steps {
        timeout(time: 1, unit: 'HOURS') {
          // Parameter indicates whether to set pipeline to UNSTABLE if Quality Gate fails
          // true = set pipeline to UNSTABLE, false = don't
          waitForQualityGate abortPipeline: true
        }
      }
    }
  }
}