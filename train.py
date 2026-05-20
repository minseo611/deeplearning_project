import pandas as pd
import re

# GitHub의 원본(Raw) 데이터 직접 링크
url = 'https://raw.githubusercontent.com/e9t/nsmc/master/ratings_train.txt'

# URL에서 바로 읽어오기 (다운로드 과정 생략)
df = pd.read_csv(url, sep='\t')

# 데이터가 잘 들어왔는지 상위 5개 행 확인
print("데이터 로드 완료! 데이터 크기:", df.shape)
print(df.head())

def normalize_korean_text(text):
    if not isinstance(text, str):
        return ""
    
    # 특수문자 제거 (한글, 영문, 숫자, 공백 보존)
    text = re.sub(r'[^가-힣ㄱ-ㅎㅏ-ㅣa-zA-Z0-9\s]', '', text)
    # 반복 자모음 정규화 (2회 제한, 예: ㅋㅋㅋㅋ -> ㅋㅋ)
    text = re.sub(r'([ㄱ-ㅎㅏ-ㅣ])\1+', r'\1\1', text)
    # 다중 공백 단일화 및 양끝 공백 스트립
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

print("전처리 작업을 시작합니다. 15만 개 데이터라 수십 초 정도 걸릴 수 있습니다...")

# 2. 결측치(NaN)가 있는 행 제거
df = df.dropna(subset=['document'])

# 3. 전처리 함수 적용 (apply 함수로 15만 개 행에 일괄 적용)
df['clean_text'] = df['document'].apply(normalize_korean_text)

# 4. 전처리 결과가 빈 문자열('')인 행 제거 (이모티콘만 있던 리뷰 등)
df = df[df['clean_text'] != '']

# 5. 팀원 2와 약속한 규격으로 데이터프레임 추출
final_df = df[['clean_text', 'label']].copy()

# 6. 전처리 완료된 데이터를 CSV 파일로 저장
final_df.to_csv('preprocessed_train_data.csv', index=False, encoding='utf-8-sig')

print(f"전처리 100% 완료! 최종 데이터 크기: {final_df.shape}")
print("VS Code 왼쪽 탐색기 창을 확인해보세요. 'preprocessed_train_data.csv'가 생성되었습니다!")