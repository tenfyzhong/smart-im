#!/usr/bin/env python
# -*- coding: utf-8 -*-

from parser import Parser
from meta import Meta
import logging


class WubiParser(Parser):

    def __init__(self):
        super(WubiParser, self).__init__()

    @Parser.sort_metas
    def parse(self, path):
        with open(path, 'r') as f:
            for line in f:
                words = line.split()
                if len(words) < 3:
                    logging.error(
                        'line[%s] should be the format:[code word priority]'
                        % line)
                try:
                    priority = int(words[2])
                except ValueError as e:
                    logging.error(e)
                m = Meta(words[0], words[1], priority)
                self.insert_meta(m)
