import glob
import matplotlib.pyplot as plt


def plot_params(name, metric):
	# Setting a title for the plot
	title = "Comparing {} metric for {} configurations".format(name, len(metric))
	plt.title(title)

	# Line graph for each config
	for idx, config in enumerate(metric):
		plt.plot(range(len(config)), config, label="Config {}".format(idx+1))

	# Best position
	plt.legend(loc=0)

	# Save the plot as a file
	plt.savefig("{}.png".format(name))

	# Clear the plot so that next one can be created from scratch
	plt.gcf().clear()


def get_params():
	bleu = list()
	meteor = list()
	rouge = list()
	cider = list()

	pathlist = sorted(glob.glob('experiments/train_valid_test_*.txt'))

	# To get the files in the order of configurations
	sorted(pathlist)

	for idx, str_path in enumerate(pathlist):
		# Create an array for storing all values of this file
		bleu.append([])
		meteor.append([])
		rouge.append([])
		cider.append([])

		# Open the file
		with open(str_path) as f:
			lines = f.readlines()

			for line in lines:
				split_line = line.split()

				# # For validation value of metrics
				# bleu[idx].append(float(split_line[8]))
				# meteor[idx].append(float(split_line[12]))
				# rouge[idx].append(float(split_line[13]))
				# cider[idx].append(float(split_line[14]))

				# For test value of metrics
				bleu[idx].append(float(split_line[15]))
				meteor[idx].append(float(split_line[19]))
				rouge[idx].append(float(split_line[20]))
				cider[idx].append(float(split_line[21]))

	print bleu, meteor, rouge, cider

	plot_params("BLEU", bleu)
	plot_params("METEOR", meteor)
	plot_params("ROUGE", rouge)
	plot_params("CIDEr", cider)


if __name__ == "__main__":
	get_params()
