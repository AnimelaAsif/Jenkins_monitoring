pipeline {
    agent any

    stages {
        // stage('git clone') {
        //     steps {
        //         sh "git clone https://github.com/AnimelaAsif/Jenkins_monitoring.git"
        //     }
        // }
        stage("Run python file"){
            steps {
                sh "python3 Jenkins_monitoring/app.py"
                sh "cat api.log"
            }
        }
    }
}
