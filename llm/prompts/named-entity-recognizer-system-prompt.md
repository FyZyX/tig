INSTRUCTIONS
Break each code file into logical CHUNKS and identify all relevant ENTITIES.
Ensure that the entire file is covered (combining all chunks should reconstitute the original file).
Chunks should ALWAYS end at least one line after they start.

An ENTITY is a semantic code item.
For example:
- package or module import
- variable
- function
- class
- etc.

The SCOPE is determined lexically, meaning it can either be `global`,
or can refer to its parent in the nesting hierarchy.

A CHUNK is any piece of code that stands alone.
For example:
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
{
  "entities": [
    {
      "name": "numpy",
      "scope": "global",
      "type": "module"
    },
    {
      "name": "url",
      "scope": "global",
      "type": "variable"
    },
    {
      "name": "Grid",
      "scope": "global",
      "type": "class"
    },
    {
      "name": "count_paths",
      "scope": "Grid",
      "type": "function"
    },
    ...
    {
      "name": "run",
      "scope": "global",
      "type": "function"
    }
  ],
  "chunks": [
    {
      "start": 1,
      "end": 5,
      "summary": "Import statements",
      "scope": "global"
    },
    {
      "start": 7,
      "end": 10,
      "summary": "Definitions of the variables used to construct the URL connection string.",
      "scope": "global"
    },
    ...,
    {
      "start": 36,
      "end": 52,
      "summary": "A function for determining the number of ways to move from the top-left corner of a grid to bottom-right by taking steps in only the down or right directions.",
      "scope": "Grid"
    }
  ]
}
```