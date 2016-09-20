# -*- coding: utf-8 -*-

from boto.route53.connection import Route53Connection

from aws_r53_dyndns.ip_providers import ExternalIpAddressProviderFactory


def update_record(credential, zone, domain, new_ip):
    conn = Route53Connection(**credential)
    _zone = conn.get_zone(zone)
    status = _zone.update_a(domain, new_ip)
    return status
