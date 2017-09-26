#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from im.parser import Parser
from im.meta import Meta


class ParserTestCase(unittest.TestCase):
    def test_insert_meta(self):
        p = Parser()
        meta0 = Meta('a', r'工', 100)
        p.insert_meta(meta0)
        self.assertEqual(p._inverted_list['a']._metas[0], meta0, msg=None)
        meta1 = Meta('a', r'工工', 255)
        p.insert_meta(meta1)
        self.assertEqual(p._inverted_list['a']._metas[1], meta1, msg=None)

    def test_empty(self):
        p = Parser()
        meta0 = Meta('', r'工')
        self.assertFalse(p.insert_meta(meta0))
        meta1 = Meta('a', r'')
        self.assertFalse(p.insert_meta(meta1))

    def setUp(self):
        self.get_meta_parser = Parser()
        self.meta0 = Meta('a', r'工', 156)
        self.get_meta_parser.insert_meta(self.meta0)
        self.meta1 = Meta('ab', r'节', 228)
        self.get_meta_parser.insert_meta(self.meta1)
        self.meta2 = Meta('aa', r'式', 228)
        self.get_meta_parser.insert_meta(self.meta2)
        self.meta3 = Meta('ab', r'蒸', 327)
        self.get_meta_parser.insert_meta(self.meta3)

    def test_get_meta1(self):
        metas, has_more = self.get_meta_parser.get_meta(
            'a',
            0,
            2,
            perfect_match=False)
        self.assertListEqual([self.meta0, self.meta2], metas, msg=None)
        self.assertTrue(has_more, msg=None)
        metas, has_more = self.get_meta_parser.get_meta(
            'a',
            2,
            2,
            perfect_match=False)
        self.assertListEqual([self.meta1, self.meta3], metas, msg=None)
        self.assertFalse(has_more, msg=None)

    def test_get_meta2(self):
        metas, has_more = self.get_meta_parser.get_meta(
            'a',
            0,
            3,
            perfect_match=False)
        self.assertListEqual(
            [self.meta0, self.meta2, self.meta1],
            metas,
            msg=None)
        self.assertTrue(has_more, msg=None)
        metas, has_more = self.get_meta_parser.get_meta(
            'a',
            3,
            3,
            perfect_match=False)
        self.assertListEqual([self.meta3], metas, msg=None)
        self.assertFalse(has_more, msg=None)

    def test_get_meta_no_more1(self):
        metas, has_more = self.get_meta_parser.get_meta(
            'aa',
            0,
            2,
            perfect_match=False)
        self.assertListEqual([self.meta2], metas, msg=None)
        self.assertFalse(has_more, msg=None)

    def test_get_meta_no_more2(self):
        metas, has_more = self.get_meta_parser.get_meta(
            'ab',
            0,
            2,
            perfect_match=False)
        self.assertListEqual([self.meta1, self.meta3], metas, msg=None)
        self.assertFalse(has_more, msg=None)

    def test_get_meta_empty1(self):
        metas, has_more = self.get_meta_parser.get_meta(
            'c',
            0,
            5,
            perfect_match=False)
        self.assertListEqual([], metas, msg=None)
        self.assertFalse(has_more, msg=None)

    def test_get_meta_empty2(self):
        metas, has_more = self.get_meta_parser.get_meta(
            'a',
            5,
            5,
            perfect_match=False)
        self.assertListEqual([], metas, msg=None)
        self.assertFalse(has_more, msg=None)

    def test_get_meta_perfect(self):
        metas, has_more = self.get_meta_parser.get_meta(
            'a',
            0,
            2,
            perfect_match=True)
        self.assertListEqual([self.meta0], metas, msg=None)
        self.assertFalse(has_more, msg=None)


if __name__ == '__main__':
    unittest.main()
