## Install and Run

`pip install git+https://github.com/toracle/aws-r53-dyndns.git`

`aws-r53-dyndns <your domain>`


## Prerequisite

You should have two conditions:

* AWS credentials file
* Proper IAM permission to Route53

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
