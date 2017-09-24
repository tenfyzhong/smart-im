#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import unittest
from wubi_parser import WubiParser
from meta import Meta


class WubiParserTestCase(unittest.TestCase):
    def setUp(self):
        self._wubi_parser = WubiParser()

    def test_parse(self):
        metas = []
        dir_path = os.path.dirname(os.path.realpath(__file__))
        for meta in self._wubi_parser.parse(dir_path+'/../testdata/wubi.txt'):
            metas.append(meta)

        meta0 = Meta('a', r'工', 116)
        meta1 = Meta('thyg', r'自主', 112)
        meta2 = Meta('gidr', r'还愿', 112)
        self.assertListEqual(
            [meta0, meta1, meta2],
            metas,
            msg=None)


if __name__ == '__main__':
    unittest.main()
