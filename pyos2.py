#! /usr/local/bin/python
# -*- coding: utf-8 -*-

from Queue import Queue
from pyos1 import *


class Scheduler(object):
    def __init__(self):
        self.ready = Queue()
        self.taskmap = {}

    def new(self, target):
        newtask = Task(target)
        self.taskmap[newtask.tid] = newtask
        self.schedule(newtask)
        return newtask.tid

    def schedule(self, task):
        self.ready.put(task)

    def mainloop(self):
        while self.taskmap:
            task = self.ready.get()
            result = task.run()
            self.schedule(task)


if __name__ == "__main__":
    def foo():
        while True:
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
