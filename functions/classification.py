from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier, KernelDensity
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def plot_confusion_matrix(y_true, y_pred, model_name, target_name):
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=np.unique(y_true), yticklabels=np.unique(y_true))
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')
    plt.title(f'Macierz konfuzji dla {model_name} ({target_name})')
    plt.show()

def classify(features, target, target_name='unnamed', model_type='decision_tree', params=None):
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.6, random_state=12)
    if model_type == 'random_forest':
        model = RandomForestClassifier(random_state=params[0])
    elif model_type == 'decision_tree':
        model = DecisionTreeClassifier(random_state=params[0])
    elif model_type == 'knn':
        model = KNeighborsClassifier(n_neighbors=params[1])
    model.fit(X_train, y_train)


    y_pred = model.predict(X_test)

    print(f'Dokładność modelu {model_type} dla {target_name}:{accuracy_score(y_test, y_pred):.2f}', )

    # cm = confusion_matrix(y_test, y_pred)
    # print(cm)

    plot_confusion_matrix(y_test, y_pred, model_type, target_name)

    # print(classification_report(y_test, y_pred))

# def classify_density(features, target, model_type='kernel_density'):
#     X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.3, random_state=42)
#
#     classes = np.unique(y_train)
#     kde_models = {}
#     for cls in classes:
#         class_data = X_train[np.array(y_train).ravel() == cls]
#         kde = KernelDensity(kernel='gaussian', bandwidth=1.0)
#         kde.fit(class_data)
#         kde_models[cls] = kde
#     y_pred = []
#     for test_sample in X_test:
#         densities = {cls: kde.score_samples([test_sample])[0] for cls, kde in kde_models.items()}
#         y_pred.append(max(densities, key=densities.get))
#     y_pred = np.array(y_pred).ravel()
#     y_test = np.array(y_test).ravel()
#     accuracy = accuracy_score(y_test, y_pred)
#     print("Dokładność modelu:", accuracy)
#     print(classification_report(y_test, y_pred))
#     print(confusion_matrix(y_test, y_pred))

