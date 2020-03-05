from random import randrange


def cross_validation_split(dataset, n_folds):
    dataset_split = list()
    dataset_copy = list(dataset)
    fold_size = int(len(dataset) / n_folds)
    for i in range(n_folds):
        fold = list()
        while len(fold) < fold_size:
            index = randrange(len(dataset_copy))
            fold.append(dataset_copy.pop(index))
        dataset_split.append(fold)
    return dataset_split


def relative_metric(actual, predicted):
    accuracy = list()
    for ac, pr in zip(actual, predicted):
        accuracy.append((1 - abs(ac - pr) / ac) * 100)
    return sum(accuracy) / float(len(accuracy))


def accuracy_metric(actual, predicted):
    correct = 0
    for i in range(len(actual)):
        if actual[i] == predicted[i]:
            correct += 1
    return correct / float(len(actual)) * 100.0


def evaluate_algorithm(dataset, algorithm_callback, n_folds, *args):
    folds = cross_validation_split(dataset, n_folds)
    # print(folds)
    scores = list()
    relative = list()
    for fold in folds:
        # print(fold)
        train_set = list(folds)  # copy folds
        train_set.remove(fold)
        train_set = sum(train_set, [])
        # print(train_set)
        test_set = list()
        for row in fold:
            row_copy = list(row)
            test_set.append(row_copy)
            row_copy[-1] = None
        # print("#####")
        # print(train_set)
        # print(test_set)
        # print("****")
        predicted = algorithm_callback(train_set, test_set, *args)
        actual = [row[-1] for row in fold]
        accuracy = accuracy_metric(actual, predicted)
        scores.append(accuracy)
        relative.append(relative_metric(actual, predicted))
    return scores, relative
