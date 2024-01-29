import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
# Legend argument is used to give specifications to the piechart..
plt.pie(y, labels = mylabels)
plt.legend(title = "Four Fruits:")
plt.show() 
# We can use EXPLODE argument to slice off a part or every part of the chart.
# eg.. myexplode = [0.2,0,0,0]...