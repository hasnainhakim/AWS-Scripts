# AWS Security Hub Critical Findings Extractor

This Python script connects to AWS Security Hub using the AWS SDK (Boto3) and extracts critical findings. The findings are filtered based on severity and saved to a CSV file.

## Prerequisites

- Python 3.x
- AWS CLI installed and configured with appropriate credentials and region.
- Boto3 package installed. Install it using `pip install boto3`.

## Usage

1. Clone the repository or download the `extract_critical_findings.py` script.

2. Open the script in a text editor and make the following modifications:

   - Replace `'your_aws_profile'` with the name of your configured AWS profile.
   - Replace `'us-west-2'` with your desired AWS region.

3. Run the script by executing the following command in a terminal:

   ```bash
   python extract_critical_findings.py
The script will connect to AWS Security Hub, retrieve critical findings, and save them to a CSV file named critical_findings.csv in the same directory.

Open the CSV file to view the extracted critical findings.

Customization
If you want to adjust the maximum number of findings to retrieve, modify the MaxResults parameter in the get_findings API call.

You can further customize the CSV file and its columns by modifying the code in the for loop where findings are written to the CSV.

License
This project is licensed under the MIT License.
