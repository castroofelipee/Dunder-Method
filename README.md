# Dunder-Method


## What “dunder methods” are

In Python, some behavior looks like it’s built into the language:

- `len(something)`
- `print(something)`
- `something1 + something2`
- `something in collection`
- `for item in something:`

What’s really happening is: Python tries to call a special method on your object.
Those special methods have names like `__len__` or `__add__`.

People call them “dunder methods” because they use **double underscores** (dunder = double underscore).


## Why you’d use them

Dunder methods let your own classes feel like “real” Python objects.
Instead of writing `playlist.length()` or `money.add(other)`, you can support the normal Python syntax.

Some common ones:

- `__init__`: how the object is created
- `__repr__`: developer-friendly string (useful in debugging)
- `__str__`: user-friendly string (what `print()` shows)
- `__len__`: makes `len(obj)` work
- `__iter__`: makes `for x in obj` work
- `__contains__`: makes `x in obj` work
- `__getitem__`: lets you do `obj[i]`
- `__add__`: lets you do `a + b`
- `__lt__` (and friends): comparisons like `<`, `>`, etc.
- `__enter__` / `__exit__`: context managers


## Code example

This repo includes a small script: `dunder_examples.py`.
It shows a few classes:

- `Money`: custom printing, addition, and comparison
- `Playlist`: length, iteration, indexing, and membership checks
- `Timer`: a context manager used with `with ...:`
