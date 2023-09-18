import subprocess

# Define the AWS CLI commands as strings
stack_creation_commands = [
    'aws cloudformation create-stack --stack-name sns-sqs-stack --template-body file://sqs-sns.yaml --capabilities CAPABILITY_NAMED_IAM',
    'aws cloudformation create-stack --stack-name s3-stack --template-body file://s3-bucket.yaml --capabilities CAPABILITY_NAMED_IAM',
    'aws cloudformation create-stack --stack-name lambda-stack --template-body file://lambda1.yaml --capabilities CAPABILITY_NAMED_IAM'
]

# Function to execute AWS CLI commands
def execute_aws_commands(commands):
    for command in commands:
        try:
            subprocess.run(command, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e}")
            exit(1)

# Execute stack creation commands
print("Creating CloudFormation stacks...")
execute_aws_commands(stack_creation_commands)

print("Script execution completed.")
