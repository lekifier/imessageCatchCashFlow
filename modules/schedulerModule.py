import schedule
import sys
import shutil
from datetime import datetime
from .reportModule import InoutReport
from .analysisModule import InoutAnalysis


class InoutScheduler:
    def __init__(self, config):
        self.config = config
        self.report = InoutReport(self.config)
        self.analysis = InoutAnalysis(self.config)
        self.dailyReportTime = config['SCHEDULERINFO']['DailyReportTime']
        self.weeklyReportTime = config['SCHEDULERINFO']['WeeklyReportTime']
        self.monthlyReportTime = config['SCHEDULERINFO']['MonthlyReportTime']
        self.yearlyReportTime = config['SCHEDULERINFO']['YearlyReportTime']
        self.logClearTime = config['LOGINFO']['LogClearTime']
        self.analysisTime = config['SCHEDULERINFO']['AnalysisTime']

    def clearLog(self):
        shutil.rmtree(self.config['LOGINFO']['LogPth'])

    def aliveDetect(self):
        time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print('['+time+']'+" Core service is alive")
        sys.stdout.flush()

    def schedulerManage(self):
        # Report schedule
        if self.config['DEBUG']['MODE'] == 'debug':
            schedule.every(300).seconds.do(self.aliveDetect)
            # schedule.every(12).seconds.do(self.clearLog)
        schedule.every().day.at(self.dailyReportTime).do(self.report.dailyReport)
        schedule.every().day.at(self.dailyReportTime).do(self.clearLog)
        schedule.every().sunday.at(self.weeklyReportTime).do(self.report.weeklyReport)
        schedule.every(30).days.at(self.monthlyReportTime).do(
            self.report.monthlyReport)
        schedule.every(365).days.at(self.yearlyReportTime).do(
            self.report.yearlyReport)
        # Analysis schedule
        schedule.every().day.at(self.analysisTime).do(self.analysis.writeToNote)

    def startScheduler(self):
        self.schedulerManage()
        # email notification the service has started
        while True:
            schedule.run_pending()

    def testScheduler(self):
        self.schedulerManage()
        # schedule.run_all()
