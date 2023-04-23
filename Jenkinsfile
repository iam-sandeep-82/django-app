pipeline {
    // agent { docker {image "iamsandeep82/django-app:latest"}}
    agent any
    stages {
        stage('DOCKER RUNNING') {
            steps {
               sh "echo $PWD"
            }
        }
        stage('Create Docker Image') {
            steps {
            
                sh "docker build -t iamsandeep82/django-app:v1 ."
                sh "docker run -d -p 8000:8000 -e SECRET_KEY=1234 iamsandeep82/django-app:v1"
                sh "curl locahost:8000"
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