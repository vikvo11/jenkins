import jenkins

server = jenkins.Jenkins('http://134.122.74.209:8080/', username='test', password='1184070a7f78076b25ae29e0611b2236dc')
user = server.get_whoami()
#version = server.get_version()
print('Hello %s from Jenkins' % (user['fullName']))
print (server.jobs_count())
jobs = server.get_jobs()
print (jobs)
server.build_job('Send_msg')
#server.build_job('Send_msg', {'TOKEN': '521265983:AAFUSq8QQzLUURwmCgXeBCjhRThRvf9YVM0', 'CHAT_ID': '488735610', 'MSG': 'TestMesage'})
last_build_number = server.get_job_info('Send_msg')['lastCompletedBuild']['number']
build_info = server.get_build_info('Send_msg', last_build_number)
print (build_info)

