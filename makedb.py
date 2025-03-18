import random
import pandas as pd
# 사용할 과목 리스트
subjects = [
    "물리학2", "생명과학2", "지구과학2", "화학2", "일본어2", "윤리와사상", "정치와법", "과학사",
    "인공지능수학", "기하", "심화수학", "영화감상과비평", "환경", "인공지능과피지컬컴퓨팅", "응용프로그래밍개발"
]

# 랜덤한 한국어 이름 생성 (일반적인 한국 성 + 자주 쓰이는 이름 조합)
surnames = ["김", "이", "박", "최", "정", "조", "윤", "장", "임", "한"]
first_names = ["민준", "서연", "지우", "서현", "예준", "도윤", "하은", "지호", "하윤", "은서", 
               "민재", "현우", "승민", "서우", "준서", "태윤", "유진", "윤서", "지민", "수민"]

# 학번 생성 (30101 ~ 31130 범위에서 랜덤 선택)
student_ids = [f"{grade}{class_num:02}{student_num:02}" for grade in range(3, 4) 
               for class_num in range(1, 12) for student_num in range(1, 31)]
random.shuffle(student_ids)

# 200개 데이터 생성
data = []
for i in range(200):
    student_id = student_ids[i]
    name = random.choice(surnames) + random.choice(first_names)
    password = f"{random.randint(1000, 9999)}"
    chosen_subjects = random.sample(subjects, 4)  # 랜덤하게 4개 과목 선택

    data.append([student_id, name, *chosen_subjects, password])

# 데이터프레임 생성
columns = ["number", "name", "a-class", "b-class", "c-class", "d-class", "password"]
df_students = pd.DataFrame(data, columns=columns)

# UTF-8로 인코딩하여 CSV 파일로 저장
output_file_path = "student_database.csv"
df_students.to_csv(output_file_path, index=False, encoding="utf-8")

# 파일 경로 제공
output_file_path