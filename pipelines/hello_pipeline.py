from zenml import pipeline
from zenml.steps import step

# Step 정의
@step
def hello_step() -> None:
    print("✅ Hello from ZenML!")

# Pipeline 정의
@pipeline
def hello_pipeline():
    hello_step()

# 실행
if __name__ == "__main__":
    hello_pipeline().run()
