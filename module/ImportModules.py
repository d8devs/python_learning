'''
import matplotlib.pyplot as plt

plt.plot([1,2,3], [5,4,5])
plt.show()
'''
# otherwise long version without "as" naming
'''

import matplotlib.pyplot

matplotlib.pyplot.plot([1,2,3], [5,4,5])
matplotlib.pyplot.show()
'''

# otherwise import only pyplot functionality
from matplotlib import pyplot

pyplot.plot([1,2,3], [5,4,5])
pyplot.show()