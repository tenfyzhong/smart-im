#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from meta import Meta


class MetaTestCase(unittest.TestCase):
    def test_sort(self):
        a = [Meta(r'a', r'东', 255), Meta(r'a', r'工', 256)]
        a.sort(cmp=None, key=None, reverse=True)
        self.assertListEqual(
            a,
            [Meta(r'a', r'工', 256), Meta(r'a', r'东', 255)])

    def test_cmp(self):
        self.assertEqual(
            1,
            Meta(r'a', r'工', 256).__cmp__(Meta(r'a', r'东', 255)))
        self.assertEqual(
            1,
            Meta(r'a', r'工', 256).__cmp__(Meta(r'a', r'东', 256)))
        self.assertEqual(
            -1,
            Meta(r'a', r'东', 256).__cmp__(Meta(r'a', r'工', 256)))
        self.assertEqual(
            0,
            Meta(r'a', r'工', 256).__cmp__(Meta(r'a', r'工', 256)))


if __name__ == '__main__':
    unittest.main()
