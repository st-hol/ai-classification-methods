# Split a dataset based on an attribute and an attribute value
def test_split(index, value, dataset):
    left, right = list(), list()
    for row in dataset:
        if row[index] < value:
            left.append(row)
        else:
            right.append(row)
    return left, right


# Calculate the Gini index for a split dataset
def gini_index(groups, classes):
    # print("GIN INDEX:")
    # print(groups)
    # print(classes)
    n_instances = float(sum([len(group) for group in groups]))  # count all samples at split point
    # print(n_instances)
    gini = 0.0
    for group in groups:  # sum weighted Gini index for each group
        size = float(len(group))
        if size == 0:
            continue  # avoid divide by zero
        score = 0.0
        for class_val in classes:  # score the group based on the score for each class
            p = [row[-1] for row in group].count(class_val) / size
            score += p * p
        gini += (1.0 - score) * (size / n_instances)  # weight the group score by its relative size
    return gini


def get_split(dataset):
    # print(dataset)
    class_values = list(set(row[-1] for row in dataset))  # CLASS BY RESULT
    # print(class_values)
    b_index, b_value, b_score, b_groups = 999, 999, 999, None
    # print("DATA")
    # print(dataset)
    for index in range(len(dataset[0]) - 1):  # CLASS BY INPUT
        for row in dataset:
            groups = test_split(index, row[index], dataset)  # GET RIGHT AND LEFT PREDICTED SPLIT
            gini = gini_index(groups, class_values)
            if gini < b_score:
                b_index, b_value, b_score, b_groups = index, row[index], gini, groups
    return {'index': b_index, 'value': b_value, 'groups': b_groups, 'score': b_score}


def to_terminal(group):
    outcomes = [row[-1] for row in group]
    return max(set(outcomes), key=outcomes.count)


def split(node, max_depth, min_size, depth):
    left, right = node['groups']
    del (node['groups'])
    # check for a no split
    if not left or not right:
        node['left'] = node['right'] = to_terminal(left + right)
        return
    # check for max depth
    if depth >= max_depth:
        node['left'], node['right'] = to_terminal(left), to_terminal(right)
        return
    # process left child
    if len(left) <= min_size:
        node['left'] = to_terminal(left)
    else:
        node['left'] = get_split(left)
        split(node['left'], max_depth, min_size, depth + 1)
    # process right child
    if len(right) <= min_size:
        node['right'] = to_terminal(right)
    else:
        node['right'] = get_split(right)
        split(node['right'], max_depth, min_size, depth + 1)


def build_tree(train, max_depth, min_size):
    # print(train)
    root = get_split(train)
    split(root, max_depth, min_size, 1)
    return root


def predict(node, row):
    if row[node['index']] < node['value']:
        if isinstance(node['left'], dict):
            return predict(node['left'], row)
        else:
            return node['left']
    else:
        if isinstance(node['right'], dict):
            return predict(node['right'], row)
        else:
            return node['right']


def decision_tree(train, test, max_depth, min_size):
    """"
        cart algorithm
    """
    tree = build_tree(train, max_depth, min_size)
    # print(tree)
    predictions = list()
    for row in test:
        prediction = predict(tree, row)
        predictions.append(prediction)
    # print(predictions)
    return (predictions)
