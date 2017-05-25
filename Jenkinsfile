pipeline {
    agent any
    stages {
      
            stage ("Install Python Virtual Enviroment") {
                steps {
                    sh 'virtualenv --no-site-packages -p /usr/bin/python3.5 env3'
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
                    . ./env/bin/activate
                    python setup.py sdist develop
                    deactivate
                   '''
              }
            }

            stage ("Collect Static files") {
                steps {
                  sh '''
                    . ./env/bin/activate
                    python manage.py collectstatic --noinput
                    deactivate
                   '''
                }
            }


            stage ("Run Unit/Integration Tests") {
               steps {
                  sh '''
                        . ./env/bin/activate
                        python manage.py jenkins
                        deactivate
                     '''
               }
            }
    }
}
