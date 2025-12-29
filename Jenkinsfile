pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Installing dependencies'
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Deploy - ETL') {
            steps {
                echo 'Running ETL pipeline'
                bat 'python etl\\etl_pipeline.py'
            }
        }

        stage('Visualize') {
            steps {
                echo 'Dashboard refreshed'
            }
        }
    }

    post {
        success {
            echo 'Pipeline executed successfully'
        }
        failure {
            echo 'Pipeline failed'
        }
    }
}
