# CloudFormation Template README

This README provides instructions for using the CloudFormation template provided in this repository. The template is designed to create the below:
1) An SQS queue which subscribes to a SNS topic based on a particular message type
2) A lambda function which is listening to the SQS Queue (in point 1) events and writing themessages body to s3
3) S3 bucket configured with versioning and lifecycle polices for that data
4) Necessary IAM policies and roles required for this use-case
5) Also, some improvements for this infra based on efficiency and security pointof view.
6) Include a Readme describing the work and how to run the stack
7) Add a script to run with the commands to run the stack

## Prerequisites

Before you proceed, make sure you have the following prerequisites:

1. AWS Account: You need an AWS account to create and manage CloudFormation stacks.

2. AWS CLI: Install the AWS Command Line Interface (CLI) on your local machine. You can download it from [AWS CLI Installation Guide](https://aws.amazon.com/cli/).

## How to Create a CloudFormation Stack

1. **AWS CLI Configuration**: Ensure you have configured the AWS CLI with your AWS credentials using the `aws configure` command.

2. **Template Customization**: Modify the CloudFormation template (`your-template.yaml`) as needed, specifying parameter values and resource configurations.
   
  - Create a yaml file which will create a SNS topic , SQS Queue and Subscription to the topic
  
  - Create a yaml file which will create a S3 bucket with bucket versioning enabled and lifecycle policies configured to it
  
  - Create a yaml file which will create a lambda function that will listens to the SQS queue message body and it will store the recieved 
    messages to the S3 bucket
  
  - And Created the IAM role and permissions attached to the S3 bucket and lambda function
  
3. **script** :create python script and run the script that will run the below commands and create a stacks 

   -aws cloudformation create-stack --stack-name sns-sqs-stack --template-body file://sqs-sns.yaml --capabilities CAPABILITY_NAMED_IAM

   -aws cloudformation create-stack --stack-name s3-stack --template-body file://s3-bucket.yaml --capabilities CAPABILITY_NAMED_IAM

   -aws cloudformation create-stack --stack-name lambda-stack --template-body file://lambda1.yaml --capabilities CAPABILITY_NAMED_IAM

4. **Run the script**
   
   -Python script that will contains the aws CLI cammands to create stacks 

6. **Invoke lambda function** :

   -aws lambda invoke --invocation-type RequestResponse --function-name lambda-sqs-sns --log-type Tail outputfile.txt;  more outputfile.txt

## Efficiency and Security Improvements:

-  Use AWS CloudFormation Nested Stacks: If your infrastructure is complex, consider using AWS CloudFormation nested stacks to modularize your 
   templates. This can make it easier to manage and update your infrastructure.
-  Implement robust error handling in your Lambda function to handle failures gracefully.
-  cloudWatch Alarms and Monitoring: Set up CloudWatch alarms to monitor resource utilization and trigger actions (e.g., scaling) based on 
   predefined thresholds. This helps in proactive management of your resources
   
**Security improvements:**
-  Access Control:
   Review and refine IAM roles and policies to ensure the principle of least privilege for Lambda, SQS, and S3 access.
-  Backup and Disaster Recovery:
   Implement backup and disaster recovery strategies for critical components, such as maintaining backups of important data in case of accidental 
   deletion.
-  Multi-Factor Authentication (MFA): Enable MFA for AWS accounts and IAM users to add an extra layer of security.

## Cleanup

Don't forget to delete your CloudFormation stack and resources when you're finished to avoid incurring unnecessary costs. You can use the aws cloudformation delete-stack command.

 -aws cloudformation delete-stack --stack-name "yourstackname"

