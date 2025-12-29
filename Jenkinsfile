pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Deploy - ETL') {
            steps {
                sh 'python etl/etl_pipeline.py'
            }
        }

        stage('Visualize') {
            steps {
                sh 'echo Dashboard refreshed'
            }
        }
    }
}
