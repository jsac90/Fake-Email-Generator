import random
import string
import csv
import progressbar

'''
Asks user for how many fake emails they want generated. Must be Integer. Duh.
If not an integer, keeps recursively cycling back until it gets an integer. 
'''
def getcount():
	rownums = input("How many fake email addresses?: ")
	try:
		rowint = int(rownums)
		return rowint
	except ValueError:
		print ("Please enter an integer value")
		return getcount()

'''
Creates a random string of digits between 1 and 20 characters alphanumeric and adds it to a fake domain and fake extension
Most of these emails are completely bogus (eg - gmail.gov) but will meet formatting requirements for my purposes
'''
def makeEmail():
	extensions = ['com','net','org','gov']
	domains = ['gmail','yahoo','comcast','verizon','charter','hotmail','outlook','frontier']

	winext = extensions[random.randint(0,len(extensions)-1)]
	windom = domains[random.randint(0,len(domains)-1)]

	acclen = random.randint(1,20)

	winacc = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(acclen))

	finale = winacc + "@" + windom + "." + winext
	return finale

#save count to var
howmany = getcount()

#counter for While loop
counter = 0

#empty array for loop
emailarray = []

#uses counter to figure out how many emails to keep making

print ("Creating email addresses...")
print ("Progress: ")

prebar = progressbar.ProgressBar(maxval=int(howmany))

for i in prebar(range(howmany)):
	while counter <= howmany:
		emailarray.append(str(makeEmail()))
		counter = counter+1
		prebar.update(i)
	
print ("Creation completed.")

#user input for filename. Can even take in a file path, pending you have permission to write there
filename = input("name your file: ")

'''
Acutally writes to file here.
uses WA which will write and append the file. If the file doesn't exist, this will create it. 
Will write email addresses to array one per row which is why the array is important. 
Once complete, will close the file. 
'''
print ("Progress: ")

bar = progressbar.ProgressBar(maxval=int(howmany))
	
emailfile = open(str(filename), 'w')
aa = csv.writer(emailfile)
for emailaddr in bar(emailarray):
	aa.writerow([emailaddr])
	bar.update()
emailfile.close()

print ("File '" + filename + "' created.")
