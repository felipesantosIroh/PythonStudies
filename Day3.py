#!/bin/python3

import math
import os
import random
import re
import sys


def IsWeird (a):
	if((a % 2) != 0): 
		print("Weird")
	elif(((a % 2) == 0) and (2 < a < 5)):
		print("Not Weird")
	elif(((a % 2) == 0) and (6 < a < 20)):
		print("Weird")
	elif(((a % 2) == 0) and (20 < a)):
		print("Not Weird")

a = int(input())
IsWeird(a)