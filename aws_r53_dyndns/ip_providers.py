# -*- coding: utf-8 -*-

try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen

from aws_r53_dyndns.exceptions import NotFoundException


class PublicIpAddressProvider(object):
    def get_ip(self):
        raise NotImplementedError()


class IpifyPublicIpAddressProvider(PublicIpAddressProvider):
    name = 'ipify'

    def get_ip(self):
        response = urlopen('https://api.ipify.org/?format=text').read().decode('utf8')
        return response


def get_public_ip(provider_name='ipify'):
    classes = PublicIpAddressProvider.__subclasses__()
    for cls in classes:
        if cls.name == provider_name:
            return cls().get_ip()

    raise NotFoundException('No such external IP address provider: %s', provider_name)
