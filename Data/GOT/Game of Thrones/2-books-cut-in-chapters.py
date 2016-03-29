#!/usr/bin/python
# -*- coding: utf-8 -*-
# F F machin
# T F  
# T F 
# F T Prologue
# F T
# F F jdjfhf
# F F nehehehe


def cutInChapters(lines, i):
	isNewChapter = False
	oldLine = '1'
	fp = None
	j=0

	for line in lines:
		if len(line) == 1 and len(oldLine) == 1 and not isNewChapter:
			continue

		elif len(line) > 1 and len(oldLine) == 1 and not isNewChapter:
			oldLine = line

		elif len(line) == 1 and len(oldLine) > 1 and not isNewChapter:
			if fp <> None:
				fp.close()
			fp = open('data/GOT' + str(i) + '-' + str(j) + '-' + oldLine.strip() + '.txt','w+')
			j = j+1
			isNewChapter = True
			oldLine = line

		elif len(line) == 1 and len(oldLine) == 1 and isNewChapter:
			continue

		elif len(line) > 1 and len(oldLine) >= 1 and isNewChapter:
			fp.write(line)
			oldLine = line

		elif len(line) == 1 and len(oldLine) > 1 and isNewChapter:
			isNewChapter = False
			oldLine = line
		
	fp.close()



for i in range(1,6):
	with open('books/GOT'+str(i)+'.txt','r') as fp:
		lines = fp.readlines()
	cutInChapters(lines, i)

