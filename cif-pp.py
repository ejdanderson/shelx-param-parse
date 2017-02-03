import re
import numpy
import sys

# Minimal arguments
if len(sys.argv) > 1 :
    i = open(sys.argv[1])
else :
    i = open('data/shelxl.cif')

if len(sys.argv) > 2 :
    o = open(sys.argv[2], 'w')
else :
    o = open('data/shelxl.csv', 'w')


def cifpp_main():
    regexpat = '[a-zA-Z0-9\.]+'
    lines = i.readlines()
    lbreak = False

    for index, line in enumerate(lines):
        if re.match('^ _atom_site_disorder_group', line):
            lbreak = True;
            sc_index = index + 1
            curline = lines[sc_index]
            while not curline.isspace() :
                line_arr = curline.split();
                # site, el, x,y,z,Ueq, "Uani", SOF
                # Y1 Yb 0.30069(9) 0.40234(7) 0.49639(7) 0.0145(2) Uani 0.563(5) 1 d . . . . .
                o.write
                o.write(line_arr[0] + ','  + '\n')
                o.write('x,' + line_arr[2] + '\n')
                o.write('y,' + line_arr[3] + '\n')
                o.write('z,' + line_arr[4] + '\n')
                o.write('Ueq,' + line_arr[5] + '\n')
                o.write('SOF,' + line_arr[7] + '\n')
                o.write('\n');
                sc_index += 1
                curline = lines[sc_index]

        if lbreak :
            break

cifpp_main()
