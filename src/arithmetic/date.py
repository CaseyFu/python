# 转化时间
import math
import time


def isLeapYear(year):
    # 判断闰年
    if((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
        return True
    else:
        return False


def getMonthOfDayA(year, month):
    # 返回一个月有多少天
    day = 0
    if(month == 2):
        if(isLeapYear(year)):
            day = 29
        else:
            day = 28
    else:
        day = math.ceil(abs(month-7.5)) % 2 + 30
    return day


def getMonthOfDayB(year, month):
    # 返回一个月有多少天
    if(year < 1 or month < 1 or month > 12):
        return None
    commonYear = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if(isLeapYear(year) and month == 2):
        return int(commonYear[1]+1)
    else:
        return int(commonYear[month-1])


def calculateDate(baseDate, totalDay):
    # 根据基准yyyy-MM-dd和天数计算时间
    arr = baseDate.split("-")
    year = int(arr[0])
    month = int(arr[1])
    day = int(arr[2])
    if(month > 12 or day > getMonthOfDayB(year, month)):
        print("输入不合法")
        return
    for i in range(1, 4, 1):
        totalDay += getMonthOfDayB(year, i)
    totalDay += day
    while(totalDay > 365):
        if(isLeapYear(year)):
            totalDay -= 366
        else:
            totalDay -= 365
        year += 1

    month = 1
    while(totalDay > getMonthOfDayB(year, month)):
        totalDay -= getMonthOfDayB(year, month)
        month += 1
    print(year, "-", month, "-", totalDay-1)


def calculateDaysOfBirth(birthday):
    now = time.localtime(time.time())
    ticks = time.time()
    print(ticks)
    print(now)


if(__name__ == "__main__"):
    calculateDaysOfBirth("hhh")
