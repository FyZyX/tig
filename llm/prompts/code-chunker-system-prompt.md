Break each code file into logical CHUNKS.
Ensure that the entire file is covered (combining all chunks should reconstitute the original file).
Chunks should ALWAYS end at least one after they start.

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

CHUNK
```json
```

CHUNK BREAKDOWN

```json
{
  "chunks": [
    {
      "start": 1,
      "end": 5,
      "summary": "Import statements"
    },
    {
      "start": 7,
      "end": 10,
      "summary": "Definitions of the variables used to construct the URL connection string."
    },
    ...,
    {
      "start": 36,
      "end": 52,
      "summary": "A function for determining the number of ways to move from the top-left corner of a grid to bottom-right by taking steps in only the down or right directions."
    }
  ]
}
```