pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Installing dependencies'
                bat '"C:\\Users\\Dell\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" -m pip install --upgrade pip'
                bat '"C:\\Users\\Dell\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" -m pip install --only-binary=:all: -r requirements.txt'
            }
        }

        stage('Deploy - ETL') {
            steps {
                echo 'Running ETL pipeline'
                bat '"C:\\Users\\Dell\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" etl\\etl_pipeline.py'
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
