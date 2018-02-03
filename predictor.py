from surprise import SlopeOne
from surprise import Dataset
import sys, os

def getPrediction( uid, iid):

	data = Dataset.load_builtin('ml-100k')

	trainset = data.build_full_trainset()

	algo = SlopeOne()
	algo.fit(trainset)
	pred = algo.predict(uid, iid, r_ui=4, verbose=True)

	return pred.est

def main():
	lines = sys.stdin.readlines()

	lines = lines[0]
	lines = lines.split(',')
	uid = int(lines[0])
	iid = int(lines[1])
	pred = getPrediction(str(uid), str(iid))

	print pred


if __name__ == '__main__':
    main()