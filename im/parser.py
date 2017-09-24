#!/usr/bin/env python
# -*- coding: utf-8 -*-
from meta import CodeMetas


class Parser(object):
    """
    码表解释器
    """

    def __init__(self):
        self._metas = {}
        self._inverted_list = {}

    def parse(self, path):
        """
        解释码表，返回Meta列表，或者yield Meta列表
        """
        raise NotImplementedError

    def load(self, paths):
        """
        加载码表
        :paths: 码表文件路径，支持多个码表文件，同样代码、同样的词，前面出现的优
        先级比后面的高，所以后面文件出现的会直接忽略掉，对于存在自定义码表文件的，
        自定义文件应该放在前面
        """
        def meta_key(meta):
            return meta.code() + ":" + meta.word()
        meta_set = set()
        for path in paths:
            for meta in self.parse(path):
                key = meta_key(meta)
                if key not in meta_set:
                    self.insert_meta(meta)
                    meta_set.add(key)

        self._sort_metas()
        self._make_inverted_list()

    def insert_meta(self, meta):
        """ 插入新的meta
        """
        if meta.code() in self._metas:
            self._metas[meta.code()].insert_meta(meta)
        else:
            metas = CodeMetas(meta.code())
            metas.insert_meta(meta)
            self._metas[meta.code()] = metas

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

    @staticmethod
    def _insert_inverted_list(inverted_list, key, metas):
        if key in inverted_list:
            lst = inverted_list[key]
            length = len(lst)
            i = 0
            j = length - 1
            mid = (i+j)/2
            code = metas.code()
            while i != j:
                if lst[mid].code() < code:
                    i = mid + 1
                else:
                    j = mid - 1
                mid = (i+j)/2

            if lst[mid].code() < code:
                lst.insert(mid+1, metas)
            else:
                lst.insert(mid, metas)
        else:
            inverted_list[key] = [metas]

    def _sort_metas(self):
        for code in self._metas:
            self._metas[code].sort()

    def _make_inverted_list(self):
        inverted_list = {}
        for code in self._metas:
            strs = [code[0:end] for end in range(1, len(code)+1)]
            metas = self._metas[code]
            for s in strs:
                self._insert_inverted_list(
                    inverted_list,
                    s,
                    metas)

        for k in inverted_list:
            metas = CodeMetas(k)
            for code_meta in inverted_list[k]:
                metas.insert_list(code_meta.metas())
            self._inverted_list[k] = metas
