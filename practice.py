

def checkReporting( employee, reporting, reportingDict, empdict ):

	if empdict.has_key(reporting):

		for subreporting in empdict[reporting]:
			if subreporting not in empdict[employee]:
				reportingDict[employee].append(subreporting)

			if empdict.has_key(subreporting):
				checkReporting(employee, subreporting, reportingDict, empdict)
	else:
		if reporting not in empdict[employee]:
			reportingDict[employee].append(reporting)


empdict = {
	1: [2, 3, 4], 
	3: [5, 6, 7], 
	5: [8, 9, 10]
}

reportingDict = {}

for key in empdict:
	reportingDict.update({key: []})	


for values in empdict.values():
	for key in values:
		if key not in reportingDict:
			reportingDict.update({key:[]})

print reportingDict


for employee in empdict:
	for reporting in empdict[employee]:
		if reporting not in reportingDict[employee]:
			reportingDict[employee].append(reporting)

		checkReporting(employee, reporting, reportingDict, empdict)

print reportingDict


