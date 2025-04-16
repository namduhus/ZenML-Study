from zenml import step, pipeline

# step 1 : 프롬프트 생성
@step
def prompt_step() -> str:
    return "Tell me a fun fact about space"

# step 2 : LLM 응답 시뮬레이션
@step
def llm_step(prompt: str) -> str:
    return f"[LLM 응답] Here's something about space: {prompt[::1]}"


# step 3 : 응답출력
@step
def print_response_step(response: str) -> None:
    print(f"[LLM 응답출력] {response}")


# ZenML 파이프라인 정의
@pipeline
def llm_pipeline():
    prompt = prompt_step()
    response = llm_step(prompt)
    print_response_step(response)


if __name__ == "__main__":
    llm_pipeline().run()