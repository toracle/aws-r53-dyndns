# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function, unicode_literals)

from aws_r53_dyndns.base import update_or_create_record
from aws_r53_dyndns.base import get_aws_credentials
from aws_r53_dyndns.base import get_zone_from_domain
from aws_r53_dyndns.base import get_argparser
from aws_r53_dyndns.ip_providers import get_public_ip


def main():
    argparser = get_argparser()
    options = argparser.parse_args()

    domain = options.domain
    zone = options.zone or get_zone_from_domain(domain)
    provider_name = options.provider
    credential = get_aws_credentials(options)
    
    ip = get_public_ip(provider_name)
    update_or_create_record(credential, zone, domain, ip)
