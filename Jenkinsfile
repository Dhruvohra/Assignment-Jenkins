pipeline {
    agent any
    stages {
    stage('Version Check') {
      steps {
        sh 'git status'
        echo 'Printing Files'
        sh ls
        sh 'python3 --version'
      }
    }
    stage('Run Script') {
      steps {
        sh 'python3 email.py'
      }
    }
  }
}
