#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 12:23:20 2017

@author: nikilreddymamilla
"""

def gcd_rec(m,n):
    if(n):
        return gcd_rec(n,m%n)
    else:
        return m
    
def gcd(M,N):
    m=max(M,N)
    n=min(M,N)
    while(n != 0):
        r=m%n
        m=n
        n=r
    return m