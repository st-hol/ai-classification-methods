from random import seed

import matplotlib.pyplot as plt

import common  # execution flow
import dt  # decision tree
import knn  # k-nearest-neighbours
import utils  # read csv


def first_lab():
    seed(123)
    n_folds = 5
    dataset = utils.read_all_data()
    num_neighbors = 5
    scores_dt, relative_dt = common.evaluate_algorithm(dataset, knn.k_nearest_neighbors, n_folds, num_neighbors)

    print('--- [knn] --- Scores: %s' % scores_dt)
    print('--- [knn] --- Average Accuracy: %.3f%%' % (sum(scores_dt) / float(len(scores_dt))))
    print()
    print('--- [knn] --- Relative Scores: %s' % relative_dt)
    print("--- [knn] --- Relative Accuracy: %.3f%%" % (sum(relative_dt) / float(len(relative_dt))))

    print("-" * 150)

    max_depth = 10
    min_size = 1
    scores_knn, relative_knn = common.evaluate_algorithm(dataset, dt.decision_tree, n_folds, max_depth, min_size)
    print('--- [dt] --- Scores: %s' % scores_knn)
    print('--- [dt] --- Average Accuracy: %.3f%%' % (sum(scores_knn) / float(len(scores_knn))))
    print()
    print('--- [dt] --- Relative Scores: %s' % relative_knn)
    print("--- [dt] --- Relative Accuracy: %.3f%%" % (sum(relative_knn) / float(len(relative_knn))))
    show_graphic([i for i in range(n_folds)], relative_dt, [i for i in range(n_folds)], relative_knn)


def show_graphic(x1, y1, x2, y2):
    fig, ax = plt.subplots()
    ax.plot(x1, y1, "r", label='dt', linewidth='2', alpha=0.4)
    ax.plot(x2, y2, "b", label='knn', linewidth='2', alpha=0.4)
    ax.set_title('Compare DT and KNN')
    plt.show()


if __name__ == '__main__':
    first_lab()
