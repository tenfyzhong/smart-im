#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from meta import Meta


class MetaTestCase(unittest.TestCase):
    def test_sort(self):
        a = [Meta('a', r'东', 256), Meta('a', r'工', 255)]
        a.sort(cmp=None, key=None, reverse=False)
        self.assertListEqual(
            a,
            [Meta('a', r'工', 255), Meta('a', r'东', 256)])

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


if __name__ == '__main__':
    unittest.main()
