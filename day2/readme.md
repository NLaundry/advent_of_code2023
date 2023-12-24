# Part 2


# Part 1

## What I learned

### Named Tuples and Data classes

- nice, clean easy way to get something typed-ish like a struct without writing a full class.
- 

### Generator expressions

similar to but different from list comprehensions

generator expression syntax 
```python
(expression for item in iterable if condition)
```

List comprehensions
```python
[ expression for item in iterable if condition ]
```
#### Key Differences:
Memory Usage: List comprehensions build the entire list in memory, while generator expressions yield items one at a time, consuming less memory for large datasets.
Return Type: List comprehensions return a list, whereas generator expressions return a generator object.
Use Case: Use list comprehensions when you need to access the elements directly and repeatedly. Use generator expressions when dealing with large data sets where you want to process items one at a time or when you want to iterate over the results once.

### You can create a list of boolean checks

return all([ a < b, a < c, ..])

### getattr

dynamically get at attribute of an object

```python
@dataclass
class Round:
    red: int = 0
    green: int = 0
    blue: int = 0

bob = Round()
getattr(bob, 'red')
```



## Notes

- cubes: r, g, b
- secret number of cubes of each colour
- Goal: figure out info about the number of cubes
- Input: elf gets handfuls of random cubes, shows them, puts them back, does N times
- play several games - probably each line

which games are possible given x red, y green, z blue
- sum the IDs of the possible games




### How would I do this?

do you want a nice clean implementation or to try to one line this?
- let's build it nicely

#### structures

- Game class: list[RoundData], ID: int
- round class: tuple [int, int, int] (red, green, blue) - or I do red, green, blue as actual class values
    - tuple is probably faster but less descriptive
    - class is probably less performant. meh, who cares.

#### Parsing

- 1 indexed, can probably expect that line # = ID # (part 2 may change this)
- remove "Game #: " from the start of the line. (that should be regexable?)
- read till semi colon (I think you can split by semicolon) - note that the last round is not stopped by a semi colon
- can't rely on the order OR always having all of red, green, blue present. 
    - So you do need some sort of conditional checking (match)

#### Check possibility

- create "max_game" of type Game and compare to each game (easy map )
    - just to learn more python, can you create a comparison method? less than?
    - yeah let's do that - optimize for learning

#### Sum IDs

- reduce for summing IDs




## Problem Description
--- Day 2: Cube Conundrum ---

You're launched high into the atmosphere! The apex of your trajectory just barely reaches the surface of a large island floating in the sky. You gently land in a fluffy pile of leaves. It's quite cold, but you don't see much snow. An Elf runs over to greet you.

The Elf explains that you've arrived at Snow Island and apologizes for the lack of snow. He'll be happy to explain the situation, but it's a bit of a walk, so you have some time. They don't get many visitors up here; would you like to play a game in the meantime?

As you walk, the Elf shows you a small bag and some cubes which are either red, green, or blue. Each time you play this game, he will hide a secret number of cubes of each color in the bag, and your goal is to figure out information about the number of cubes.

To get information, once a bag has been loaded with cubes, the Elf will reach into the bag, grab a handful of random cubes, show them to you, and then put them back in the bag. He'll do this a few times per game.

You play several games and record the information from each game (your puzzle input). Each game is listed with its ID number (like the 11 in Game 11: ...) followed by a semicolon-separated list of subsets of cubes that were revealed from the bag (like 3 red, 5 green, 4 blue).

For example, the record of a few games might look like this:

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
In game 1, three sets of cubes are revealed from the bag (and then put back again). The first set is 3 blue cubes and 4 red cubes; the second set is 1 red cube, 2 green cubes, and 6 blue cubes; the third set is only 2 green cubes.

The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

In the example above, games 1, 2, and 5 would have been possible if the bag had been loaded with that configuration. However, game 3 would have been impossible because at one point the Elf showed you 20 red cubes at once; similarly, game 4 would also have been impossible because the Elf showed you 15 blue cubes at once. If you add up the IDs of the games that would have been possible, you get 8.

Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?


