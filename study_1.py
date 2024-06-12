# 【うるう年を判定するルール】
# 原則として、西暦が4で割り切れる年は、うるう年である
# ただし原則として西暦が100で割り切れる盧氏は、閏年ではない
# ただし、西暦が400で割り切れる年は、絶対にうるう年ではない

# 上記のルールに準拠すると、400年にうるう年は97回存在することになる

def leap_year(year) :
    if (year % 4 == 0 and year % 100 != 0 ) or year % 400 == 0 :
        return True
    else:
        return False
   
# 指定された年月の「1日」は何曜日？
def day_of_week(year, month):
    # 1月~12月の月の日数
    days_of_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
   
    # うるう年の場合は2月の日数が29になる
    if leap_year(year):
        days_of_month[2] = 29
   
    # dayに1日を設定する
    day = 1
   
    # 西暦１年１月1日（月曜日）からの日数を得る
    days = 0
   
    # 年の日数を集計する
    for y in range(1, year):
        if(leap_year(y)):
            days += 365
        else:
            days += 366
   
    # 月の日数を集計する
    for m in range(1, month):
        days += days_of_month[m]
       
    # 日を集計する
    days += day
   
    # 日曜日~土曜日を0~6で返す
    return days % 7
   

if __name__ == '__main__':
    # 曜日
    days_of_week_name = ['日','月','火','水','木','金','土']

    # 年月をキー入力する
    # 入力データを読み込む
    for i in range(1):
        year = int(input())
        month = int(input())
        # １日の曜日を表示する
        print(str(year)+ '年' + str(month)+ '月1日は' + days_of_week_name[day_of_week(year, month)] + '曜日')