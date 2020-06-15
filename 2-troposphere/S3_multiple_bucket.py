from troposphere import Output, Ref, Template
from troposphere.s3 import Bucket, PublicRead

t = Template("Create multiple S3 Bucket for XKE")
t.set_version()

for i in range(1, 10):
    s3_bucket = t.add_resource(Bucket("TestBucket" + str(i),
                                      BucketName="xke-test-bucket-" + str(i),
                                      AccessControl=PublicRead))
    t.add_output(Output(
        "BucketName" + str(i),
        Value=Ref(s3_bucket),
        Description="Name of S3 bucket"
    ))

print(t.to_json())
