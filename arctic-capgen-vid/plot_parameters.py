import numpy as np

import os
import glob
# from pathlib import Path
import matplotlib.pyplot as plt

def plot_params(name, metric):

	x_names = ['Config '+str((idx+1)) for idx in range(len(metric))]

	title = "Comparing {} metric for 9 configurations".format(name)
	plt.title(title)
	plt.bar(range(len(metric)), metric, align='center')
	plt.xticks(range(len(metric)), x_names)
	plt.savefig(name+".png")
	plt.gcf().clear()
	# plt.show()


def get_params():
	print "hi"

	bleu = list()
	meteor = list()
	rouge = list()
	cider = list()

	pathlist = sorted(glob.glob('experiments/train_valid_test_*.txt'))

	# To get the files in the order of configurations
	sorted(pathlist)

	for str_path in pathlist:
		with open(str_path) as f:
			last_line = f.readlines()[-1].split()
			# print type(last_line[15])
			bleu.append(float(last_line[15]))
			meteor.append(float(last_line[19]))
			rouge.append(float(last_line[20]))
			cider.append(float(last_line[21]))

	print bleu, meteor, rouge, cider
	# print "bye"

	plot_params("BLEU", bleu)
	plot_params("METEOR", meteor)
	plot_params("ROUGE", rouge)
	plot_params("CIDEr", cider)


if __name__ == "__main__":
	get_params()