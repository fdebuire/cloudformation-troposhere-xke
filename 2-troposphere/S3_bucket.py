from troposphere import Output, Ref, Template
from troposphere.s3 import Bucket, PublicRead

t = Template("Create S3 Bucket for XKE")
t.set_version()

s3_bucket = t.add_resource(Bucket("TestBucket",
                                  BucketName="xke-test-bucket",
                                  AccessControl=PublicRead, ))

t.add_output(Output(
    "BucketName",
    Value=Ref(s3_bucket),
    Description="Name of S3 bucket"
))

print(t.to_json())
