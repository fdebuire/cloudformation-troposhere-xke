from troposphere import Template, GetAtt
from troposphere.cloudformation import Stack

t = Template('MainStack')
t.set_version()

S3 = t.add_resource(Stack(
    'S3',
    TemplateURL='https://name-of-bucket.s3.amazonaws.com/S3.cform'
))

EC2 = t.add_resource(Stack(
    'EC2',
    Parameters=dict(
        BucketName=GetAtt(S3, 'Outputs.BucketName')
    ),
    TemplateURL='https://name-of-bucket.s3.amazonaws.com/EC2.cform'
))

print(t.to_yaml())
