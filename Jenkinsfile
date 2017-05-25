node {
  def installed = fileExists 'bin/activate'

  if (!installed) {
      stage("Install Python Virtual Enviroment") {
          sh 'virtualenv --no-site-packages .'
      }
  }  

  stage ("Get Latest Code") {
      checkout scm
  }

  stage ("Install Application Dependencies") {
      sh '''
          source bin/activate
          python setup.py sdist develop
          deactivate
         '''
  }

  stage ("Collect Static files") {
      sh '''
          source bin/activate
          python manage.py collectstatic --noinput
          deactivate
         '''
  }


  stage ("Run Unit/Integration Tests") {
      def testsError = null
      try {
          sh '''
              source ../bin/activate
              python manage.py jenkins
              deactivate
             '''
      }
      catch(err) {
          testsError = err
          currentBuild.result = 'FAILURE'
      }
      finally {
          junit 'reports/junit.xml'

          if (testsError) {
              throw testsError
          }
      }
  }
}
