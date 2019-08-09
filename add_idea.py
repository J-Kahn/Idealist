# Simple interactive script to add ideas to an ida file


from idealist import idealist as ida

# Start with the file to open
file_name = input('Enter ida file name: ')


# Open up the ida file
newlist = ida.idea_list()
newlist.load(file_name)


# Get the idea id
idea_code = input('Enter identifier for new idea: ')
x1 = ida.idea(idea_code)

# Get the idea name
name = input('Enter title for ' + idea_code + ': ')
x1.name = name

# Get the idea status
status = input('Enter status for ' + idea_code + ': ')
x1.status = status

# Get the idea description
descr = input('Enter description for ' + idea_code + ': ')
x1.description = descr

# Do we want to add notes?
add_notes = input('Add notes to ' + idea_code + '? Y/N ')

# There can be multiple notes so we're going to do this as a loop.
if add_notes == 'Y':
	print('When done enter \'q\'')
	done = False
	notes = 0
	while not done:
		notes += 1
		new_note = input('Note ' + str(notes) + ': ')
		if new_note == 'q':
			break
		else:
			x1.add_note(new_note)

# Do we want to add sources?
add_sources = input('Add sources to ' + name + '? Y/N ')

# There can be multiple sources so we're going to do this as a loop
if add_sources == 'Y':
	print('When done enter \'q\'')

	done = False
	sources = 0
	while not done:
		sources += 1
		new_source = input('Source ' + str(sources) + ': ')
		if new_source == 'q':
			break
		else:
			x1.add_source(new_source)

# Optional gut check that the idea looks okay
print_idea = input('Print idea? Y/N ')
if print_idea == 'Y':
	print(x1)

# Now we add it to the list
newlist.add_idea(x1)


# Optional gut check that the ida file looks okay
print_ida = input('Print idealist? Y/N ')
if print_ida == 'Y':
	print(newlist)

# Do we want to save? Currently only doing overwrites of the original idealist.
save_ida = input('Save idealist? Y/N ')
if save_ida == 'Y':
	newlist.save(file_name)