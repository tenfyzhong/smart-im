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
        self.word = word
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
        """TODO: 更新优先级

        :priority: 新的优先级

        """
        self._priority = priority

    def __cmp__(self, other):
        return self.priority.__cmp__(other)
