from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from zenml import step, pipeline
from typing import Tuple
import numpy as np


# 학습 데이터로딩 단계
@step
def data_loader()-> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(iris.data, 
                                                        iris.target, 
                                                        test_size=0.2, 
                                                        random_state=42)
    return X_train, X_test, y_train, y_test


# 모델 학습 단계
@step
def trainer(X_train: np.ndarray, y_train: np.ndarray) -> LogisticRegression:
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)
    return model


# 정확도 평가
@step
def evaluator(model: LogisticRegression, X_test: np.ndarray, y_test: np.ndarray) -> float:
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    return acc


# 결과 출력
@step
def print_score(acc: float) -> None:
    print(f"[Acc] {acc:.4f}")


# 파이프라인
@pipeline
def iris_pipeline():
    X_train, X_test, y_train, y_test = data_loader()
    model = trainer(X_train=X_train, y_train=y_train)
    acc = evaluator(model=model, X_test=X_test, y_test=y_test)
    print_score(acc=acc)

if __name__ == "__main__":
    iris_pipeline().run()