#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Parser(object):
    """
    码表解释器
    """

    def __init__(self):
        self._metas = {}

    def parse(self, path):
        raise NotImplementedError

    def insert_meta(self, meta):
        """ 插入新的meta
        """
        if meta.code() in self._metas:
            self._metas[meta.code()].append(meta)
        else:
            self._metas[meta.code()] = [meta]

    def _fuzzy_words(self, code, begin, count):
        prefix_matchs = [(k, m) for k, m in self._metas
                         if k != code and k.startwith(code)]
        prefix_matchs.sort(lambda l, r: l[0] < r[0]
                           if len(l[0]) == len(r[0])
                           else len(l[0]) < len(r[0]))
        result = []
        for (_, metas) in prefix_matchs:
            for meta in metas:
                if begin > 0:
                    begin -= 1
                    continue
                result.append(meta)
                if len(result) >= count:
                    return result
        return result

    def get_words(self, code, begin, count, perfect_match=False):
        """根据code查找匹配的词

        :code: 用户输入的code
        :begin: 开始的位置
        :count: 返回的个数
        :perfect_match: 完美匹配，如果为true，则要与code完全匹配才能匹配中，否则以code为前缀匹配
        :returns: ([metas], has_more)
        """
        metas = self._metas.get(code, [])
        has_more = begin + count < len(metas)
        result = ([], False) if has_more else \
            (metas[begin:begin + count], has_more)
        if perfect_match or len(result[0]) >= count:
            return result
        fuzzy_count = count - len(result)
        fuzzy_begin = begin - len(metas)
        return result + self._fuzzy_words(code, fuzzy_begin, fuzzy_count)

    @staticmethod
    def sort_metas(func):
        def sorter_parser(self, path):
            func(self, path)
            for code, meta in self._metas:
                meta.sort()
            return func
