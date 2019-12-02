### Solution 1

`python solution.py`

### Solution 2

Bruteforce method. Uses input.txt and `answer = ...` in code

`python solution_part2_bruteforce.py`

### Debug

For Solution 2 I made a debug output script

`python solution_part2_debug.py`

The debug script outputs all of the operations, but if the parameter is unknown it replaces it with a '?'. Params 1 and 2 are unknown, and if a value is derived from an unknown then it becomes unknown as well.

Some sample output:
```
op=1, pos1=12, pos2=2, ret=3
i[3] = ?: (1 + ?)
op=1, pos1=1, pos2=2, ret=3
i[3] = ?: (? + ?)
op=1, pos1=3, pos2=4, ret=3
i[3] = ?: (? + 1)
op=1, pos1=5, pos2=0, ret=3
i[3] = 2: (1 + 1)
op=2, pos1=13, pos2=1, ret=19
i[19] = ?: (5 * ?)
```

