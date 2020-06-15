import os

from troposphere import Template, Ref, Parameter
from troposphere.ec2 import SecurityGroup, Instance

t = Template("Create EC2")
t.set_version()

bucket_name = t.add_parameter(Parameter(
    'BucketName',
    Type='String'
))

security_group_ingress = []

cidrs = ["10.0.1.0/24",
         "10.0.2.0/24",
         "10.0.3.0/24",
         "10.0.4.0/24",
         "10.0.5.0/24",
         "10.0.10.0/24"]
for cidr_ip in cidrs:
    security_group_ingress.append({'FromPort': 22,
                                   'ToPort': 22,
                                   'IpProtocol': 'tcp',
                                   'CidrIp': cidr_ip})

security_group = t.add_resource(SecurityGroup(
    'XKESecurityGroup',
    SecurityGroupIngress=security_group_ingress,
    VpcId='vpc-1234',
    GroupDescription='Enable SSH access to the EC2 machine'
))


environment = os.getenv('ENVIRONMENT', 'dev')


def get_instance_type():
    if environment == 'dev':
        return 't2.micro'
    elif environment == 'prod':
        return 'm5.large'
    raise ValueError("Environment {} unknown".format(environment))


t.add_resource(Instance(
    'XKEInstance',
    ImageId='ami-951945d0',
    DisableApiTermination=True,
    InstanceType=get_instance_type(),
    KeyName='xke-key',
    SecurityGroupIds=[Ref(security_group)],
    SubnetId='subnet-1234',
))

print(t.to_yaml())
