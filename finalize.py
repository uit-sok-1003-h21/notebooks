#!/usr/bin/python
# -*- coding: UTF-8 -*-

import nbformat as nbf
import nbconvert as nb
import os
import re
from matplotlib import pyplot as plt



def main():    
    for file in os.listdir():
        fname = os.fsdecode(file)
        print(f"nummerates {fname}")
        if fname.endswith(".ipynb"): 
            convert(fname)
            recount_and_replace(fname,'#### Eksempel')
            recount_and_replace(fname,'#### Oppgave')
            

def recount_and_replace(fname,what):
    if len(what.split(' '))!=2 or not ('#' in what):
        raise RuntimeError(f'what needs to be on the form "#### word", not {what}')
    f=open(fname)
    s=f.read()
    i=1
    n=0
    while True:
        m=re.search(what+' (\d+)',s[n:])
        if m is None:
            break
        old=s[m.start()+n:m.end()+n]
        new=f'{what} {i}'
        s=s[:m.start()+n]+new+s[m.end()+n:]
        s=replace_references(s, old, new)
        n+=m.end()
        i+=1
    f.close()
    if i>1:
        f=open(fname,'w',newline='')
        f.write(s)        
        f.close()

        
def replace_references(s,old,new):
    n=0
    old=old[old.find(' ')+1:]
    new=new[new.find(' ')+1:]
    if old==new:
        return s
    while True:
        m=re.search(f"\\w*(?<!#### ){old}",s[n:])
        if m is None:
            break
        s=s[:m.start()+n]+new+s[m.end()+n:]
        n+=m.end()
    return s


def convert(file):
    html,res=nb.HTMLExporter(template_name='Classic').from_filename(file)
    html=html.replace('.ipynb">','.html">')
    f=open(file.replace('.ipynb','.html'),'w',encoding="utf-8")
    f.write(html)
    f.close()


main()