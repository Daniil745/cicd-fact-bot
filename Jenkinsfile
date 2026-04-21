pipeline {
    agent any

    environment {
        DOCKERHUB_USER = 'daniil9090'
	APP_NAME = 'fact-bot'
	TARGET_HOST = '192.168.1.104'
	TARGET_USER = 'daniil'
	VERSION = "build-${BUILD_NUMBER}"
    }

    stages {
	stage('Checkout') {
	    steps {
		echo 'Cloning repository...'
                checkout scm
            }
        }

	stage('Build docker image') {
	    steps {
		echo 'Building docker image...'
		sh """
		   cd app
		   docker build -t ${DOCKERHUB_USER}/${APP_NAME}:${VERSION} .
		   docker tag ${DOCKERHUB_USER}/${APP_NAME}:${VERSION} ${DOCKERHUB_USER}/${APP_NAME}:latest
		"""
	    }
	}

	stage('Push to dockerhub') {
	
	}
	
	stage('Deploy to VM2') {
            steps {
		echo 'Deploying to prod server...'
		sh 'echo "Would to deploy VM2 here"'
	    }
	}
    }

    post {
	success {
	    echo 'Pipeline completed successfully!'
	}
	failure {
	    echo 'Pipeline failed'
	}
    }

}
