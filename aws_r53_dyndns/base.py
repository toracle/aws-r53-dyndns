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


def create_record(zone, domain, new_ip):
    status = zone.add_a(domain, new_ip, ttl=600)
    return status


def update_record(zone, domain, new_ip):
    status = zone.update_a(domain, new_ip)
    return status


def update_or_create_record(credential, zone, domain, new_ip):
    conn = Route53Connection(**credential)
    _zone = conn.get_zone(zone)
    records = _zone.get_a(domain)

    if records:
        update_record(_zone, domain, new_ip)
    else:
        create_record(_zone, domain, new_ip)


def get_zone_from_domain(domain):
    return '.'.join(domain.split('.')[-2:])


def get_aws_credentials(options):
    return get_aws_credentials_from_config(options.aws_credentials_path)


def get_aws_credentials_from_config(path):
    _path = os.path.abspath(os.path.expanduser(path))
    if not os.path.isfile(_path):
        raise NotFoundException("AWS credentials file is not exist on {}! Install awscli and run 'aws configure'".format(_path))

    cfg = ConfigParser()
    cfg.read(_path)
    aws_access_key_id = cfg['default']['aws_access_key_id']
    aws_secret_access_key = cfg['default']['aws_secret_access_key']
    return {
        'aws_access_key_id': aws_access_key_id,
        'aws_secret_access_key': aws_secret_access_key
    }


def get_argparser():
    argparser = ArgumentParser()
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
