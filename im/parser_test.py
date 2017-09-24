#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from parser import Parser
from meta import Meta, CodeMetas


class ParserTestCase(unittest.TestCase):
    def test_insert_meta(self):
        p = Parser()
        meta0 = Meta(r'a', r'工', 256)
        p.insert_meta(meta0)
        self.assertEqual(p._metas[r'a']._metas[0], meta0, msg=None)
        meta1 = Meta(r'a', r'工工', 255)
        p.insert_meta(meta1)
        self.assertEqual(p._metas[r'a']._metas[1], meta1, msg=None)

    def test_insert_inverted_list0(self):
        inverted_list = {}
        codeMetas0 = CodeMetas(r'a')
        meta00 = Meta(r'a', r'工', 256)
        codeMetas0.insert_meta(meta00)
        Parser._insert_inverted_list(inverted_list, r'a', codeMetas0)
        self.assertEqual(inverted_list[r'a'][0], codeMetas0)

        codeMetas1 = CodeMetas(r'ac')
        meta10 = Meta(r'ac', r'芭', 128)
        codeMetas1.insert_meta(meta10)
        Parser._insert_inverted_list(inverted_list, r'a', codeMetas1)
        self.assertEqual(inverted_list[r'a'][0], codeMetas0)
        self.assertEqual(inverted_list[r'a'][1], codeMetas1)

        codeMetas2 = CodeMetas(r'ab')
        meta20 = Meta(r'ab', r'节', 128)
        codeMetas2.insert_meta(meta20)
        meta21 = Meta(r'ab', r'蒸', 128)
        codeMetas2.insert_meta(meta21)
        Parser._insert_inverted_list(inverted_list, r'a', codeMetas2)
        self.assertEqual(inverted_list[r'a'][0], codeMetas0)
        self.assertEqual(inverted_list[r'a'][1], codeMetas2)
        self.assertEqual(inverted_list[r'a'][2], codeMetas1)

    def test_insert_inverted_list1(self):
        inverted_list = {}
        codeMetas0 = CodeMetas(r'a')
        meta00 = Meta(r'a', r'工', 256)
        codeMetas0.insert_meta(meta00)
        Parser._insert_inverted_list(inverted_list, r'a', codeMetas0)
        self.assertEqual(inverted_list[r'a'][0], codeMetas0)

        codeMetas2 = CodeMetas(r'ab')
        meta20 = Meta(r'ab', r'节', 128)
        codeMetas2.insert_meta(meta20)
        meta21 = Meta(r'ab', r'蒸', 128)
        codeMetas2.insert_meta(meta21)
        Parser._insert_inverted_list(inverted_list, r'a', codeMetas2)
        self.assertEqual(inverted_list[r'a'][0], codeMetas0)
        self.assertEqual(inverted_list[r'a'][1], codeMetas2)

        codeMetas1 = CodeMetas(r'ac')
        meta10 = Meta(r'ac', r'芭', 128)
        codeMetas1.insert_meta(meta10)
        Parser._insert_inverted_list(inverted_list, r'a', codeMetas1)
        self.assertEqual(inverted_list[r'a'][0], codeMetas0)
        self.assertEqual(inverted_list[r'a'][1], codeMetas2)
        self.assertEqual(inverted_list[r'a'][2], codeMetas1)

    def test_make_inverted_list(self):
        p = Parser()
        meta0 = Meta('a', r'工', 256)
        p.insert_meta(meta0)
        meta1 = Meta('ab', r'节', 128)
        p.insert_meta(meta1)
        meta2 = Meta('aa', r'式', 128)
        p.insert_meta(meta2)
        meta3 = Meta('ab', r'蒸', 127)
        p.insert_meta(meta3)
        p._sort_metas()
        p._make_inverted_list()
        self.assertListEqual(
            [meta0, meta2, meta1, meta3],
            p._inverted_list['a'].metas(),
            msg=None)
        self.assertListEqual(
            [meta2],
            p._inverted_list['aa'].metas(),
            msg=None)
        self.assertListEqual(
            [meta1, meta3],
            p._inverted_list['ab'].metas(),
            msg=None)


if __name__ == '__main__':
    unittest.main()
