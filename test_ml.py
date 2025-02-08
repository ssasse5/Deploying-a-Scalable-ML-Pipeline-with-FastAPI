import pytest
import pandas as pd
import numpy as np
from ml.model import train_model, inference, compute_model_metrics
from sklearn.ensemble import RandomForestClassifier
# TODO: add necessary import

def sample_data():
    X = np.random.rand(100, 5)
    y = np.random.randint(0, 2, 100)
    return X, y
# TODO: implement the first test. Change the function name and input as needed
def test_train_model():
    """
    Test if train_model returns a trained RandomForestClassifier instance.
    """
    X_train, y_train = sample_data()
    model = train_model(X_train, y_train)
    assert isinstance(model, RandomForestClassifier)
    pass


# TODO: implement the second test. Change the function name and input as needed
def test_inference():
    """
    Test if inference function returns expected output type and shape.
    """
    X_train, y_train = sample_data()
    model = train_model(X_train, y_train)
    preds = inference(model, X_train)
    assert isinstance(preds, np.ndarray)
    assert preds.shape[0] == X_train.shape[0]
    pass


# TODO: implement the third test. Change the function name and input as needed
def test_compute_model_metrics():
    """
    Test if compute_model_metrics returns precision, recall, and fbeta.
    """
    y_true = np.array([1, 0, 1, 1, 0, 1, 0, 0, 1, 0])
    y_pred = np.array([1, 0, 1, 1, 0, 0, 0, 1, 1, 0])
    precision, recall, fbeta = compute_model_metrics(y_true, y_pred)
    assert isinstance(precision, float)
    assert isinstance(recall, float)
    assert isinstance(fbeta, float)
    pass
