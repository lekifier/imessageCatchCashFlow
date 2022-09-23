# coding=utf-8
import re
import sqlite3


class InoutQuery:
    def __init__(self, config):
        self.config = config
        self.dbPath = self.config['DATABASE']['DBUrl']
        self.targetKeyword = self.config['MESSAGEINFO']['TargetKeyword']
        self.incomeKeyword = self.config['MESSAGEINFO']['IncomeKeyword']
        self.expenseKeyword = self.config['MESSAGEINFO']['ExpenseKeyword']
        self.generalSQL = '''SELECT * FROM message
                            WHERE datetime(CURRENT_TIMESTAMP, 'localtime') <
                            datetime((date/1e9+978307200)+24*3600*{}+30
                            , 'unixepoch', 'localtime')
                            AND text like '%{}%{}%';'''

    def infoParser(self, msgs):
        infoList = []
        for msg in msgs:
            info = re.findall(r'\d+\.\d+', msg[2])
            infoList.append(float(info[0]))
        return infoList

    def msgsQuery(self, dbConnect, interval, targetKeyword, businessKeyword):
        msgs = dbConnect.cursor()
        msgs.execute(self.generalSQL.format(
            interval, targetKeyword, businessKeyword))
        return msgs

    def inout(self, interval):
        dbConnect = sqlite3.connect(self.dbPath)
        incomeMsgs = self.msgsQuery(dbConnect, interval, self.targetKeyword,
                                    self.incomeKeyword)
        expenseMsgs = self.msgsQuery(dbConnect, interval, self.targetKeyword,
                                     self.expenseKeyword)
        income = self.infoParser(incomeMsgs)
        expense = self.infoParser(expenseMsgs)
        dbConnect.close()
        return income, expense
