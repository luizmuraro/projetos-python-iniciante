#!-*- conding: utf8 -*-
import random

while True:
    for x in range(1):
        print random.randint(1,6)

    resp = raw_input("Voce quer ir de novo? s/n  ")

    if resp == 'n':
        break
