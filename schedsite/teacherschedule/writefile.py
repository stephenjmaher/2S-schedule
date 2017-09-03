DAYSELECT = 'day_select'
DUTYSELECT = 'duty_select'
DAYSOFWEEK = {'monday': '0', 'tuesday': '1', 'wednesday': '2', 'thursday': '3', 'friday': '4'}
NUMDAYS = 5


''' writes the input data to a file that is collected via the web app
'''
def writeCollectedData(inputdata):
    outfilename = "./TeacherScheduling.in"
    outfile = open(outfilename, 'w')

    dayselect = []
    for i in range(NUMDAYS):
        dayselect.append([])
    dutyselect = []

    numstaff = 0
    numduties = 0

    # printing the teacher work days to file
    for key in inputdata.keys():
        datalist = key.split('_')
        print inputdata[key]
        if key.startswith(DAYSELECT):
            daynum = int(datalist[-1])
            numdays = len(inputdata[key])

            for i in range(numdays):
                dayselect[daynum].append(int(DAYSOFWEEK[inputdata[key][i]]))
            print dayselect

        if key.startswith(DUTYSELECT):
            staffnum = int(datalist[-2])
            dutynum = int(datalist[-1])

            if numstaff < staffnum + 1:
                for i in range(staffnum - numstaff + 1):
                    dutyselect.append({})
                numstaff = staffnum + 1

            numduties = max(numduties, dutynum + 1)

            dutyselect[staffnum]['duty_' + str(dutynum)] = inputdata[key]
            print dutyselect, dutynum

    print dayselect
    print dutyselect







