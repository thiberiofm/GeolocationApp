#!/bin/bash
yum update -y && yum update -y
INTANCE_ID=($curl -s http://IP-TODO/latest/meta-data/instance-id)
aws ec2 associate-address --instance-id $INTANCE_ID --allocation eipalloc-todo
sudo amazon-linux-extras install docker
sudo service docker start
sudo docker container run -d -p80:5000 -v db:/tmp thiberiofm/geolocation_app_flask

