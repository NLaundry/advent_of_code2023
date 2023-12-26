
## Possible Bugs

- currently collision detection is returning too many values? Apparently ...
- works on example input but not test input

- could be something weird to do with ranges -> I am including values that might not be valid such as x_coord -1, y_coord -1, and greater than max by 1 
    - I don't see what that would do though. There aren't going to be any symbols in those ranges.
- I've also filtered for the weird chance that INSIDE a part number there is a symbol so even when y==y', I'm allowing for x inside range, not just on the edges

- could be the regex

.....
.235.
.....

### Solution 
match.end() grabs the index of the character AFTER the end of the match, not the index of the final character of the match. ... read the docs type beat.

replaced match.end() with match.end() - 1

It's always a damn off by one error

## Things I learned

### match.end() 

match.end() grabs the index of the character AFTER the end of the match, not the index of the final character of the match. ... read the docs type beat.

replaced match.end() with match.end() - 1

It's always a damn off by one error


### Python ranges exclude the largest value

range(5,10) = [5,6,7,8,9] but NOT 10

### pattern_not_period = r"[!#$%&'()*+,-/:;<=>?@[\\\]^_`{|}~]"

This pattern doesn't work the way I expect because the '-' lists all characters between , and / which includes '.'

Maybe, just always put - at the end of a pattern if required.

## Collision Checking

I want to create a collision detection algorithm for part numbers.

I need to get all symbols that are 
y-1
y
y+1
with x value between x_left -1 and x_right +1

essentially a bounding box around the part number

for each line y index
    if contains no parts
        return
    else:
        - symbols_list = so, I can grab all symbols in [y-1, y, y+1] and put them in a list together
        for part in parts
            - filter for all elements with x_coord in range of the part

This should work except for things that go beyond the max X, min Y, max Y, and min X - it'll create a wraparound I think cause of the way python indexing works.

A simpler algorithm is to implement "has_collision" for each part
- then have it loop through each symbol
- way less efficient
- not true, I could still grab the relevant symbols via filter by y_coord
- then filter by X

I like this better

so we pass the symbols list to the "has_collision function"


