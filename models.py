import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier



def get_score(name, classifier, param_grid):
    # Read in prepped data
    train_features = pd.read_csv('./data/prepped/train_features.csv', sep=',')
    test_features = pd.read_csv('./data/prepped/test_features.csv', sep=',')
    train_outcome = pd.read_csv('./data/prepped/train_outcome.csv', sep=',')
    test_outcome = pd.read_csv('./data/prepped/test_outcome.csv', sep=',')

    # Create Scalar
    scaler = MinMaxScaler()

    # Create pipeline
    pipeline = make_pipeline(scaler, classifier)

    # Grid search pipeline
    grid_search = GridSearchCV(pipeline, param_grid=param_grid, return_train_score=True, scoring='accuracy')

    # Train
    grid_search.fit(train_features[1:], train_outcome['17'])

    # Score
    grid_search.score(test_features[1:], test_outcome['18'])

    # Predict
    predictions = grid_search.predict(test_features)

    # Return Params & Score 
    best_param = grid_search.cv_results_['params'][grid_search.best_index_]
    best_score = name + ' ' + str(grid_search.best_score_)
    return best_param, best_score, predictions


# Create Classifiers
neighbors_clf = KNeighborsClassifier()
tree_clf = DecisionTreeClassifier()
neural_clf = MLPClassifier()
ada_clf = AdaBoostClassifier()


# Create param grids
neighbors_grid = {
    'kneighborsclassifier__n_neighbors':range(1, 5),
    'kneighborsclassifier__weights':['uniform', 'distance']
}
tree_grid = {
    'decisiontreeclassifier__max_depth': range(1,20),
    'decisiontreeclassifier__criterion': ['gini', 'entropy'],
    'decisiontreeclassifier__splitter': ['best', 'random']
}
neural_grid = {
    'mlpclassifier__learning_rate': ['constant', 'invscaling', 'adaptive'],
    'mlpclassifier__hidden_layer_sizes': [(100, 10), (100, 20), (100, 30)],
    'mlpclassifier__activation': ['logistic', 'relu', 'tanh']
}
ada_grid = {
    'adaboostclassifier__n_estimators': range(1, 50)
}

# Run Scores
neighbors_param, neighbors_score, neighbors_pred = get_score('K Nearest Neighbors', neighbors_clf, neighbors_grid)
tree_param, tree_score, tree_pred = get_score('Decision Trees', tree_clf, tree_grid)
neural_param, neural_score, neural_pred = get_score('Neural Network', neural_clf, neural_grid)
ada_param, ada_score, ada_pred = get_score('ADA Boost', ada_clf, ada_grid)

pd.DataFrame(tree_pred).to_csv('./data/prepped/predictions.csv')

    

# Print Scores
print(neighbors_score) 
print(tree_score) 
print(neural_score) 
print(ada_score)
