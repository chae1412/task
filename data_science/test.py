import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.jointplot(x=tips['total_bill'], y=tips['tip'], kind='hex')

plt.show()