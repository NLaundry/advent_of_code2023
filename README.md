# advent_of_code2023

## Things I learned

### Python regex library

re.findall is consumptive - meaning it won't find overlaps
- I solved this with a different regex library called ... get this, regex. and then set "overlapping=True"

### Python Maps

Ah, that makes sense! In Python 3, `map()` returns an iterator, which is a lazy sequence. The elements are not actually processed or generated until you iterate over the iterator or convert it to a list with `list()`. This is different from Python 2, where `map()` would directly return a list.

So, when you used `map()` to create `two_digit_nums`, you were creating an iterator, not a list. When you passed this iterator to `reduce()`, if you hadn't iterated through the `map` result or converted it to a list, it might have appeared empty to `reduce()` if it had been already iterated over somewhere else in your code.

By converting the result of `map()` to a list:

```python
two_digit_nums = list(map(...))
```

You force the evaluation of the entire iterator and create a list with all the elements. This ensures that `reduce()` receives an actual list to work with, preventing the error you encountered. It's a good practice to convert `map()` results to lists if you need to use them directly, especially in contexts where an actual list type is expected or needed.
