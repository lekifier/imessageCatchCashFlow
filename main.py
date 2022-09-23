#!/opt/homebrew/bin/python3
import os
import sys
import argparse
import configparser
from datetime import datetime

from modules.schedulerModule import InoutScheduler


def configInit(configName):
    configPth = os.path.join(configName)
    config = configparser.ConfigParser()
    config.read(configPth)
    return config


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    defaultConfigPth = os.path.join(os.path.split(
        os.path.realpath(__file__))[0], 'catchCashFlow.cfg')
    nowTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print('['+nowTime+']'+' Load config file at '+defaultConfigPth)
    sys.stdout.flush()
    parser.add_argument('--config-pth', type=str, default=defaultConfigPth,
                        help='Config file path')
    args = parser.parse_args()
    config = configInit(args.config_pth)

    scheduler = InoutScheduler(config)
    scheduler.startScheduler()
