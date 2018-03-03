#!/bin/bash
aws ec2 describe-security-groups |grep -i groupid|while read a b ; do    sg=`echo $b|sed 's/\"//g'`; aws ec2 delete-security-group  --group-id $sg ; done
