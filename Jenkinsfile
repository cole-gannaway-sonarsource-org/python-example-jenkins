stage('SCM') {
  checkout scm
}
stage('SonarQube Analysis') {
  def scannerHome = tool 'sonar-scanner-cli';
  withSonarQubeEnv() {
    sh "${scannerHome}/bin/sonar-scanner -Dsonar.sources=. -Dsonar.host.url=http://localhost:9000"
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
