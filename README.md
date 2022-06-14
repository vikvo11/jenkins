# jenkins
curl -X POST http://test:apiToken@134.122.74.209:8080/job/test_job/build


curl -X POST http://admin:apiToken@35.177.232.11:8080/job/Send_msg/build --data-urlencode json='{"parameter": [{"name":"TOKEN", "value":"*****"}, {"name":"CHAT_ID", "value":"488735610"}, {"name":"MSG", "value":"Sample\Plan"}]}'

sudo ufw allow 8080
sudo ufw enable
sudo ufw status

**(Declarative Pipeline)**
pipeline {
environments{foo="foo"}
}
echo "foo - ${env.foo}"

**(Scripted Pipeline)**
node{
def home
 stage ('test'){
 withEnv(["java_home=$home"])
   {sh 'echo $java_home'
   }
   
 }
}
