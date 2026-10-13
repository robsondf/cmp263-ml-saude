"""Pipelines candidatos de classificação tabular; ajustar ao dataset/protocolo."""
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

def classification_pipelines(numeric, categorical, seed=263):
    """Retorna pipelines novos; chamar fit só no treino de cada divisão.

    Colunas ordinais, grupos, datas, códigos de ausência e alvo precisam ser
    auditados antes. Não infere o tipo clínico a partir do dtype numérico.
    Não faz balanceamento, tuning, calibração ou divisão automaticamente.
    """
    if set(numeric) & set(categorical):
        raise ValueError('Colunas numéricas e categóricas devem ser distintas.')
    if not numeric and not categorical:
        raise ValueError('Defina as colunas elegíveis no protocolo.')
    models = {
        'dummy': DummyClassifier(strategy='prior'),
        'logistic_regression': LogisticRegression(max_iter=2000, random_state=seed),
        'knn': KNeighborsClassifier(n_neighbors=5),
        'decision_tree': DecisionTreeClassifier(random_state=seed),
        'random_forest': RandomForestClassifier(n_estimators=200, random_state=seed, n_jobs=1),
        'svm': SVC(kernel='rbf', probability=False, random_state=seed),
    }
    result = {}
    for name, estimator in models.items():
        numeric_steps = Pipeline([
            ('impute', SimpleImputer(strategy='median', keep_empty_features=True)),
            ('scale', StandardScaler()),
        ])
        categorical_steps = Pipeline([
            ('impute', SimpleImputer(strategy='most_frequent', keep_empty_features=True)),
            ('encode', OneHotEncoder(handle_unknown='ignore', sparse_output=True)),
        ])
        prepare = ColumnTransformer([
            ('numeric', numeric_steps, list(numeric)),
            ('categorical', categorical_steps, list(categorical)),
        ], remainder='drop')
        result[name] = Pipeline([('prepare', prepare), ('model', estimator)])
    return result
