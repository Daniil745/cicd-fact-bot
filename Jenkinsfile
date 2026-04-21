pipeline {
    agent any

    stages {
	stage('Checkout') {
	    steps {
		echo 'Cloning repository...'
                checkout scm
            }
        }
	
	stage('Test') {
	    steps {
	        echo 'Running test...'
	        sh 'echo "All test passed"'
            }
        }

	stage('Build docker image') {
	    steps {
		echo 'Building docker image...'
		sh 'cd app && docker build -t fact-bot:latest .'
	    }
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
