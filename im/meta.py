#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Meta(object):
    """
    码表词
    """

    def __init__(self, code, word, priority=10000):
        """
        code: 码
        word: 对应的词
        priority: 这个词所在同码中的优先级
        """
        self._code = code.strip()
        self._word = word.strip()
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

    def __lt__(self, other):
        return self.__cmp__(other) < 0

    def __le__(self, other):
        return self.__cmp__(other) <= 0

    def __eq__(self, other):
        return self._code == other._code and \
            self._word == other._word and  \
            self._priority == other._priority

    def __str__(self):
        return "<%s,%s,%d>" % (self._code, self._word, self._priority)


class KeyMetas(object):
    """
    每个代码对应的meta列表
    """
    def __init__(self, key):
        self._key = key
        self._metas = None

    def _find_insert(self, meta):
        assert self._metas is not None
        length = len(self._metas)
        i = 0
        j = length - 1
        mid = (i+j)//2
        while i < j:
            if self._metas[mid] < meta:
                i = mid + 1
            else:
                j = mid

            mid = (i + j) // 2

        if self._metas[mid] < meta:
            self._metas.insert(mid+1, meta)
        else:
            self._metas.insert(mid, meta)

    def insert(self, meta):
        """找到合适的位置进行插入
        合适的位置定义为
        代码字典序越小，则排在前面
        代码相同，则priority的小在前面
        priority相同，则先插入的在前面

        :meta: 需要插入的元素
        """
        if not self._metas:
            self._metas = [meta]
        else:
            self._find_insert(meta)

    def key(self):
        return self._key

    def metas(self):
        return self._metas

    def len(self):
        return len(self._metas)

    def __str__(self):
        result = '<%s,' % self._key
        for meta in self._metas:
            result += str(meta) + ','
            result[-1] = '>'
            return result

    def __eq__(self, other):
        return self._key == other._key and self._metas == other._metas
