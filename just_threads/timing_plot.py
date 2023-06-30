"""
This script is used to generate a plot of speedup gained
as a function of the number of threads.

After performing measurements, fill in the results array below
and execute this script.
"""

import sys
import numpy as np
from matplotlib import pyplot

results = [
    # Fill in the results here, as:
    # n_threads, time_in_seconds,
    # n_threads, time_in_seconds,
    # ...
    1, 12.85,
    2, 8.2,
    3, 10.33 ,
    4, 10.51,
    5, 10.31,
    6, 10.91,
    7, 10.34,
    8, 9.56,
    9, 9.60,
    10,  9.28,
    11,9.42,
    12, 10.40
]

if ... in results:
    sys.exit('Please fill in the results in the results list above')
if results[0] != 1:
    sys.exit('Please put the result for 1 thread in the first row.\n'
             'We need it as the base.')

results = np.array(results).reshape(-1, 2)

threads = results[:, 0]
timings = results[:, 1]
assert threads[0] == 1
speedup = timings[0] / timings

fig, axes = pyplot.subplots()

axes.plot(threads, speedup, '-*')
axes.set_xlabel('# threads')
axes.set_ylabel('speedup')
axes.spines[['right', 'top']].set_visible(False)

axes.plot(threads, threads, '--')
# axes.set_ylim(top=speedup.max()*1.3)

pyplot.show()
