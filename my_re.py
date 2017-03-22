#!/usr/bin/python
# -*- coding:utf8 -*-

import re
import os, sys

if __name__ == '__main__':
    my_str = raw_input('Input a string:')

    re_str = r'.*?(\w+@\w+\.com)'
    pattern = re.compile(re_str, re.VERBOSE|re.IGNORECASE|re.DOTALL)
    print '---------------match'
    ret = pattern.match(my_str)
    if ret:
        print '>>>>>>group'
        data = ret.group()
        print data

        print '>>>>>>groups'
        data = ret.groups()
        print data
    else:
        print 'not matched'

    print ''
    print '---------------findall'
    ret = pattern.findall(my_str)
    print ret

    print ''
    print '---------------search'
    ret = pattern.search(my_str)
    if ret:
        print '>>>>>>group'
        data = ret.group()
        # for tmp in data:
        #     print tmp
        print data
        print '>>>>>>groups'
        data = ret.groups()
        print data

    print ''
    print '----------------sub'
    # ret = re.sub(pattern.match(my_str).groups()[0], 'hah', my_str)
    # print ret
    
    re_str = r'(\w+@\w+\.com)'
    pattern = re.compile(re_str, re.VERBOSE|re.IGNORECASE|re.DOTALL)
    
    print '>>>>>>subn'
    ret = re.subn(pattern, '^_^', my_str)    #此处的替换不是在原字符串中替换，而是拷贝了再替换，然后返回替换后的结果
    print ret
    
    print '>>>>>>sub'
    ret = pattern.sub('^_^', my_str)
    print ret

    print ''
    print '----------------split'
    ret = re.split("/", my_str)
    print ret