import sys
from datetime import datetime
from .dataModule import DailyInoutData, WeeklyInoutData, MonthlyInoutData, YearlyInoutData
from .emailModule import InoutEmail


class InoutReport:
    def __init__(self, config):
        self.config = config
        self.dailyData = DailyInoutData(self.config)
        self.weeklyData = WeeklyInoutData(self.config)
        self.monthlyData = MonthlyInoutData(self.config)
        self.yearlyData = YearlyInoutData(self.config)
        self.email = InoutEmail(self.config)

    def generalReport(self, totalGeneralIncome, totalGeneralExpense, generalSavings):
        timeNow = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print('['+timeNow+']' + ' Generating report...')
        generalReport = '收入: {:.2f} 元\n'.format(totalGeneralIncome)
        generalReport += '支出: {:.2f} 元\n'.format(totalGeneralExpense)
        generalReport += '净流入: {:.2f} 元'.format(generalSavings)
        return generalReport

    def dailyReport(self):
        dailyEmail = self.email
        dailyIncome, dailyExpense, dailySavings = self.dailyData.dailySummary()
        dateReport = '截至 '+datetime.now().strftime('%Y-%m-%d %H:%M:%S')+' 二十四小时流水为:'+'\n'
        contentReport = self.generalReport(
            dailyIncome, dailyExpense, dailySavings)
        dailyReport = dateReport+contentReport
        print(dailyReport)
        sys.stdout.flush()
        dailyEmail.sendMail(dailyReport)

    def weeklyReport(self):
        weeklyEmail = self.email
        weeklyIncome, weeklyExpense, weeklySavings = self.weeklyData.weeklySummary()
        dateReport = '截至 '+datetime.now().strftime('%Y-%m-%d %H:%M:%S')+' 一周流水为:'+'\n'
        contentReport = self.generalReport(
            weeklyIncome, weeklyExpense, weeklySavings)
        weeklyReport = dateReport+contentReport
        print(weeklyReport)
        sys.stdout.flush()
        weeklyEmail.sendMail(weeklyReport)

    def monthlyReport(self):
        monthlyEmail = self.email
        monthlyIncome, monthlyExpense, monthlySavings = self.monthlyData.monthlySummary()
        dateReport = '截至 '+datetime.now().strftime('%Y-%m-%d %H:%M:%S')+' 一月流水为:'+'\n'
        contentReport = self.generalReport(
            monthlyIncome, monthlyExpense, monthlySavings)
        monthlyReport = dateReport+contentReport
        print(monthlyReport)
        sys.stdout.flush()
        monthlyEmail.sendMail(monthlyReport)

    def yearlyReport(self):
        yearlyEmail = self.email
        yearlyIncome, yearlyExpense, yearlySavings = self.yearlyData.yearlySummary()
        dateReport = '截至 '+datetime.now().strftime('%Y-%m-%d %H:%M:%S')+' 一年流水为:'+'\n'
        contentReport = self.generalReport(
            yearlyIncome, yearlyExpense, yearlySavings)
        yearlyReport = dateReport+contentReport
        print(yearlyReport)
        sys.stdout.flush()
        yearlyEmail.sendMail(yearlyReport)
    # expend to Bark notification
