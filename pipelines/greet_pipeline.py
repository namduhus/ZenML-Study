from zenml import step, pipeline

# step 1: 사용자 이름 생성
@step
def input_step() -> str:
    return "Duhyeon"

# step 2: 인사말 생성
@step
def greet_step(name: str) -> str:
    return f"Nice meet you, {name}!"

# step 3: 인사말 출력
@step
def print_step(greeting: str) -> None:
    print(f"[print_step] 👋{greeting}")

# 파이프라인 정의
@pipeline
def greet_pipeline():
    name = input_step()
    greeting = greet_step(name)
    print_step(greeting)

# 실행
if __name__ == "__main__":
    greet_pipeline().run()