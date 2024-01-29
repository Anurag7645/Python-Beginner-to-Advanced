import matplotlib.pyplot as plt
import numpy as np
# Here we are using the default xpoints given by the machine if x is not defined. eg[1,2,3,4]..
ypoints = np.array([3,8,1,10])

plt.plot(ypoints,marker = 'o')
plt.show()

# We can use the MARKER argument to emphasize each pointwith a specific marker..