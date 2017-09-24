#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Meta(object):
    """
    码表词
    """

    def __init__(self, code, word, priority):
        """
        code: 码
        word: 对应的词
        priority: 这个词所在同码中的优先级
        """
        self._code = code
        self._word = word
        self._priority = priority

    def code(self):
        """ 返回当前的码
        :returns: 当前的码
        """
        return self._code

    def word(self):
        """ 当前码对应的词
        :returns: 当前的词
        """
        return self._word

    def priority(self):
        """ 当前的优先级
        :returns: 优先级
        """
        return self._priority

    def set_priority(self, priority):
        """更新优先级
        :priority: 新的优先级
        """
        self._priority = priority

    def __cmp__(self, other):
        """
        大小规则：
        代码越字的在前面
        优先级越小的在前面
        """
        if self._code < other._code:
            return -1
        elif self._code > other._code:
            return 1
        elif self._priority != other._priority:
            return self._priority - other._priority
        else:
            return 0

    def __str__(self):
        return "<%s,%s,%d>" % (self._code, self._word, self._priority)


class CodeMetas(object):
    """
    每个代码对应的meta列表
    """
    def __init__(self, code):
        self._code = code
        self._metas = []

    def insert_meta(self, meta):
        self._metas.append(meta)

    def insert_list(self, metas):
        self._metas += metas

    def sort(self):
        """对metas进行排序
        """
        self._metas.sort(reverse=True)

    def code(self):
        return self._code

    def metas(self):
        return self._metas

    def len(self):
        return len(self._metas)

    def __str__(self):
        result = '<%s,' % self._code
        for meta in self._metas:
            result += str(meta) + ','
        result += '>'
        return result
