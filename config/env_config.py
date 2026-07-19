import os
from config.validators import validate_env_vars

class StackEnvConfig:
    def __init__(self, project_name, environment, aws_account):
        validate_env_vars(
            "PROJECT_NAME",
            "PROJECT_OWNER",
            "BUCKET_TERRAFORM_STATE_NAME",
            "BUCKET_WEBSITE_TEST_NAME",
            "BUCKET_WEBSITE_PROD_NAME",
            "AWS_APATITE_PROD_ACCOUNT_ID",
            "AWS_REGION",
        )
        self.project_owner = os.getenv("PROJECT_OWNER")
        self.aws_account = aws_account
        self.region = os.getenv("AWS_REGION")
        self.project_name = project_name
        self.stack_name = project_name
        self.environment = environment
        self.application_id_tag = os.getenv("PROJECT_NAME")

        self.terraform_state_bucket_name = os.getenv("BUCKET_TERRAFORM_STATE_NAME")

        

        self.test_website_bucket_name = os.getenv("BUCKET_WEBSITE_TEST_NAME")
        self.dev_website_bucket_name = os.getenv("BUCKET_WEBSITE_DEV_NAME")
        self.prod_website_bucket_name = os.getenv("BUCKET_WEBSITE_PROD_NAME")
        self.tags = {
            "Project": self.project_name,
            "Owner": self.project_owner,
            "Environment": self.environment,
        }

class stackConfig:
    def __init__(self, project_name):
        self.prod = StackEnvConfig(
            project_name = project_name,
            environment = "prod",
            aws_account = os.getenv("AWS_APATITE_PROD_ACCOUNT_ID")
        )

stack_config = {
    os.getenv("PROJECT_NAME") : stackConfig(project_name = os.getenv("PROJECT_NAME"))
}