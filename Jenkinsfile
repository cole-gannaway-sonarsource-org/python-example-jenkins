stage('SCM') {
  steps {
    checkout scm
  }
}
stage('SonarQube Analysis') {
  steps {
    def scannerHome = tool 'SonarScanner';
    withSonarQubeEnv() {
      sh "${scannerHome}/bin/sonar-scanner -Dsonar.sources=. -Dsonar.host.url=http://localhost:9000 -Dsonar.token=sqb_5789005784469477f4aa6393999a6838d8943ee5 -Dsonar.verbose=true"
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
