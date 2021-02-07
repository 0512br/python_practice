# モジュールをインポート
import math

# 給料を入力
monthlySalary = input('月あたりの給料 (円):')
monthlySalary = float(monthlySalary)

# 離職時の年齢を入力
retirementAge = input('離職時の年齢 (歳):')
retirementAge = int(retirementAge)

# 賃金日額を概算
dailyWage = monthlySalary / 30
dailyWage = math.floor(dailyWage)

# retirementAgeによって賃金日額の最高額が変わってくる, 就業促進定着手当の計算のみなので基本手当だけだったらいらない？
# 最低額は年齢共通(50616)
minDailyWage = 2574
if 60 <= retirementAge < 65:
  maxDailyWage = 15970
elif 45 <= retirementAge < 60:
  maxDailyWage = 16740
elif 30 <= retirementAge < 45:
  maxDailyWage = 15210
else:
  maxDailyWage = 13700

if dailyWage > maxDailyWage:
  dailyWage = maxDailyWage

# 基本手当日額の計算(一般被保険者)
# 給付率を求める, (50617, 50801)
# 基準値は毎月勤労統計に基づき変更
minStandard = 5030
maxStandard = 12390
minStandard_over60 = 5030
maxStandard_over60 = 11140
if 60 <= retirementAge < 65:
  if minDailyWage <= dailyWage < minStandard_over60:
    rate = 0.8
  elif maxStandard < dailyWage:
    rate = 0.45
  else:
    rate = 0.8 - 0.35 * (dailyWage - minStandard_over60) / (maxStandard_over60 - minStandard_over60)
else:
  if minDailyWage <= dailyWage < minStandard:
    rate = 0.8
  elif maxStandard < dailyWage:
    rate = 0.5
  else:
    rate = 0.8 - 0.3 * (dailyWage - minStandard) / (maxStandard - minStandard)

# resultRate = rate * 100
# resultRate = math.floor(resultRate)
# print('給付率: ' + str(resultRate) + '%')

# 基本手当日額の出力
resultPrice = dailyWage * rate
resultPrice = math.floor(resultPrice)
print('基本手当日額の概算: ' + str(resultPrice) + '円')

