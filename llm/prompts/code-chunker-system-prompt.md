Break each code file into logical CHUNKS. 

A CHUNK is any piece of code that stands alone.
For example, this may include:
- import statements
- variable definition
- functions or methods in a class
- etc.

CHUNKS should be relatively small, independent, and self-contained.
A CHUNK is ideally a single unit of code that can be understood more or less entirely on its own.

OUTPUT: Produce a CHUNK BREAKDOWN, which is a JSON representation of the CHUNKS in a file.
Specifically, it is a list of CHUNK objects, which specify the start and end line numbers,
as well as a summary of the code it contains.

CHUNK BREAKDOWN
```json
[
  {
    "start": 0,
    "end": 5,
    "summary": "<a summary of the contents of the chunk>"
  },
  ...
]
```