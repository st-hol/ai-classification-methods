from random import seed

import common  # execution flow
import dt  # decision tree
import knn  # k-nearest-neighbours
import utils  # read csv


def first_lab():
    seed(123)
    n_folds = 5
    dataset = utils.read_all_data()
    num_neighbors = 5
    scores, relative = common.evaluate_algorithm(dataset, knn.k_nearest_neighbors, n_folds, num_neighbors)

    print('--- [knn] --- Scores: %s' % scores)
    print('--- [knn] --- Average Accuracy: %.3f%%' % (sum(scores) / float(len(scores))))
    print("--- [knn] --- Relative Accuracy: %.3f%%" % (sum(relative) / float(len(relative))))

    print("-" * 150)

    max_depth = 10
    min_size = 1
    scores, relative = common.evaluate_algorithm(dataset, dt.decision_tree, n_folds, max_depth, min_size)
    print('--- [dt] --- Scores: %s' % scores)
    print('--- [dt] --- Average Accuracy: %.3f%%' % (sum(scores) / float(len(scores))))
    print("--- [dt] --- Relative Accuracy: %.3f%%" % (sum(relative) / float(len(relative))))


if __name__ == '__main__':
    first_lab()
