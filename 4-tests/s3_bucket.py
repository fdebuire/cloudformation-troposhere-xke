from troposphere import Output, Ref, Template
from troposphere.s3 import Bucket

template = Template()


def create_bucket(template):
    return template.add_resource(Bucket("TestBucket",
                                        BucketName="my-test-bucket"))


def add_bucket_output(template, s3_bucket):
    return template.add_output(Output(
        "BucketName",
        Value=Ref(s3_bucket),
        Description="Name of S3 bucket"
    ))


if __name__ == "__main__":
    s3_bucket = create_bucket(template)
    s3_output = add_bucket_output(template, s3_bucket)

    print(template.to_json())
