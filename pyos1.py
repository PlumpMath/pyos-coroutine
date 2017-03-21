#! /usr/local/bin/python
# -*- coding: utf-8 -*-


class Task(object):
    taskid = 0

    def __init__(self, target):
        Task.taskid += 1
        self.tid = Task.taskid  # Task ID
        self.target = target    # Target coroutine
        self.sendval = None     # Value to send

    def run(self):
        return self.target.send(self.sendval)


if __name__ == "__main__":
    def foo():
        print "Part 1"
        yield
        print "Part 2"
        yield
    t1 = Task(foo())
    t1.run()
    t1.run()
