import sys
import pandas as pd
from matplotlib import pyplot as plt

def plot(filename):
	df = pd.read_csv(filename)
	df2 = df.groupby('AGE')['SEX'].value_counts().unstack().fillna(0)
	df2.plot.bar(figsize=(20,10), title='Gender/Age Bar Chart', fontsize=14)
	plt.show()

if __name__ == '__main__':
	plot(sys.argv[1])
