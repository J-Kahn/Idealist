import idealist as ida

newlist = ida.idea_list()
x1 = ida.idea("protestantism")
x1.name = "The Protestant Ethic and the Spirit of Capitalism"
x1.change_status("backburner")
x1.add_note("Correlation not the same as causation.")
x1.add_note("Policy relevance?")
x1.description = "Depressing puritan ethics encourage harder work -> higher growth."
x1.add_source("Max Weber may have written something about this...")

newlist.add_idea(x1)
newlist["protestantism"]
print newlist["protestantism"]

x1 = ida.idea("badnewsbears")
x1.name = "How bad can the Bears season get?"
x1.change_status("new")
x1.description = "Hypothesize on the exact depths to which the Bears can sink this season."
x1.add_note("Seems like it could be pretty bad.")
x1.add_source("Cutler, 2014 'Apologia'")

newlist.add_idea(x1)
newlist.save("examplelist.ida")

newerlist = ida.idea_list()
newerlist.load("examplelist.ida")

print newlist

newerlist["protestantism"].print_bib()
newerlist["protestantism"].print_notes()

newerlist.print_ifstatus("new")

newerlist.print_long("longlist.txt")