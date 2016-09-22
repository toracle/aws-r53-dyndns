# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function, unicode_literals)
from aws_r53_dyndns import base


def test_should_return_same_domain():
    assert base.get_zone_from_domain('toracle.com') == 'toracle.com'

def test_should_return_top_domain():
    assert base.get_zone_from_domain('api.toracle.com') == 'toracle.com'

def test_argparser_should_return_default_provider():
    argparser = base.get_argparser()
    options = argparser.parse_args(['toracle.com'])
    assert options.provider == 'ipify'
