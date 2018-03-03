#!/bin/bash
ansible-playbook -vvvv -i inventory deploy.yml   -e my_route53_zone=$1  -e ssh_key_name=$2
