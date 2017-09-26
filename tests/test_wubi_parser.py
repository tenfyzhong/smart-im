#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import tempfile
from im.wubi_parser import WubiParser
from im.meta import Meta, KeyMetas


class WubiParserTestCase(unittest.TestCase):
    def setUp(self):
        self._wubi_parser = WubiParser()

    def test_load(self):
        f0 = tempfile.TemporaryFile(mode='w+')
        lines = ["a 工 0\n"]
        f0.writelines(lines)
        f0.seek(0)

        f1 = tempfile.TemporaryFile(mode='w+')
        lines = ["a 工 116\n", "ab 节 112\n"]
        f1.writelines(lines)
        f1.seek(0)

        p = WubiParser()
        files = [f0, f1]
        p.load(files)

        meta0 = Meta('a', r'工', 0)
        meta1 = Meta('ab', r'节', 112)

        key_metas0 = KeyMetas('a')
        key_metas0.insert(meta0)
        key_metas0.insert(meta1)

        key_metas1 = KeyMetas('ab')
        key_metas1.insert(meta1)

        inverted_list = {}
        inverted_list['a'] = key_metas0
        inverted_list['ab'] = key_metas1

        self.assertDictEqual(inverted_list, p._inverted_list, msg=None)

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
