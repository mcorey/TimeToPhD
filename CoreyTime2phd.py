#!/usr/bin/python
#Python Script to estimate time to PhD

basetime = 0			#Time in months
phd_components = {}		#Dictionary for future use

#Make function here to ask questions and then take in answers
#in dictionary Q&A
#Feed in one dictionary, replace dictionaries with responses
#e.g. take pair ({yearsCoursework:"How Many Years Coursework?,#months,"})
#Ask question key(list[0]), append to "num"+str(key)
#run test calculation
#if exception, ask again 
#otherwise, calculate number of months

#Input: 
yearsCoursework = raw_input("How Many Years of Coursework? ")
basetime += int(yearsCoursework)*6
#phd_components({"coursework":yearsCoursework})

numSoloPapers = raw_input("How many solo papers do you plan to publish in grad school? ")
basetime += int(numSoloPapers)*12
#phd_components({soloPapers:numSoloPapers})

numGroupPapers = raw_input("How many group papers do you plan to publish in grad school? ")
basetime += int(numGroupPapers)*4
#phd_components({groupPapers:numGroupPapers})

numDissChapters = raw_input("How many substantive chapters in your dissertation (do not include intro/conclusion)? ")
basetime += (int(numDissChapters) * 8) - (4*int(numSoloPapers))
#phd_components({dissChapers:numDissChapters})

numKids = raw_input("How many children will you have during your degree (0 if none)? ")
basetime += int(numKids)*6
#phd_components({kids:numKids})

hoursPerWeek = raw_input("How many hours a week do you plan to work on your PhD? ")
weeksVacation= raw_input("How many weeks per year do you plan to take off for vacation/sick days? ")
hoursPerYear = int(hoursPerWeek) * (52-int(weeksVacation))


timeToFinish =( (basetime/12)* ((40*52)/ float(hoursPerYear)) )
#months/12 = yearsOfWork * [40hrs*50 weeks / hoursWorkedPerYear] -->(factor for ideal hours / your hours )

valid = False
while valid == False:
	money2spare = raw_input("Do you enough money you'll never have to work? (yes/no)")
	money2spare = money2spare.lower()
	if money2spare == "y" or money2spare == "yes":
		timeToFinish -= timeToFinish*.10
		valid = True
	elif money2spare == "n" or money2spare == "no":
		timeToFinish = timeToFinish
		valid = True
	else:
		print "Please Try Again..."
		valid = False

#print basetime
#print hoursPerYear
#print timeToFinish
print "Your time to finish should be " + str(timeToFinish) + " years!"

