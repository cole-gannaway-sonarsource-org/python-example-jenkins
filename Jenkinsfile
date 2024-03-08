
pipeline{
    agent{
        label "node"
    }
    stages{
        stage("SCM"){
            steps{
                echo "========executing SCM========"
                checkout scm
            }
            post{
                always{
                    echo "========always========"
                }
                success{
                    echo "========SCM executed successfully========"
                }
                failure{
                    echo "========SCM execution failed========"
                }
            }
        }
        stage("SonarQube Analysis"){
            steps{
                def scannerHome = tool 'sonar-scanner-cli';
                withSonarQubeEnv() {
                  sh "${scannerHome}/bin/sonar-scanner -Dsonar.sources=. -Dsonar.token=sqb_5789005784469477f4aa6393999a6838d8943ee5 -Dsonar.host.url=http://localhost:9000"
                }
                echo 'SonarQube Analysis would be running'
            }
            post{
                always{
                    echo "========always========"
                }
                success{
                    echo "========SonarQube Analysis executed successfully========"
                }
                failure{
                    echo "========SonarQube Analysis execution failed========"
                }
            }
        }
        stage("Quality Gate"){
            steps{
                timeout(time: 1, unit: 'HOURS') {
                  // Parameter indicates whether to set pipeline to UNSTABLE if Quality Gate fails
                  // true = set pipeline to UNSTABLE, false = don't
                  waitForQualityGate abortPipeline: true
                }
            }
            post{
                always{
                    echo "====++++always++++===="
                }
                success{
                    echo "====++++Quality Gate executed successfully++++===="
                }
                failure{
                    echo "====++++Quality Gate execution failed++++===="
                }
        
            }
        }
    }
    post{
        always{
            echo "========always========"
        }
        success{
            echo "========pipeline executed successfully ========"
        }
        failure{
            echo "========pipeline execution failed========"
        }
    }
} 