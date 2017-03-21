#! /usr/local/bin/python
# -*- coding: utf-8 -*-

from pyos2 import *


if __name__ == "__main__":
    def foo():
        for i in xrange(5):
            print "I'm foo"
            yield

    def bar():
        while True:
            print "I'm bar"
            yield

    sched = Scheduler()
    sched.new(foo())
    sched.new(bar())
    sched.mainloop()
