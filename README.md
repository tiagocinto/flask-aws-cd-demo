# Python's Flask CD Demo  
This is a sample repo to assist continuous delivery (CD) python's flask projects over the AWS cloud environment (Elastic Beanstalk). Based on https://github.com/noahgift/Flask-Elastic-Beanstalk and https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html.  

### General info ###
For better integration, use AWS Cloud9 IDE. 

### Running this project  ###
1- clone this repo;  
2- cd into the repo dir: cd /home/user/flask-aws-cd-demo;  
3- create a virtualenv: virtualenv .[venv_name];  
4- source the virtualenv (activate it): source .[venv_name]/bin/activate;  
5- let make install packages: make install install-local install-test;  
6- additionally, perform other make actions: make lint test format;  
7- run flask server: python main.py;  
8- open another shell and test with: 'curl http://127.0.0.1:8080/' or 'curl http://127.0.0.1:8080/echo/hello'.  

### Deploying on AWS  ###
1- update the .ebignore file with the virtual env folder previously created;  
2- on the elastic beanstalk GUI, go to 'Apps > Create a new app' and provides a app's name;  
3- click on the newly created app, and then on 'create a new env';  
4- check 'web server', the env's name, the python's version, and 'sample app'; (a)  
5- test your app with the url created on 'envs' option;  
6- on cloud shell, update 'environment', 'application_name', 'default_plataform', and 'default_region' in the .elasticbeanstalk/config.yml file (check those info on the eb GUI);  
7- deploy on eb: eb deploy;  
8- test your deployed app.  
(a) the environment creation provides the following resources: ec2 instance, instance security group, load balancer, load balancer security group, auto scaling group, s3 bucket, cloud watch alarms -- to monitor the load on the instances and detect high/low demand --, and domain name.  

 


### Configuring CD  ###
1- ...
