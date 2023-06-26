import boto3
import csv

def extract_critical_findings():
    # Specify the AWS profile to use
    aws_profile = 'nxms-internal-security'
    # Specify the AWS region
    aws_region = 'us-east-1'  # Replace with your desired region

    # Create a session with the specified AWS profile and region
    session = boto3.Session(profile_name=aws_profile, region_name=aws_region)

    # Create a Boto3 client for Security Hub
    securityhub_client = session.client('securityhub')

    # Retrieve critical findings from Security Hub
    response = securityhub_client.get_findings(
        Filters={
            'SeverityLabel': [
                {
                    'Value': 'CRITICAL',
                    'Comparison': 'EQUALS'
                }
            ]
        },
        MaxResults=100  # Adjust the maximum number of findings to retrieve if needed
    )

    findings = response['Findings']

    # Prepare CSV file
    csv_filename = 'critical_findings.csv'
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Finding ID', 'Title', 'Description', 'Severity'])

        # Write each finding to CSV
        for finding in findings:
            finding_id = finding['Id']
            title = finding['Title']
            description = finding['Description']
            severity = finding['Severity']['Label']

            writer.writerow([finding_id, title, description, severity])

    print(f'Critical findings extracted and saved to "{csv_filename}".')


# Call the function to extract and save the critical findings
extract_critical_findings()
