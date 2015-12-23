import sys
import re
import random

guestNames = "guests.txt"
scriptName = sys.argv[1]
outputName = "NamesAdded.txt"
nameRE = "\[name([0-9]+)\]"
pageRE = "#PAGE_[A-Z][0-9]+"
page2number = {}

guests = []

with open(guestNames, "r") as guestFile:
  for line in guestFile:
    guests.append(line.strip())

random.shuffle(guests)

namePattern = re.compile(nameRE)
pagePattern = re.compile(pageRE)

with open(scriptName, "r") as readFile:
  with open(outputName, "w") as outputFile:
    pageCount = 1
    for line in readFile:
      pageId =  pagePattern.search(line)

      if pageId:
        if pageId.group(0) not in page2number.keys():
          page2number[pageId.group(0)] = pageCount
          pageCount += 1
        line = line.replace(pageId.group(0), "Page " + str(page2number[pageId.group(0)]))
      hits =  namePattern.search(line)
      if hits:
        index = int(hits.group(1)) - 1
        if(index < len(guests)):
          exactId = "[name" + hits.group(1) + "]"
          outputFile.write(line.replace(exactId, guests[index]))
        else:
          outputFile.write(line.replace(exactId, "Bill"))
      else:
        outputFile.write(line)
