#!/usr/bin/python
# -*- coding: utf-8 -*-)

import os
import sys
import shutil

def batch_rename(path):
    for file in os.listdir(path):
        full = os.path.join(path, file)
        if os.path.isdir(full):
            batch_rename(full)
            print 'dir:',full
        else:
            print 'file:',full
            pos = full.find("╚¤╣·╤▌╥х_╡┌")
            pos += len("╚¤╣·╤▌╥х_╡┌")
            index = full[pos:pos+2]
            print 'pos:', pos, ' index:',index
            new = str(index) + "_The.Three.Kingdoms.srt"
            #shutil.copyfile(full, path+"/"+new)
            shutil.copyfile(full, new)


if __name__ == '__main__':
    if( len(sys.argv) > 1 ):
        batch_rename(sys.argv[1])
