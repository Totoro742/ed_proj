from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier


def classify(features, target, model_type='decision_tree'):
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.3, random_state=42)
    if model_type == 'random_forest':
        model = RandomForestClassifier(random_state=42)
    elif model_type == 'decision_tree':
        model = DecisionTreeClassifier(random_state=42)
    elif model_type == 'knn':
        model = KNeighborsClassifier(n_neighbors=4)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    print("Dokładność modelu:", accuracy_score(y_test, y_pred))


    print(classification_report(y_test, y_pred))

    #print confusion matrix

    print(confusion_matrix(y_test, y_pred))