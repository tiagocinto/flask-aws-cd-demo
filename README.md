# Python's Flask CD Demo  
This is a sample repo to assist continuous delivery (CD) python's flask projects over the AWS cloud environment (Elastic Beanstalk). Based on https://github.com/noahgift/Flask-Elastic-Beanstalk and https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html.  

### General info ###
For better integration, use AWS Cloud9 IDE. 

### Running this project  ###
1. clone this repo;  
1. cd into the repo dir: cd /home/user/flask-aws-cd-demo;  
1. create a virtualenv: virtualenv .[venv_name];  
1. source the virtualenv (activate it): source .[venv_name]/bin/activate;  
1. let make install packages: make install install-local install-test;  
1. additionally, perform other make actions: make lint test format;  
1. run flask server: python main.py;  
1. open another shell and test with: 'curl http://127.0.0.1:8080/' or 'curl http://127.0.0.1:8080/echo/hello'.  

### Deploying on AWS  ###
1. update the .ebignore file with the virtual env folder previously created;  
1. on the elastic beanstalk GUI, go to 'apps > create a new app' and provides an app's name;  
1. click on the newly created app, and then on 'create a new env';  
1. choose 'web server' and 'sample app';  
2. type the env's name and the python's version;  
3. test your app with the url created on 'envs' option<sup>a</sup>;  
4. on cloud shell, update 'environment', 'application_name', 'default_plataform', and 'default_region' in the .elasticbeanstalk/config.yml file (check those info on the eb GUI);  
5. deploy on eb: eb deploy [env's_name];  
6. test your deployed app.  

<sup>a</sup> the environment creation provides the following resources: ec2 instance, instance security group, load balancer, load balancer security group, auto scaling group, s3 bucket, cloud watch alarms -- to monitor the load on the instances and detect high/low demand --, and domain name.  
 
### Configuring CD  ###
1. go to the code build GUI (build menu) and create a new project (check if you are on the same region of eb's app);  
1. on source, choose 'GitHub' and connect to your account using OAuth;  
1. select your repo;  
1. check 'use git submodules', 'report build statuses to source...', and 'rebuild every time a code change...';  
1. choose 'Amazon Linux 2' for OS, 'standard' for runtime, and 'aws/codebuild/amazonlinux2-aarch64-standard:2.0' for image version;  
1. after you create the build, navigate to the "build details" section and click on the service role;  
1. click on 'add permissions > attach roles';  
1. filter by 'AdministratorAccess' and add it;  
1. set the 'eb deploy' line in Makefile to your deploy env's name;  
1. set the virtual env's name for the pre-building conditions in buildspec.yml;  
1. test CD confs by committing some changes to application.py. 
