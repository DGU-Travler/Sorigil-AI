from openai import OpenAI
from dotenv import load_dotenv
import json
import os

# .env 파일 로드
load_dotenv()

client = OpenAI(
  api_key=os.getenv("GPT_API")  # API 키 설정
)

def main():

    with open("input.json", "r", encoding="utf-8") as file:
        input_data = json.load(file)

    user_input = input_data.get("message", "")

    # 기본적인 시스템 프롬프트 설정
    system_prompt = """
    너는 입력된 내용을 간결하고 이해하기 쉽게 바꿔주는 역할을 수행해. 
    중요한 정보는 남기되, 불필요한 표현은 줄여서 명확하게 전달하는 데 초점을 맞춰줘.
    """

    # 메시지 구성
    messages = [{"role": "system", "content": system_prompt.strip()}, {"role": "user", "content": user_input.strip()}]

    # OpenAI API 호출
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # 사용하려는 모델 이름
        messages=messages
    )

    # 응답 출력
    assistant_reply = response.choices[0].message.content
    print("\nGPT의 응답:")
    print(assistant_reply)

if __name__ == "__main__":
    main()
