# Fair-Drafter

This project was created quick and painlessly create a statistically fair draft regardless of player number or amount of rounds.

This can be used for a variety of games or tournaments where there are sequential rounds of picks for various players and absolute fairness is desired.

## Quick Start

Made for people with absolutely no knowledge of how to code or patience the following is instructions on running this program as fast as possible.

* Go [here](https://repl.it/languages/python). This website runs python code you give it and displays the results.

* Click on [drafter.py](https://github.com/Upgwades/Fair-Drafter/blob/master/drafter.py) and copy and paste all the code that is shown.

* Click the run button and follow the on-screen prompts. The result will be a series of statistically fair draft outputs based on the criteria you provided.

## Getting Started

For the code people.

### Prerequisites

The only external dependency is numpy.

```
import numpy as np
```

### Running It

This section will explain the inputs and outputs of running the code.

#### Inputs

Firstly a comma sepparated list of players is requested. Do not include spaces or anything else as error checking was not implemented.

```
Enter player names separated with commans and no spaces: will,frank,billy,chuck_norris
```

Next the number of rounds is requested. Again do not include anything besides a whole number.

```
Enter the number of rounds: 15
```

The number of times to run the program is then requested. Results of one run are relatively fair meaning there is no guarantee they are the optimal result. In math-ee terms running the program finds a local max measure of fairness. Running the program multiple times increases the odds that the optimal value is found.

```
Enter the number of times to run the program: 100
```

Pretty self explanatory. There isn't really a reason not to put "y" here but the option is provided anyway.

```
Weighted rounds (getting the pick in the first pick in an early round is worth more than in later rounds)? (y/n): y
```

#### Outputs

The output is the programs optimum result of a draft order for everyone. The average weighted round pick number is exactly what it sounds like with one caveat. Before averaging the picks of a person, each pick is multiplied by a value corresponding to what round it represents. So if there are 15 rounds then frank's first pick of 3 will be 3 times 15 when it is used in the average. For frank's last round pick 1 will be 1 times 1.

The fairness score is intimately related to how the program runs. In the course of running the program once the main action happens in a for loop where the program creates random draft orders for everyone, calculates each of their average weight round picks, generates a distribution from this and checks to see if all the numbers fall within the 49th and 51st quartile. Since this nobel goal is not guaranteed to be obtainable every iteration of the loop results in small (.01) increase to the tolerance which consequentially increase the range beyond the 49th and 51st quartile. The "fairness" score is the final tolerance of the loop when it succeeds in its goal.

Running the whole program multiple times has the advantage of randomly finding a tighter set of values with less increases in the range. The final result is the output of the for loop that ran the least amount of times (had the lowest fairness score).

```
crunching numb3rs...
crunching numb3rs...
crunching numb3rs...


will's drafting order is (4, 3, 1, 1, 3, 2, 2, 3, 2, 4, 2, 4, 3, 2, 4) with an average weighted round pick of 20.2
frank's drafting order is (3, 1, 3, 3, 4, 3, 4, 2, 1, 1, 1, 3, 2, 3, 1) with an average weighted round pick of 20.2
billy's drafting order is (2, 4, 4, 2, 2, 1, 1, 1, 4, 2, 4, 1, 4, 4, 3) with an average weighted round pick of 19.8666666667
chuck_norris's drafting order is (1, 2, 2, 4, 1, 4, 3, 4, 3, 3, 3, 2, 1, 1, 2) with an average weighted round pick of 19.7333333333

And a fairness score of 0.32 (lower is better)
```

## Authors

* **Will Irwin** - *Everything* - [Upgwades](https://github.com/Upgwades)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Stackoverflow was very helpful
* My local USL Pokemon League for inspiration for the idea
