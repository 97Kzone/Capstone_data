import dataToDb
import state_cal 
import pymysql

# 미리 해야 하는 것
# 0. dataToDb, state_cal 파일의 library 중 불 꺼진 library install 해주세요... (ex. schedule)
# 1. fdr 라이브러리를 최신화 해주세요(중요) "pip install --upgrade finance-datareader"

# 0. US채권(1,5,10) 수익률 세팅, 1회 실시 후 daily_total() 로 최신화하면 됩니다
# dataToDb.us_bond()

# 1. 일일 주가 최신화, stock_marcap_old, stock_marcap 2개 DB UPDATE
# dataToDb.every_do()
# state_cal.union_table()

# 2. 일일 종합 지수 최신화 (KOSPI, NASDAQ, S&P500, US채권)
# dataToDb.daily_total()

# 3. 매일 갱신해야 하는 메소드 22-09-12 일단 날짜 자동화 작업중
# state_cal.every_pebr() # 오늘날짜까지 per, pbr, psr update (날짜 자동화 O)
# state_cal.sector_pebr() # 모든 업종 평균 per, pbr, psr (날짜 자동화 O)
# state_cal.daily_evalu_update() # 종목별 적정주가 업데이트 (날짜 자동화 O)
state_cal.daily_evalu_score() # 당일주가 / 적정주가 비율 계산 (아직 문제 많음 사용 X)
# state_cal.daily_donda() # 돈다지수

# 4. 재무제표가 추가되면 이용할 메소드 (분기)
# dataToDb.stock_statement() #재무제표 추가 됐을 때 사용
# state_cal.report_cal() #재무제표 연결 => 당기로 분리
# state_cal.cal_statement() # 추가된 재무제표 EPS, BPS, ROE 계산 
# state_cal.sector_indicator() # 업종평균 EPS, BPS, ROE
# state_cal.cal_epsrate() # EPS 증가율
# state_cal.cal_pegr() 
# state_cal.cal_evalu()
# state_cal.daily_evalu_update()

# 5. 아직 사용하지 않는 메소드
# daily_donda() # 돈다지수 초회 세팅용 (분기 + 일일 평균 값)

