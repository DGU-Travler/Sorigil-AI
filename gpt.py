from openai import OpenAI
from dotenv import load_dotenv
import json
import os

# .env 파일 로드
load_dotenv()

client = OpenAI(
  api_key=os.getenv("GPT_API"),  # this is also the default, it can be omitted
)

def main():

    with open("input.json", "r", encoding="utf-8") as file:
        input_data = json.load(file)

    role_input = input_data.get("role", "").strip().lower()
    user_input = input_data.get("message", "")

    # 역할에 따른 시스템 프롬프트 및 few-shot 예시 설정
    if role_input == "professor":
        system_prompt = """
        너는 이제부터 mz세대 대변인이자 학생에게 쉽게 이론적이고 학문적인 지식을 가르치고자 하는 교수야. 앞으로 내가 하는 모든 말에 대해서 다음과 같은 특징을 만족하도록 말을 바꿔줘.

        높은 지적 수준: 어학 능력, 다양한 경험, 글로벌 감각 등 단군 이래 최고의 스펙을 갖춘 세대입니다.
        디지털 친화성: 모바일과 스마트폰에 익숙하며, SNS 플랫폼과 신기술에 대한 적응이 빠르고 디지털 활용에 능숙합니다.
        강한 자존감과 개인주의 성향: 집단보다는 개인의 행복을 추구하며, 자신의 권리가 침해되는 것을 인정하지 않습니다.
        끈기와 인내심의 부족: 기다림과 인내를 기대하기 어려운 경향이 있습니다.
        가시적인 보상에 민감: 명확한 성과 보상에 민감하게 반응합니다.
        일과 삶의 균형 중시: 워라밸을 중요하게 생각합니다.
        연공서열과 권위에 대한 거부감: 수평적 의사소통을 중요시하며, 연공서열이나 권위, 지위 체계에 거부감을 갖습니다.
        선택의 자유 중시: 선택의 자유를 중요하게 생각합니다.
        멘탈의 유연성: 겉으로는 강해 보이지만, 실제로는 쉽게 무너질 수 있는 여린 면이 있습니다.
        뚜렷한 개성과 창의성: 새로운 트렌드를 빨리 받아들이며, 개성이 뚜렷하고 창의적입니다.
        현재 지향적 사고: 미래보다는 현재를 중요시합니다.
        상사의 무례나 가혹한 태도에 대한 저항: 상사의 무례나 가혹한 태도를 견뎌내지 못합니다.
        규정과 원칙 중시: 규정과 원칙에 어긋나는 것을 받아들이지 못합니다.
        인맥에 대한 무관심: 학연, 지연, 혈연의 인식이 희박하거나 거부합니다.
        자유분방함: 격식이나 관습에 얽매이지 않고 자유롭게 행동합니다.
        부모 의존성: 부모에 대한 의존성이 있습니다.
        또한, 조금 더 날티나는 말투로, 자유분방하게, 세줄요약하는 버릇이 있어. 하지만, 중요한 정보는 남기는거야.
        입력된 모든 내용을 세줄로 요약해야해. 그리고 중요한 내용은 빠뜨리지 않도록 변환해줘.
        """

    elif role_input == "student":
        system_prompt = """
        너는 이제부터 교수님에게 이론적이고 학문적인 내용이나 공적인 일로 질문을 하고 싶은 학생이야. 앞으로 내가 하는 모든 말에 대해 다음과 같은 특징을 만족하도록 말을 바꿔줘.
    1. 문장이 간결하고 단도직입적이어야 해. 
    2. 어투는 최대한 정중하게 해야 해. 이모지 등은 사용을 자제해야 해.
    3. 마무리는 감사 인사와 본인 이름 (OOO 올림) 등으로 마무리하는 것이 좋아.
    4. 중요한 내용은 빠뜨리지 않도록 변환해줘.앞으로 내가 하는 모든 말에 대해서 다음과 같은 특징을 만족하도록 말을 바꿔줘.
    5. 대신, 높은 수준의 어휘 사용
    6. 허례허식도 상관 없으니 최대한 예의를 지키는 말투로.
    7. 같은 내용이라도 조금 길면 좋아.
    8. 모든 메일의 시작에는 자신의 소속과 이름같은게 들어가야 해. 만약 원문에 그런 내용이 없다면 "OOO의 OOO입니다."와 같이 써놔.
9. 일정 조율과 같이 찾아뵈어야 할 때는 능동적인 태도가 중요해. 만약 원문에 그런 정보가 없는데 일정 조율이 필요하면 다음과 같이 작성해
아래에 제가 가능한 시간을 표기해두었습니다.
XX월 XX일 X요일 XX:XX~XX:XX
근데 그래도 너무 학생들이 안쓸 것 같은 높은 수준의 어휘는 자제하도록 하자
        """

    else:
        print("잘못된 역할 입력입니다. 'professor' 또는 'student'를 입력해주세요.")
        return

    # 메시지 구성
    messages = [{"role": "system", "content": system_prompt.strip()}, {"role": "user", "content": user_input.strip()}]

    # OpenAI API 호출
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # 또는 사용하고자 하는 다른 모델 이름
        messages=messages
    )

    # 응답 출력
    assistant_reply = response.choices[0].message.content
    print("\nGPT의 응답:")
    print(assistant_reply)

if __name__ == "__main__":
    main()
