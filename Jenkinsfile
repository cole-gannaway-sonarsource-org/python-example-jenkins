pipeline {
  agent {
    docker { image 'node:16-alpine' }
  }
  stages {
    stage('Test') {
      steps {
        echo 'Before running node --version'
        sh 'node --version'
        echo 'After running node --version'
      }
    }
  }
}