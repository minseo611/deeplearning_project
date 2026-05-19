import pandas as pd

# GitHub의 원본(Raw) 데이터 직접 링크
url = 'https://raw.githubusercontent.com/e9t/nsmc/master/ratings_train.txt'

# URL에서 바로 읽어오기 (다운로드 과정 생략)
df = pd.read_csv(url, sep='\t')

# 데이터가 잘 들어왔는지 상위 5개 행 확인
print("데이터 로드 완료! 데이터 크기:", df.shape)
print(df.head())