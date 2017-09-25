#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .parser import Parser
from .meta import Meta


class WubiParser(Parser):

    def __init__(self):
        super(WubiParser, self).__init__()

    def parse(self, f):
        for line in f:
            words = line.split()
            if len(words) == 2:
                yield Meta(words[0], words[1])
            elif len(words) == 3:
                priority = int(words[2])
                yield Meta(words[0], words[1], priority)
