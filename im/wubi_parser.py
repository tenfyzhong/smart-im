#!/usr/bin/env python
# -*- coding: utf-8 -*-

from parser import Parser
from meta import Meta
import logging


class WubiParser(Parser):

    def __init__(self):
        super(WubiParser, self).__init__()

    def parse(self, f):
        for line in f:
            words = line.split()
            priority = 0
            try:
                priority = int(words[2])
            except ValueError as e:
                logging.error(e)
            yield Meta(words[0], words[1], priority)
