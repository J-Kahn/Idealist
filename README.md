Over time, I've gotten into the habit of keeping track of ideas for academic papers, projects, and ultimately the twinkle in my eye that is my dissertation. The problem is, a simple list isn't really helping me. I need to keep track of the idea, whether or not I've rejected it, any progress I've made or thoughts I've had, and any relevant papers associated with the idea. Unsatisfied with the available alternatives, I've written up a super simple python script to track these ideas, available here. (The name "idealist" was actually unintentional)

There are two classes: `idea`s and `idea_list`s. Ideas have an id (which they'll be indexed by in their list), a name, a description, a status, notes and bibliography. All of these are simple strings except for the notes and bibliography, which are lists of strings. Ideas are initialized with their id, and the rest of their aspects can be manipulated through a set of functions I have included or just through manipulating them directly.

Idea_lists are dictionaries of ideas indexed by their id. Printing the id_list will display a numbered list with their name, id and status, after which they can be viewed directly as elements of the id_list. The list can then be saved or loaded, the encoding is pretty basic: Each line contains a separate idea with each field described by `field = {FIELD_TEXT}`. The exception are bibliographies, which are lists of the form `[FIELD_ONE && FIELD_TWO && FIELD THREE && ... ]`. Right now all fields must be entered, I will fix this at some point.

Example usage:

```
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
```
*Update: 8/9/19 - * I've added a simple script, `add_idea.py` to make adding an idea to an ida file as easy as possible.
