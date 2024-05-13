import matplotlib.pyplot as plt
import pandas as pd

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

data = {
    "list": list
}

df = pd.DataFrame(data)

df.plot()   

plt.show()