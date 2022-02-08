# SonOpt
Hi! This is SonOpt, a Max/MSP application for sonifying bi-objective population-based optimization algorithms.

Requirements:

- Max 7.0 or above (demo version also works, you can download it here: https://cycling74.com/downloads/ )
- Python OSC ( more on how to install here: https://pypi.org/project/python-osc/ )

Optional:

- Pymoo (more on how to install here: https://pymoo.org/ )

If you do not wish to use pymoo - although we highy recommend it - you are free to do so. In this case, you are encouraged to copy and paste in your code the snippet 'OSC communication'. This is to ensure a smooth communication between SonOpt and your algorithm, including the correct formatting of the values sent to MAX/MSP.
You might notice the 'sleep' function at the end of each generation. The purpose of this is to intentionally slow down the algorithm in order to create perceivable sonic results. We recommend using a minimum of 0.3 sec between generations so that there is no sound lag, however this varies with the population number.

A few instruction on how to use SonOpt:

Please download all the files in the directory. Run the file named 'SonOpt.maxproj' within the project folder named 'SonOpt' (do not move it elsewhere). In the folder named 'test algorithms' you will find two optimization algorithms (NSGA-II and MOEA/D).

Open SonOpt, turn on sound, and then run the Python script of the algorithm you want to test.

Both SonOpt and the algorithms are initiallized to run out of the box. If you want to tweak the parameters you can, but in this case please consult the paper.

Enjoy!
