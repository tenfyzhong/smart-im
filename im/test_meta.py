#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from .meta import Meta, KeyMetas


class MetaTestCase(unittest.TestCase):
    def test_sort(self):
        meta0 = Meta('a', r'东', 256)
        meta1 = Meta('a', r'工', 255)
        a = [meta0, meta1]
        a.sort()
        self.assertListEqual(
            a,
            [meta1, meta0])

    def test_cmp0(self):
        self.assertEqual(
            1,
            Meta('a', r'工', 256).__cmp__(Meta('a', r'东', 255)))
        self.assertEqual(
            -1,
            Meta('a', r'东', 255).__cmp__(Meta('a', r'工', 256)))
        self.assertEqual(
            0,
            Meta('a', r'工', 256).__cmp__(Meta('a', r'工', 256)))

    def test_cmp1(self):
        self.assertEqual(
            -1,
            Meta('a', r'工', 256).__cmp__(Meta(r'aa', r'式', 256)),
            msg=None)
        self.assertEqual(
            0,
            Meta('aa', r'式', 256).__cmp__(Meta(r'aa', r'式', 256)),
            msg=None)
        self.assertEqual(
            1,
            Meta('aaa', r'工', 256).__cmp__(Meta(r'aa', r'式', 256)),
            msg=None)


class KeyMetasTestCase(unittest.TestCase):
    def test_insert(self):
        key_metas = KeyMetas('a')
        meta0 = Meta('a', r'工', 100)
        key_metas.insert(meta0)
        self.assertListEqual([meta0], key_metas.metas(), msg=None)
        meta1 = Meta('a', r'东', 200)
        key_metas.insert(meta1)
        self.assertListEqual([meta0, meta1], key_metas.metas(), msg=None)
        meta2 = Meta('a', r'切', 150)
        key_metas.insert(meta2)
        self.assertListEqual(
            [meta0, meta2, meta1],
            key_metas.metas(),
            msg=None)
        meta3 = Meta('aa', r'式', 150)
        key_metas.insert(meta3)
        self.assertListEqual(
            [meta0, meta2, meta1, meta3],
            key_metas.metas(),
            msg=None)


if __name__ == '__main__':
    unittest.main()
