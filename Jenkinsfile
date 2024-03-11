node {
  stage('SCM') {
    checkout scm
  }
  stage('SonarQube Analysis') {
    def scannerHome = tool 'SonarScanner';
    withSonarQubeEnv() {
      sh "${scannerHome}/sonar-scanner-cli-5.0.1.3006-linux/bin/sonar-scanner -Dsonar.token=$SONAR_TOKEN"
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