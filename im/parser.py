#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .meta import KeyMetas


class Parser(object):
    """
    码表解释器
    """

    def __init__(self):
        self._inverted_list = {}

    def parse(self, f):
        """
        解释码表，返回Meta列表，或者yield Meta列表
        :f: 文件对象
        """
        raise NotImplementedError

    def load(self, files):
        """
        加载码表
        :files: 码表文件路径，支持多个码表文件，同样代码、同样的词，前面出现的优
        先级比后面的高，所以后面文件出现的会直接忽略掉，对于存在自定义码表文件的，
        自定义文件应该放在前面
        """
        def meta_key(meta):
            return meta.code() + ":" + meta.word()
        meta_set = set()
        for f in files:
            for meta in self.parse(f):
                key = meta_key(meta)
                if key not in meta_set:
                    self.insert_meta(meta)
                    meta_set.add(key)

    def insert_meta(self, meta):
        """ 插入新的meta
        对meta的code产生所有前缀子串，插入到对应子串的列表里

        :meta: 要插入的meta

        :return: True为插入成功
        """
        if not meta.code() or not meta.word():
            return False

        strs = [meta.code()[0:end] for end in range(1, len(meta.code())+1)]
        for s in strs:
            if s not in self._inverted_list:
                self._inverted_list[s] = KeyMetas(s)

            key_metas = self._inverted_list[s]
            key_metas.insert(meta)

        return True

    def get_meta(self, code, begin, count, perfect_match=False):
        """根据code查找匹配的词

        :code: 用户输入的code
        :begin: 开始的位置
        :count: 返回的个数
        :perfect_match: 完美匹配，如果为true，则要与code完全匹配才能匹配中，否则以code为前缀匹配
        :returns: ([metas], has_more)
        """
        if code not in self._inverted_list:
            return ([], False)

        metas = self._inverted_list[code]
        if begin >= metas.len():
            return ([], False)

        end = begin + count
        if not perfect_match:
            return (metas.metas()[begin:end], end < metas.len())

        result = []
        result = [meta for meta in metas.metas()
                  if meta.code() == code and len(result) < count + 1]
        return (result[0:count], len(result) > count)
