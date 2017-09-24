#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import tempfile
from .wubi_parser import WubiParser
from .meta import Meta


class WubiParserTestCase(unittest.TestCase):
    def setUp(self):
        self._wubi_parser = WubiParser()

    def test_parse(self):
        f = tempfile.TemporaryFile(mode='w+')
        lines = ["a 工 116\n", "thyg 自主 112\n", "gidr 还愿 112\n"]
        f.writelines(lines)
        f.seek(0)

        p = WubiParser()
        metas = []
        for meta in p.parse(f):
            metas.append(meta)

        meta0 = Meta('a', r'工', 116)
        meta1 = Meta('thyg', r'自主', 112)
        meta2 = Meta('gidr', r'还愿', 112)
        self.assertListEqual(
            [meta0, meta1, meta2],
            metas,
            msg=None)

    def test_parse_no_priority(self):
        f = tempfile.TemporaryFile(mode='w+')
        lines = ["a 工"]
        f.writelines(lines)
        f.seek(0)

        p = WubiParser()
        metas = []
        for meta in p.parse(f):
            metas.append(meta)

        meta0 = Meta('a', r'工', 10000)
        self.assertListEqual([meta0], metas)


if __name__ == '__main__':
    unittest.main()
