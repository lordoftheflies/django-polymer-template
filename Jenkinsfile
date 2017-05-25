pipeline {
    agent { docker 'python:2.7.12' }
    stages {
      
            stage("Install Python Virtual Enviroment") {
                steps {
                    sh 'virtualenv --no-site-packages .'
                }
            }   

            stage ("Get Latest Code") {
                steps {
                  checkout scm
                }
            }

            stage ("Install Application Dependencies") {
              steps {
                sh '''
                    source bin/activate
                    python setup.py sdist develop
                    deactivate
                   '''
              }
            }

            stage ("Collect Static files") {
                steps {
                  sh '''
                    source bin/activate
                    python manage.py collectstatic --noinput
                    deactivate
                   '''
                }
            }


            stage ("Run Unit/Integration Tests") {
               steps {
                  sh '''
                        source ../bin/activate
                        python manage.py jenkins
                        deactivate
                     '''
               }
            }
    }
}
