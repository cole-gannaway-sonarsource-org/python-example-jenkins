node {
  stage('SCM') {
    checkout scm
  }
  stage('SonarQube Analysis') {
    def scannerHome = tool 'SonarScanner';
    withSonarQubeEnv() {
      sh "printenv && ls -al && cd $JENKINS_HOME/workspace/python-example-jenkins_$BRANCH_NAME && ls -al && ${scannerHome}/sonar-scanner-5.0.1.3006-linux/bin/sonar-scanner"
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