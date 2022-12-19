# Note Outline

This command line tool will help split one note to many in your zettelkasten. 

It will split out the parts between the `===` characters into their own note.

- 202211251217 Main Note.md
```
# [[202211251217]] Main Note

===
# [[202211250910]] First Note

My first note.    
===
===
# [[202211251045]] Second Note

My second note.    
===
===
# [[202211251152]] Third Note

And finally, this is my third note.    
===
```

This will create the following three notes.

- 202211250910 First Note.md
```
# [[202211250910]] First Note

My first note.
```

- 202211251045 Second Note.md
```
# [[202211251045]] Second Note

My second note.
```

- 202211251152 Third Note.md
```
# [[202211251152]] Third Note

And finally, this is my third note.
```

## Basic Use

To split the note to the many notes run:

`note_split note.md`

To see a dry run and output the results to the terminal run:

`note_split note.md -d`

## Installation

Download this repo and open it in the terminal and run:

`pip3 install .`
