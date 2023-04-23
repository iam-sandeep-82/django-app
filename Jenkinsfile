pipeline {
    // agent { docker {image "iamsandeep82/django-app:latest"}}
    agent any

    environment {
        dockerHome = tool 'myDocker'  // tool will provide a installed path
        mavenHome = tool 'myMaven'
        PATH = "$dockerHome/bin:$mavenHome/bin:$PATH" //from $ accessing variable

    }
    stages {
    
        stage('Create Docker Image') {
            steps {
            
                sh "docker build -t iamsandeep82/django-app:v${env.Version} ."
                sh "docker images"
            }
        }
        // stage('Package Installation') {
        //     steps {
        //         sh "python3 install -r requirements.txt"
        //         sh "python3 manage.py migrate"
        //         sh "python3 manage.py runserver"
        //     }
        // }
    }

    post{
        always{ echo "i run every condition"}
        success{ echo "i run only when any success occured"}
        failure{ echo "i run only when any error occured"}
    }
}