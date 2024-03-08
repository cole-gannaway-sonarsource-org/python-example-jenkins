stage('SCM') {
  checkout scm
}
stage('SonarQube Analysis') {
  def mvn = tool 'mvn';
  withSonarQubeEnv() {
    sh "${mvn}/bin/mvn clean verify sonar:sonar -Dsonar.projectKey=jenkinstest"
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
