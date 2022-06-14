# jenkins
curl -X POST http://test:apiToken@134.122.74.209:8080/job/test_job/build


curl -X POST http://admin:apiToken@35.177.232.11:8080/job/Send_msg/build --data-urlencode json='{"parameter": [{"name":"TOKEN", "value":"*****"}, {"name":"CHAT_ID", "value":"488735610"}, {"name":"MSG", "value":"Sample\Plan"}]}'

sudo ufw allow 8080
sudo ufw enable
sudo ufw status



pipeline:

node {
    def who
    stage('Preparation') { // for display purposes
        // Get some code from a GitHub repository
        //git 'https://github.com/jglick/simple-maven-project-with-tests.git'
        // Get the Maven tool.
        // ** NOTE: This 'M3' Maven tool must be configured
        // **       in the global configuration.
        who = sh ( 
            script: 'whoami',
            returnStdout: true
            ).trim()
echo "hm ${who}"

BUILD_FULL = sh (
    script: "git log -1 --pretty=%B | grep '\\[jenkins-full]'",
    returnStatus: true
) == 0
echo "Build full flag: ${BUILD_FULL}"


    }
    stage('Build') {
        // Run the maven build
        withEnv(["WHOI=$who"]) {
            if (isUnix()) {
                sh 'echo "$WHOI" '
            } else {
                bat(/echo "%who"/)
            }
        }
    }
  
}
