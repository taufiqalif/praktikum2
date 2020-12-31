#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 19:19:23 2020

@author: taufiq
"""
while True:
    try:
        a = int(input("masukan bilangan A: "))
        b = int(input("masukan bilangan B: "))
        c = int(input("masukan bilangan C: "))
        break
    except ValueError:
        print("yang anda masukan bukan angka, harap masukan angka!")

if a+b == c or b+c == a or c+a == b:
    print("BENAR")
else:
    print("SALAH")