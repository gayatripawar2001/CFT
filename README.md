# CloudFormation Template README

This README provides instructions for using the CloudFormation template provided in this repository. The template is designed to create 

## Prerequisites

Before you proceed, make sure you have the following prerequisites:

1. AWS Account: You need an AWS account to create and manage CloudFormation stacks.

2. AWS CLI: Install the AWS Command Line Interface (CLI) on your local machine. You can download it from [AWS CLI Installation Guide](https://aws.amazon.com/cli/).

## How to Create a CloudFormation Stack

1. **AWS CLI Configuration**: Ensure you have configured the AWS CLI with your AWS credentials using the `aws configure` command.

2. **Template Customization**: Modify the CloudFormation template (`your-template.yaml`) as needed, specifying parameter values and resource configurations.
   
- Create a yaml file which will create a SNS topic , SQS Queue and Subscription to the topic
  
- Create a yaml file which will create a S3 bucket with bucket versioning enabled and lifecycle policies configured to it
  
- Create a yaml file which will create a lambda function that will listens to the SQS queue message body and it will store the recieved messages 
  to the S3 bucket
  
- And Created the IAM role and permissions attached to the S3 bucket and lambda function

3. **Create Stack**: Run the following AWS CLI command to create a CloudFormation stack:
or 
4. **script** :create python script and run the script that will run the below commands and create a stacks 
**Create stack** :
-aws cloudformation create-stack --stack-name sns-sqs-stack --template-body file://sqs-sns.yaml --capabilities CAPABILITY_NAMED_IAM

-aws cloudformation create-stack --stack-name s3-stack --template-body file://s3-bucket.yaml --capabilities CAPABILITY_NAMED_IAM

-aws cloudformation create-stack --stack-name lambda-stack --template-body file://lambda1.yaml --capabilities CAPABILITY_NAMED_IAM

5. **Run the script**
   -Python script that will contains the aws CLI cammands to create stacks 

6. **Invoke lambda function** :

-aws lambda invoke --invocation-type RequestResponse --function-name lambda-sqs-sns --log-type Tail outputfile.txt;  more outputfile.txt

**Cleanup**

Don't forget to delete your CloudFormation stack and resources when you're finished to avoid incurring unnecessary costs. You can use the aws cloudformation delete-stack command as described earlier.

-aws cloudformation delete-stack --stack-name "yourstackname"

