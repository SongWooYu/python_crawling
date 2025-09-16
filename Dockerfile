# 1. 베이스 이미지 선택 (파이썬 3.11 슬림 버전)
FROM python:3.11-slim

# 2. 작업 디렉토리 설정 (컨테이너 내부의 /app 폴더)
WORKDIR /app

# 3. requirements.txt 파일을 컨테이너의 작업 디렉토리로 복사
COPY requirements.txt .

# 4. requirements.txt에 명시된 라이브러리 설치
# --no-cache-dir 옵션은 불필요한 캐시를 남기지 않아 이미지 용량을 줄여줍니다.
RUN pip install --no-cache-dir -r requirements.txt

# 5. 현재 폴더의 모든 파일을 컨테이너의 작업 디렉토리로 복사
COPY . .

# 6. 컨테이너가 실행될 때 기본으로 실행할 명령어 (필수는 아니지만 좋은 습관)
CMD ["python", "scraper.py"]