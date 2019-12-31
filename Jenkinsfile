pipeline {
environment {
BUILD_SCRIPTS='mypipeline'
BUILD_HOME='/jenkins/workspace/devops_test_1'
 }
agent { label 'aws' }
stages {
stage('Checkout') {
steps {
echo 'Checkout'
git 'https://github.com/yahelron/World-of-Games.git'
  }
 }
stage('build') {
steps {
echo 'build'
sh 'sudo docker-compose build'
  }
 }
stage('run') {
steps {
echo 'run'
sh 'sudo docker-compose up &'
  }
 }
stage('test') {
    agent { label 'master' }
steps {
      dir ('C:\\code\\github.com\\projects\\World of Games\\tests') {
                      bat '''
                      python e2e.py
                      @IF NOT %ERRORLEVEL% == 0 EXIT /b %ERRORLEVEL%
                      '''
      }
echo 'test'
   }
  }
stage('done') {
    agent { label 'aws' }
steps {
echo 'done successfully!'
   }
  }
 }
post {
always {
echo 'always'
sh 'ls /jenkins'
sh 'sudo docker-compose -f $BUILD_HOME/docker-compose.yml down'
sh 'sudo docker-compose -f $BUILD_HOME/docker-compose.yml rm'
sh 'sudo docker rmi -f devopstest1_flasc_server python'
// sh 'rm -fr /jenkins/workspace/*'

  }
 }
}
