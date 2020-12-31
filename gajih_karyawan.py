#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 19:06:56 2020

@author: taufiq
"""
while True:
    try:
        gaji = int(input("masukan gaji: "))
        berkeluarga = (False, True)[input("sudah berkeluarga? (Y/T)") =="Yy"]
        punya_rumah = (False, True)[input("punya rumah (Y/T)") == "Yy"]
        break
    except ValueError:
        print("yang anda masukan bukan angka, harap masukan angka!")

if gaji > 300000000:
    print("gaji sudah diatas UMR")
    if berkeluarga:
        print("wajib ikut asuransi dan menabung untuk pensiun")
    else:
        print("tidak perlu ikut asuransi")
    
    if punya_rumah:
        print("wajib bayar rumah")
    else:
        print("tidak wajib bayar pajak")
else:
    print("gaji belum UMR")