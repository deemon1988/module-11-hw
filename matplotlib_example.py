from fishing import caught_fish
import pandas as pd
import matplotlib.pyplot as plt

products = {'Potato': 50, 'Tomato': 15, 'Apple': 20, 'Banana': 30}

temperature = {"2025-01-01": 2, "2025-01-02": 3, "2025-01-03": 5, "2025-01-04": 4, "2025-01-05": 6, "2025-01-06": 7,
               "2025-01-07": 8}

temp_data = pd.Series(temperature)
fish_data = pd.Series(caught_fish)
product_data = pd.Series(products)

figure, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(17, 6))
ax1.plot(temp_data)
ax1.set_title('Temperature by day of week')
ax2.pie(fish_data, labels=fish_data.index)
ax2.set_title('Fish Caught')
ax3.bar(product_data.index, height=product_data)
ax3.set_title('Products')

plt.tight_layout()
plt.show()
