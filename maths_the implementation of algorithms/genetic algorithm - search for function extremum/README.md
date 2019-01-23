Full logic of GA implemented at "search_for_function_extremum.py" file. 
Fitness function contains a function with two parameters: F(x1, x2) = 100 / (100*(x1^2 - x2) + (x1-x1)^2 +1), that describes the extremum search space. There are ability to change function to any maths function with two parameters at method "fitness_function(value_x, value_y)".
Implemented two case of crosbreeding at random place of each chromosomes bit array: 
  with 1 break:
    chromosome1 = 1111111111
    chromosome2 = 0000000000
      progeny1 = 1111100000
      progeny2 = 0000011111
  2 breaks:
    chromosome1 = 1111111111
    chromosome2 = 0000000000
      progeny1 = 1100001111
      progeny2 = 0011110000
Selection of chromosome for crossbreeding implemented in two ways:
 - panmixia - both of chromosomes at pair for crossbreedidng chosen randomly from current population;
 - selective - chromosome is able to become a part of pair for crossbreeding only if it has fitness >= to average fitness of current population.
Chromosome can get to updated population from new and previous populations with highest value of fitness.
Calculations performs by set count of generations.

The result of final generation will shows and will contains all chromosomes at final population with their calculated fitness function.

There is ability to set next parameters:
- count of generetions;
- size of population;
- probability of mutation;
- probability of crossbreeding;
- set a range for x1 and x2
- count of chromosomes pairs for crossbreeding;
- numbers of breaks for crossbreeding (1 point, 2 point);
- selection type;
- accuracy of calculations - count of digit at float number after dot.

All unique chromosomes will be saved after calculations in a * .json file as a list. This will help to use it in the program for visualizing the approximation of calculations to the solution and their distribution in the studied area.
