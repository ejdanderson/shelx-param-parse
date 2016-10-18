import re
import numpy
import sys

# Minimal arguments
if len(sys.argv) > 1 :
    i = open(sys.argv[1])
else :
    i = open('shelxl.lst')

if len(sys.argv) > 2 :
    o = open(sys.argv[2], 'w')
else :
    o = open('shelxl.csv', 'w')

# x y z sof U11 U22 U33 U23 U13 U12 Ueq

def spp_calc_param_string(val, error) :
    val = float(val)
    m = re.search('[^0\.]', error)
    if m != None :
        error_pos = m.start()
        error = float(error)
        # Native round doesnt work properly
        error = numpy.round(error, error_pos-1)
        m = re.search('[^0\.]', str(error))
        str_format = '%0.' + str(error_pos-1) + 'f(%s)'
        return str_format % (numpy.round(val, error_pos-1), m.group())
    return '%0.1f ' % val


def spp_main():
    regexpat = '[a-zA-Z0-9\.]+'
    lines = i.readlines()

    for index, line in enumerate(lines):
        if re.match('^ ATOM', line):
            prevline = line
            curline = line
            sc_index = index
            while not (prevline.isspace() and curline.isspace()) :
                sc_index += 1
                prevline = curline
                curline = lines[sc_index]
                if not curline.isspace() and not re.match('^  ', curline):
                    nextline = lines[sc_index+1]
                    m1 = re.findall(regexpat, curline)
                    m2 = re.findall(regexpat, nextline)

                    o.write(m1[0] + ','  + '\n')
                    o.write('x,' + calcSFACString(m1[1], m2[1]) + '\n')
                    o.write('y,' + calcSFACString(m1[2], m2[2]) + '\n')
                    o.write('z,' + calcSFACString(m1[3], m2[3]) + '\n')
                    o.write('SOF,' + calcSFACString(m1[4], m2[4]) + '\n')
                    o.write('\n');

                    spp_calc_param_string(m1[4], m2[4])
                    # Skip next line, already processed
                    sc_index += 1
spp_main()
