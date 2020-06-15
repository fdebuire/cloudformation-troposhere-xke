import unittest

from troposphere import Ref, Template
from troposphere.s3 import Bucket

from s3_bucket import create_bucket, add_bucket_output


class BucketTest(unittest.TestCase):
    def test_should_create_s3_bucket(self):
        # GIVEN
        template = Template()

        # WHEN
        s3_bucket = create_bucket(template)

        # THEN
        self.assertEqual(s3_bucket.title, "TestBucket")
        self.assertEqual(s3_bucket.BucketName, "my-test-bucket")

    def test_should_add_output_for_bucket(self):
        # GIVEN
        template = Template()
        s3_bucket = Bucket("TestBucket",
                           BucketName="my-test-bucket")

        # WHEN
        output = add_bucket_output(template, s3_bucket)

        # THEN
        self.assertEqual(output.title, "BucketName")
        self.assertEqual(output.Value, Ref(s3_bucket))
        self.assertEqual(output.Description, "Name of S3 bucket")


if __name__ == '__main__':
    unittest.main()
