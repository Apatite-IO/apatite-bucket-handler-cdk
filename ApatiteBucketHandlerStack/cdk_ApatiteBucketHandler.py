from aws_cdk import (
    Stack,
    RemovalPolicy,
    CfnOutput,
    Tags,
    aws_s3 as s3
)
from constructs import Construct
from config.env_config import StackEnvConfig

class cdk_ApatiteBucketHandler(Stack):

    def __init__(self, scope: Construct, construct_id: str, config: StackEnvConfig, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        terraform_state_bucket = s3.Bucket(
            self,
            config.terraform_state_bucket_name,
            bucket_name = config.terraform_state_bucket_name,
            removal_policy = RemovalPolicy.DESTROY
        )
        for key, value in config.tags.items():
            Tags.of(terraform_state_bucket).add(key, value)

        CfnOutput(
            self,
            "TerraformStateBucketName",
            value = terraform_state_bucket.bucket_name,
            description = "S3 bucket for storing Terraform state files",
        )

        test_website_bucket = s3.Bucket(
            self,
            config.test_website_bucket_name,
            bucket_name = config.test_website_bucket_name,
            removal_policy = RemovalPolicy.DESTROY,
            auto_delete_objects = True,
            versioned = True,
            # Static website hosting
            website_index_document = "index.html",
            website_error_document = "index.html",
            # Allow public read for website serving
            block_public_access = s3.BlockPublicAccess(
                block_public_acls = False,
                block_public_policy = False,
                ignore_public_acls = False,
                restrict_public_buckets = False,
            ),
            public_read_access = True,
            cors = [
                s3.CorsRule(
                    allowed_methods = [
                        s3.HttpMethods.GET,
                        s3.HttpMethods.HEAD,
                    ],
                    allowed_origins = ["*"],
                    allowed_headers = ["*"],
                    max_age = 3000,
                )
            ],
        )
        for key, value in config.tags.items():
            Tags.of(test_website_bucket).add(key, value)

        CfnOutput(
            self,
            "TestWebsiteBucketUrl",
            value = test_website_bucket.bucket_website_url,
            description = "Test website S3 static hosting URL",
        )
        CfnOutput(
            self,
            "TestWebsiteBucketName",
            value = test_website_bucket.bucket_name,
            description = "Test website S3 bucket name",
        )

        dev_website_bucket = s3.Bucket(
            self,
            config.dev_website_bucket_name,
            bucket_name = config.dev_website_bucket_name,
            removal_policy = RemovalPolicy.DESTROY,
            auto_delete_objects = True,
            versioned = True,
            # Static website hosting
            website_index_document = "index.html",
            website_error_document = "index.html",
            # Allow public read for website serving
            block_public_access = s3.BlockPublicAccess(
                block_public_acls = False,
                block_public_policy = False,
                ignore_public_acls = False,
                restrict_public_buckets = False,
            ),
            public_read_access = True,
            cors = [
                s3.CorsRule(
                    allowed_methods = [
                        s3.HttpMethods.GET,
                        s3.HttpMethods.HEAD,
                    ],
                    allowed_origins = ["*"],
                    allowed_headers = ["*"],
                    max_age = 3000,
                )
            ],
        )
        for key, value in config.tags.items():
            Tags.of(dev_website_bucket).add(key, value)

        prod_website_bucket = s3.Bucket(
            self,
            config.prod_website_bucket_name,
            bucket_name = config.prod_website_bucket_name,
            removal_policy = RemovalPolicy.DESTROY,
            auto_delete_objects = True,
            versioned = True,
            # Static website hosting
            website_index_document = "index.html",
            website_error_document = "index.html",
            # Allow public read for website serving
            block_public_access = s3.BlockPublicAccess(
                block_public_acls = False,
                block_public_policy = False,
                ignore_public_acls = False,
                restrict_public_buckets = False,
            ),
            public_read_access = True,
            cors = [
                s3.CorsRule(
                    allowed_methods = [
                        s3.HttpMethods.GET,
                        s3.HttpMethods.HEAD,
                    ],
                    allowed_origins = ["*"],
                    allowed_headers = ["*"],
                    max_age = 3000,
                )
            ],
        )
        for key, value in config.tags.items():
            Tags.of(prod_website_bucket).add(key, value)

        CfnOutput(
            self,
            "ProdWebsiteBucketName",
            value = prod_website_bucket.bucket_name,
            description = "Production website S3 bucket name",
        )
        CfnOutput(
            self,
            "ProdWebsiteBucketUrl",
            value = prod_website_bucket.bucket_website_url,
            description = "Production website S3 static hosting URL",
        )

        self.template_options.description = f"{config.project_name} - {config.environment} stack"