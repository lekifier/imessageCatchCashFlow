#!/bin/bash
pip3 install -r requirements.txt
cp $(pwd)/com.catchcashflow.refreshchatdb.plist ~/Library/LaunchAgents/com.catchcashflow.refreshchatdb.plist
cp $(pwd)/com.catchcashflow.core.plist ~/Library/LaunchAgents/com.catchcashflow.core.plist
cd ~/Library/LaunchAgents
launchctl load com.catchcashflow.*