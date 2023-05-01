pipeline { 
    agent any
    } 
    stages {
        stage('properties') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('0 0 12 * * ?')])])
                    properties([buildDiscarder(logRotator(daysToKeepStr: '5', numToKeepStr: '20')),])
                }
                git 'https://github.com/photop33/project3.git'
            }
        }
                          stage('main.py') {
            steps {
                script {
                    bat 'start /min python main.py'
                    bat 'echo success main.py'
                }
            }
        }
     }
}
