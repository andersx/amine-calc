#!/usr/bin/env python2
import sys

def get_xyz_from_header(lines):

    xyz = []

    mode = "search"

    for line in lines:

        if mode == "read":

            tokens = line.split()
            if len(tokens) < 6:
                break
            else: 
                a = tokens[2]
                x = float(tokens[3])
                y = float(tokens[4])
                z = float(tokens[5])

                c = [a, x, y, z]
                xyz.append(c)
        

        if mode == "search":

            if "xyz 0 1" in line:
                mode = "read"
                
    return xyz


def get_xyz_from_cycle(lines):

    xyz = []

    i_cycle = 0
    for i, line in enumerate(lines):
        if "GEOMETRY OPTIMIZATION CYCLE" in line:
            i_cycle = i

    for i, line in enumerate(lines[i_cycle+5:]):
        tokens = line.split()
        if len(tokens) < 4:
            break
        else: 
            a = tokens[0]
            x = float(tokens[1])
            y = float(tokens[2])
            z = float(tokens[3])

            c = [a, x, y, z]
            xyz.append(c)

    return xyz

def log2xyz(logfile):

    f = open(logfile)
    lines = f.readlines()
    f.close()

    n = 0

    for line in lines:
        if "GEOMETRY OPTIMIZATION CYCLE" in line:
            n += 1

    xyz = []

    if n == 1:
        xyz = get_xyz_from_header(lines)

    elif n > 1:
        xyz = get_xyz_from_cycle(lines)
        # xyz = get_xyz_from_header(lines)


    return xyz

if __name__ == "__main__":

    xyz = log2xyz(sys.argv[1])

    print len(xyz)
    print sys.argv[1]
    for c in xyz:

        print "%-2s  %11.6f %11.6f %11.6f" % (c[0], c[1], c[2], c[3])

    
