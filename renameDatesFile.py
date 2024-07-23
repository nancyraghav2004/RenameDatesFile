# Peoject :- Renaming Files With American-Style Dates to European-Style Dates

# American Style :- MM-DD-YYYY
#European Style :- DD-MM-YYYY


#! python3
#renameDates.py - Renames filenames with American MM-DD-YYYY date format
#to EUropean DD-MM-YYYY

import shutil, os, re

#Create a regex that matches files with the American MM-DD-YYYY date format
datePattern = re.compile(r"""^(.?)          #all text before the date
                        ((0|1)?\d)-         #one or two digits for the month
                        ((0|1|2|3)?\d)-     #one or two digits for the days
                        ((19|20)\d\d)       #Four digits for the year
                        (.*?)$              #All text after the date
                        """,re.VERBOSE)

#Loop over the files in the working directory
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

    #Skip files without a date
    if mo == None:
        continue

    #Get the different parts of the filename.
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)


    #Form the European style format

    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    #Get the full, absolute file paths.
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    #rename the files.
    print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
    #shutil.move(amerFilename, euroFilename)  #uncomment after testing





























