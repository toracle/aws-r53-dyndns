# AWS Route53 Dyndns

[![Build Status](https://travis-ci.org/toracle/aws-r53-dyndns.svg?branch=master)](https://travis-ci.org/toracle/aws-r53-dyndns)

A simple tool to update AWS Route53 domain A record. Tested with py27, py35.

## Quickstart

Install with:

`pip install git+https://github.com/toracle/aws-r53-dyndns.git`

And run with:

`aws-r53-dyndns <your domain>`


## Usage

```
usage: aws-r53-dyndns [-h] [--zone [ZONE]] [--provider [{ipify}]]
                      [--aws-credentials-path [AWS_CREDENTIALS_PATH]]
                      domain

positional arguments:
  domain                domain to update

optional arguments:
  -h, --help            show this help message and exit
  --zone [ZONE]         zone name. guess from domain if not given
  --provider [{ipify}]  ip address provider
  --aws-credentials-path [AWS_CREDENTIALS_PATH]
                        path of aws credentials file
```

## Prerequisite

You should have two conditions:

* AWS credentials file
* Proper IAM permission to Route53

You might have an AWS credentials file on your home directory (~/.aws/credentials) if you're using awscli or boto3. 

Or simply create the file with this content:

```
[default]
aws_access_key_id=<your_access_key_id>
aws_secret_access_key=<your_secret_access_key>
```

If you're using IAM account, the account should have below permission at least.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Stmt1474383783000",
            "Effect": "Allow",
            "Action": [
                "route53:ChangeResourceRecordSets",
                "route53:ListResourceRecordSets"
            ],
            "Resource": [
                "arn:aws:route53:::hostedzone/{hosted_zone_id}"
            ]
        },
        {
            "Sid": "Stmt1474383783001",
            "Effect": "Allow",
            "Action": [
                "route53:ListHostedZones"
            ],
            "Resource": [
                "*"
            ]
        }
    ]
}
```

Replace `{hosted_zone_id}` with yours. 

You can see your zone id when you visit Route53 hosted zone with an URL on web browser, such like this: `https://console.aws.amazon.com/route53/home?regions=....#resource-record-sets:{your_hosted_zone_id}`

## TODO

* [ ] Choose AWS credential profile other than 'default'
* [ ] Use other credential method than a ini file (eg. specify as an argument directly, use env var)
* [ ] Some output messages
