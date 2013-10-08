#! /usr/bin/env python

def hello():
	print "Hello World!"

def hello2():
	print "You have chosen wisely!"

i = input("Choose (1) or (2): ")
if i == 1:
	hello()
if i == 2:
	hello2()