import requests
from bs4 import BeautifulSoup
import json

# 대상 URL
url = "https://www.kopo.ac.kr/jungsu/content.do?menu=247"

# 1. 페이지 요청
res = requests.get(url)
res.encoding = "utf-8"   # 한글 깨짐 방지
soup = BeautifulSoup(res.text, "html.parser")

# 2. 식단 테이블 찾기
table = soup.find("table", {"class": "tbl_table menu"})
rows = table.find("tbody").find_all("tr")

menu_data = []

for row in rows:
    cols = row.find_all("td")
    if len(cols) == 4:  # 구분, 조식, 중식, 석식
        # 날짜 부분은 "2025-09-08\n월요일" 형태 → 첫 줄만 추출
        date_text = cols[0].get_text(strip=True).split("\n")[0]

        # 식단 데이터 추출
        def clean_menu(td):
            items = td.get_text(strip=True).replace("\n", "").split(", ")
            return items if items != [''] else None

        breakfast = clean_menu(cols[1])
        lunch = clean_menu(cols[2])
        dinner = clean_menu(cols[3])

        menu_data.append({
            "date": date_text,
            "breakfast": breakfast,
            "lunch": lunch,
            "dinner": dinner
        })

# 3. JSON 형식으로 보기 좋게 출력
print(json.dumps(menu_data, ensure_ascii=False, indent=2))