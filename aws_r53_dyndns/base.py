# -*- coding: utf-8 -*-

import os
import logging

try:
    from ConfigParser import ConfigParser
except ImportError:
    from configparser import ConfigParser
from argparse import ArgumentParser
from boto.route53.connection import Route53Connection
from aws_r53_dyndns.exceptions import NotFoundException

logger = logging.getLogger('aws-r53-dyndns')


def update_record(credential, zone, domain, new_ip):
    conn = Route53Connection(**credential)
    _zone = conn.get_zone(zone)
    status = _zone.update_a(domain, new_ip)
    return status


def get_zone_from_domain(domain):
    return '.'.join(domain.split('.')[-2:])


def get_aws_credentials(options):
    return get_aws_credentials_from_config(options.aws_credentials_path)


def get_aws_credentials_from_config(path):
    if not os.path.isfile(path):
        raise NotFoundException("AWS credentials file is not exist on ~/.aws/credential! Install awscli and run 'aws configure'")

    cfg = ConfigParser()
    cfg.read(path)
    aws_access_key_id = cfg['default']['aws_access_key_id']
    aws_secret_access_key = cfg['default']['aws_secret_access_key']
    return {
        'aws_access_key_id': aws_access_key_id,
        'aws_secret_access_key': aws_secret_access_key
    }


def get_argparser():
    argparser = ArgumentParser('Update AWS Route53 A record')
    argparser.add_argument(
        'domain',
        help='domain to update'
    )
    argparser.add_argument(
        '--zone',
        nargs='?',
        help='zone name. guess from domain if not given'
    )
    argparser.add_argument(
        '--provider',
        nargs='?',
        default='ipify',
        choices=['ipify'],
        help='ip address provider'
    )
    argparser.add_argument(
        '--aws-credentials-path',
        nargs='?',
        default='~/.aws/credentials',
        help='path of aws credentials file'
    )
    return argparser
