from .queryModule import InoutQuery


class TimeInterval:
    daily = 1
    weekly = 7
    monthly = 30
    yearly = 365


class InoutData:
    def __init__(self, config):
        self.config = config
        self.query = InoutQuery(self.config)

    def incomeData(self, interval):
        income, _ = self.query.inout(interval)
        return income

    def expenseData(self, interval):
        _, expense = self.query.inout(interval)
        return expense


class DailyInoutData(InoutData):
    def dailyIncomeData(self):
        return self.incomeData(TimeInterval.daily)

    def dailyExpenseData(self):
        return self.expenseData(TimeInterval.daily)

    def dailySummary(self):
        income = sum(self.dailyIncomeData())
        expense = sum(self.dailyExpenseData())
        savings = income - expense
        return income, expense, savings


class WeeklyInoutData(InoutData):
    def weeklyIncomeData(self):
        return self.incomeData(TimeInterval.weekly)

    def weeklyExpenseData(self):
        return self.expenseData(TimeInterval.weekly)

    def weeklySummary(self):
        income = sum(self.weeklyIncomeData())
        expense = sum(self.weeklyExpenseData())
        savings = income - expense
        return income, expense, savings


class MonthlyInoutData(InoutData):
    def monthlyIncomeData(self):
        return self.incomeData(TimeInterval.monthly)

    def monthlyExpenseData(self):
        return self.expenseData(TimeInterval.monthly)

    def monthlySummary(self):
        income = sum(self.monthlyIncomeData())
        expense = sum(self.monthlyExpenseData())
        savings = income - expense
        return income, expense, savings


class YearlyInoutData(InoutData):
    def yearlyIncomeData(self):
        return self.incomeData(TimeInterval.yearly)

    def yearlyExpenseData(self):
        return self.expenseData(TimeInterval.yearly)

    def yearlySummary(self):
        income = sum(self.yearlyIncomeData())
        expense = sum(self.yearlyExpenseData())
        savings = income - expense
        return income, expense, savings
