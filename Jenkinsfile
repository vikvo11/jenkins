//Declarative Pipeline
pipeline {
    agent any
    stages{
    stage('Preparation') { // for display purposes
        // Get some code from a GitHub repository
        //git 'https://github.com/jglick/simple-maven-project-with-tests.git'
        // Get the Maven tool.
        // ** NOTE: This 'M3' Maven tool must be configured
        // **       in the global configuration.
        steps {
        
            script {
                def who
        who = sh ( 
            script: 'whoami',
            returnStdout: true
            ).trim()
echo "hm ${who}"
}

script {
BUILD_FULL = sh (
    script: "git log -1 --pretty=%B | grep '\\[jenkins-full]'",
    returnStatus: true
) == 0
echo "Build full flag: ${BUILD_FULL}"
}

    }
    }
    
    stage('Build') {
        steps{
            script{
        // Run the maven build
        withEnv(["WHOI=who"]) {
            
                sh 'echo "$WHOI" '
            
        }
            }
    }
    }
}}
//Scripted Pipeline
node { 
    def who 
    stage('Preparation') { 
        // for display purposes // Get some code from a GitHub repository //git 'https://github.com/jglick/simple-maven-project-with-tests.git' // Get the Maven tool. // ** NOTE: This 'M3' Maven tool must be configured // ** in the global configuration. 
        who = sh ( script: 'whoami', returnStdout: true ).trim() 
        echo "hm ${who}"

BUILD_FULL = sh ( script: "git log -1 --pretty=%B | grep '[jenkins-full]'", returnStatus: true ) == 0 
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
