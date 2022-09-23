import os
import csv
from datetime import datetime
from .dataModule import DailyInoutData


class InoutAnalysis:
    def __init__(self, config):
        self.config = config
        self.data = DailyInoutData(config)

    def writeToNote(self):
        analysisPth = self.config['ANALYSISINFO']['analysisPth']
        noteDate = datetime.now().date()
        if not os.path.exists(analysisPth):
            with open(analysisPth, 'w') as note:
                writer = csv.writer(note)
                header = ["date", "income", "expense", "savings"]
                writer.writerow(header)
        with open(analysisPth, 'a') as note:
            writer = csv.writer(note)
            income, expense, savings = self.data.dailySummary()
            info = [str(noteDate), income, expense, savings]
            writer.writerow(info)
