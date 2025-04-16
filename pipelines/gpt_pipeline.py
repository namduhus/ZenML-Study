from zenml import step, pipeline
from openai import OpenAI
from dotenv import load_dotenv
import os

# 환경 변수 불러오기
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key = api_key)

# Step 1: 프롬프트 생성
@step
def prompt_step() -> str:
    return ("Tell me a fun fact about black holse")


# Step 2: 실제 OpenAI LLM 호출
@step
def openai_step(prompt: str) -> str:
    response = client.chat.completions.create(
        model = "gpt-3.5-turbo-0125",
        messages = [
            {"role": "system", "content": "You are a science expert."},
            {"role": "user", "content" : prompt}
        ]
    )
    return response.choice[0].message.content

# step 3: 응답출력
@step
def print_response_step(response: str) -> None:
    print(f"[GPT 응답출력]{response}")

# step 4: 파이프라인
@pipeline
def pipeline():
    prompt = prompt_step()
    response = openai_step(prompt)
    print_response_step(response)

if __name__ == "__main__":
    pipeline().run()