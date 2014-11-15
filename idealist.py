# Code to implement idea list for dissertations, papers etc.

import os

class idea:
	def __init__(self, id):
		self.id = id
		self.name = ""
		self.description =""
		self.notes = []
		self.bibliography = []
		self.status = "new"

	def add_note(self, note):
		self.notes.append(note)

	def wipe_notes(self):
		self.notes = []

	def add_source(self, source):
		self.bibliography.append(source)

	def wipe_notes(self):
		self.bibliography = []

	def change_status(self, status):
		self.status = status

	def change_description(self, desc):
		self.description = desc

	def print_idea(self, num, l1, l2, l3, l4):
		print "{0:{l1}})   {1:{l2}}    {2:{l3}}   {3:{l4}}".format(num, self.name, self.id,
															self.status, l1=l1, l2=l2, 
															l3=l3, l4=l4)

	def string_rep(self, num, l1, l2, l3, l4):
		return "{0:{l1}})   {1:{l2}}    {2:{l3}}   {3:{l4}}".format(num, self.name, self.id,
															self.status, l1=l1, l2=l2, 
															l3=l3, l4=l4)

	def export(self):
		char_bib =  " && ".join(self.bibliography)
		char_notes =  " && ".join(self.notes)
		return "id = {{{0}}}, name = {{{1}}}, description = {{{2}}}, status = {{{3}}}, notes = {{[{4}]}}, bibliography = {{[{5}]}}".format(self.id, self.name, self.description,
															self.status, char_notes, char_bib)

	def print_bib(self):
		print "\n\n"
		print "Idea: {0}, Tag: {1}".format(self.name, self.id)
		print "\n"
		print "BIBLIOGRAPHY:"
		print "============="
		for i in range(0, len(self.bibliography)):
			print "{0:3}. {1}".format(i+1, self.bibliography[i])
		print "\n\n"


	def print_notes(self):
		print "\n\n"
		print "Idea: {0}, Tag: {1}".format(self.name, self.id)
		print "\n"
		print "NOTES"
		print "====="
		for i in range(0, len(self.notes)):
			print "{0:3}. {1}".format(i+1, self.notes[i])
		print "\n\n"

class idea_list:
	def __init__(self):
		self.master =  {}

	def __repr__(self):
	 	return self.string_rep()

	def __str__(self):
		return self.string_rep()

	def __getitem__(self, arg):
		return self.master[arg]

	def add_idea(self, proj):
		self.master[proj.id] = proj

	def rename(self, name, newname):
		self.master[newname] = self.master[name]
		self.master[newname].id = newname
		del self.master[name]

	def print_full(self):

		# Find lengths for fixed width numbers

		l1 = len(str(len(self.master)+1))
		l2 = max([len(self.master[x].name) for x in self.master])
		l3 = max([len(self.master[x].id) for x in self.master])
		l4 = max([len(self.master[x].status) for x in self.master])
		listmaster = list(self.master)

		for i in range(0, len(self.master)):
			nm = listmaster[i]
			self.master[nm].print_idea(i+1, l1, l2, l3, l4)

	def string_rep(self):

		# Find lengths for fixed width numbers
		ret = ""
		l1 = len(str(len(self.master)+1))
		l2 = max([len(self.master[x].name) for x in self.master])
		l3 = max([len(self.master[x].id) for x in self.master])
		l4 = max([len(self.master[x].status) for x in self.master])
		listmaster = list(self.master)

		for i in range(0, len(self.master)):
			nm = listmaster[i]
			ret = ret + "\n" + self.master[nm].string_rep(i+1, l1, l2, l3, l4)

		return ret

	def print_ifstatus(self, status):

		temp = {item: v for item, v in self.master.iteritems() 
					   if v.status == status}

		l1 = len(str(len(temp)+1))
		l2 = max([len(temp[x].name) for x in temp])
		l3 = max([len(temp[x].id) for x in temp])
		l4 = max([len(temp[x].status) for x in temp])
		listtemp = list(temp)

		for i in range(0, len(temp)):
			nm = listtemp[i]
			temp[nm].print_idea(i+1, l1, l2, l3, l4)		
	
	def eliminate_status(self, status):

		self.master = {item: v for item, v in self.master.iteritems() 
					   if v.status != status}

	def save(self, filename):
		f = open(filename,'w+')
		for i in self.master:
			f.write(self.master[i].export()+"\n")
		f.close()

	def load(self, filename):
		settingre ='\s*=\s*\{(?P<variable>[^\}]*)'
		settingrevect ='\s*=\s*\{\s*\[(?P<variable>[^\]]*)'
		f = open(filename,'r')
		for line in f:

			idsearch = re.search("id" + settingre, line)
			idline = idsearch.group('variable')

			namesearch = re.search("name" + settingre, line)
			nameline = namesearch.group('variable')

			descsearch = re.search("description" + settingre, line)
			descline = descsearch.group('variable')

			statussearch = re.search("status" + settingre, line)
			statusline = statussearch.group('variable')

			statussearch = re.search("status" + settingre, line)
			statusline = statussearch.group('variable')	

			bibsearch = re.search("bibliography" + settingrevect, line)
			bibline = bibsearch.group('variable')
			bibline = bibline.split(" && ")

			notesearch = re.search("notes" + settingrevect, line)
			noteline = notesearch.group('variable')
			noteline = noteline.split(" && ")

			if len(bibline) == 1 and bibline[0] == "":
				bibline = []

			if len(noteline) == 1 and noteline[0] == "":
				noteline = []

			x = idea(idline)
			x.status = statusline
			x.name = nameline
			x.description = descline
			x.bibliography = bibline
			x.notes = noteline

			self.add_idea(x)