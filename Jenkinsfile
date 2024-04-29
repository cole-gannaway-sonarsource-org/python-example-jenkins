node {
  triggers {
    pollSCM('H/5 * * * *')
  }
  stage('SCM') {
    checkout scm
  }
  stage('SonarQube Analysis') {
  def scannerHome = tool 'SonarScanner';
    withSonarQubeEnv() {
      sh "${scannerHome}/sonar-scanner-5.0.1.3006-linux/bin/sonar-scanner"
    }
  }
}