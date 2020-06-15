from troposphere import Base64, Select, FindInMap, GetAtt
from troposphere import GetAZs, Join, Output, If, And, Not
from troposphere import Or, Equals, Condition
from troposphere import Parameter, Ref, Tags, Template
from troposphere.cloudformation import Init
from troposphere.cloudfront import Distribution
from troposphere.cloudfront import DistributionConfig
from troposphere.cloudfront import Origin, DefaultCacheBehavior
from troposphere.ec2 import PortRange
from troposphere.s3 import Bucket, WebsiteConfiguration


t = Template()

t.add_version("2010-09-09")

t.add_description("""\
Create multiple S3 Bucket for XKE""")
TestBucket1 = t.add_resource(Bucket(
    "TestBucket1",
    AccessControl="PublicRead",
    BucketName="xke-test-bucket-1",
))

TestBucket2 = t.add_resource(Bucket(
    "TestBucket2",
    AccessControl="PublicRead",
    BucketName="xke-test-bucket-2",
))

TestBucket3 = t.add_resource(Bucket(
    "TestBucket3",
    AccessControl="PublicRead",
    BucketName="xke-test-bucket-3",
))

TestBucket4 = t.add_resource(Bucket(
    "TestBucket4",
    AccessControl="PublicRead",
    BucketName="xke-test-bucket-4",
))

TestBucket5 = t.add_resource(Bucket(
    "TestBucket5",
    AccessControl="PublicRead",
    BucketName="xke-test-bucket-5",
))

TestBucket6 = t.add_resource(Bucket(
    "TestBucket6",
    AccessControl="PublicRead",
    BucketName="xke-test-bucket-6",
))

TestBucket7 = t.add_resource(Bucket(
    "TestBucket7",
    AccessControl="PublicRead",
    BucketName="xke-test-bucket-7",
))

TestBucket8 = t.add_resource(Bucket(
    "TestBucket8",
    AccessControl="PublicRead",
    BucketName="xke-test-bucket-8",
))

TestBucket9 = t.add_resource(Bucket(
    "TestBucket9",
    AccessControl="PublicRead",
    BucketName="xke-test-bucket-9",
))

BucketName1 = t.add_output(Output(
    "BucketName1",
    Description="Name of S3 bucket",
    Value=Ref(TestBucket1),
))

BucketName2 = t.add_output(Output(
    "BucketName2",
    Description="Name of S3 bucket",
    Value=Ref(TestBucket2),
))

BucketName3 = t.add_output(Output(
    "BucketName3",
    Description="Name of S3 bucket",
    Value=Ref(TestBucket3),
))

BucketName4 = t.add_output(Output(
    "BucketName4",
    Description="Name of S3 bucket",
    Value=Ref(TestBucket4),
))

BucketName5 = t.add_output(Output(
    "BucketName5",
    Description="Name of S3 bucket",
    Value=Ref(TestBucket5),
))

BucketName6 = t.add_output(Output(
    "BucketName6",
    Description="Name of S3 bucket",
    Value=Ref(TestBucket6),
))

BucketName7 = t.add_output(Output(
    "BucketName7",
    Description="Name of S3 bucket",
    Value=Ref(TestBucket7),
))

BucketName8 = t.add_output(Output(
    "BucketName8",
    Description="Name of S3 bucket",
    Value=Ref(TestBucket8),
))

BucketName9 = t.add_output(Output(
    "BucketName9",
    Description="Name of S3 bucket",
    Value=Ref(TestBucket9),
))

print(t.to_json())
