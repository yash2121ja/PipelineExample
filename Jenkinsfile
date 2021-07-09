pipeline {
  agent any
  stages {
    stage('Start') {
      steps {
        echo 'Flie checking'
        sh '''ls 
pwd'''
      }
    }

    stage('Python and Html Linter') {
      parallel {
        stage('Python and Html Linter') {
          steps {
            echo 'Checking code python'
            sh '''ls
pwd
cd ShellScript
py_lint.sh
ls
pwd'''
          }
        }

        stage('Html code check') {
          steps {
            sh 'html_lint.sh'
          }
        }

      }
    }

    stage('Done') {
      steps {
        echo 'All check Done'
      }
    }

  }
}