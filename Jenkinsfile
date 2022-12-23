pipeline {
    agent any
    stages {
    stage('Version Check') {
      steps {
        sh 'python3 --version'
      }
    }
    stage('Run Script') {
      steps {
        sh 'python3 main.py'
      }
    }
  }
}
