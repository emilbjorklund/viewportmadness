import csv

devicefile = 'device-data.csv'
cssfile = 'viewportmadness.css'

widthDict = {}

"""
for row in deviceData:
    print row
"""


def descr_joiner(row, format):
    return ', '.join((row[0], row[1], row[2], format))


def loop_and_pick(idx, format, target):
    deviceData = csv.reader(open(devicefile))
    for row in deviceData:
        # get a normalized ref to the width number
        width = str(row[idx]).strip().split(' ')[0]
        print width

        if (width != format) or (width != 'NA'):  # skip the header line and NA-lines
            try:
                width = int(width)
                if width not in target:  # New entry, create object in deviceData:
                    # print "New width: %s" % row[idx]
                    target[width] = {
                        'devices': [descr_joiner(row, format)]  # add the device specific names as a string
                    }
                else:  # Already has that measurement, just append to list of devices.
                    # print "Already have that one!"
                    target[width]['devices'].append(descr_joiner(row, format))
            except ValueError:
                pass
        else:
            pass
            # print "This line is a goner."
    return target

loop_and_pick(3, 'Portrait', widthDict)
print 'Loop again, adding Landscape'
loop_and_pick(4, 'Landscape', widthDict)


with open(cssfile, 'w') as f:

    for item in sorted(widthDict.iterkeys()):
        lines = [
            '/* %s */\n' % ("; ".join(widthDict[item]['devices'])),
            '@media screen and (min-width: %spx) {\n' % item,
            '    /* stuff for %s and up */\n' % item,
            '}\n\n',
        ]
        f.writelines(lines)
