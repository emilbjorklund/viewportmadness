import csv

deviceData = csv.reader(open('device-data.csv'))

widthDict = {}

print "Hello!"
"""
for row in deviceData:
    print row
"""


def descr_joiner(row, format):
    return '; '.join((row[0], row[1], row[2], format))


def loop_and_pick(idx, format, target):
    for row in deviceData:

        if (row[idx] != format.strip()) or (row[idx].strip() != 'NA'):  # skip the header line and NA-lines
            if row[idx] not in target:  # New entry, create object in deviceData:
                # print "New width: %s" % row[idx]
                target[row[idx]] = {
                    'devices': [descr_joiner(row, format)]  # add the device specific names as a string
                }
            else:  # Already has that measurement, just append to list of devices.
                # print "Already have that one!"
                target[row[idx]]['devices'].append(descr_joiner(row, format))
        else:
            pass
            # print "This line is a goner."


loop_and_pick(3, 'Portrait', widthDict)
loop_and_pick(4, 'Landscape', widthDict)


with open('viewportmadness.css', 'w') as f:

    for item in sorted(widthDict.iterkeys()):
        lines = [
            '/* %s */\n' % (", ".join(widthDict[item]['devices'])),
            '@media screen and (min-width: %spx) {\n' % item,
            '    /* stuff for %s and up */\n' % item,
            '}\n\n',
        ]
        f.writelines(lines)
