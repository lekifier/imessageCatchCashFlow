#!/usr/bin/osascript
-- TODO - (Option) if you want a notification when the chat.db file refreshed uncomment it.
-- display notification "" with title "iMessage database refresh" subtitle "Have a nice day!" sound name "Frog"
-- display notification "" with title "iMessage database refresh" subtitle "Have a nice day!"
set systemvolume to alert volume of (get volume settings)
-- debug the alert sound
--log (get volume settings)
set volume alert volume 0
-- debug the alert sound
--log (get volume settings)
tell application "Finder"
	-- TODO - change this to your own path
	duplicate "Macintosh HD:Users:yourname:Library:Messages:chat.db" to "Macintosh HD:Users:path:to:imessageCatchCashFlow:DB" with replacing
	duplicate "Macintosh HD:Users:yourname:Library:Messages:chat.db-wal" to "Macintosh HD:Users:path:to:imessageCatchCashFlow:DB" with replacing
	duplicate "Macintosh HD:Users:yourname:Library:Messages:chat.db-shm" to "Macintosh HD:Users:path:to:imessageCatchCashFlow:DB" with replacing
end tell
set volume alert volume systemvolume
-- debug the alert sound
--log (get volume settings)
set timedate to current date
log "[" & timedate & "]" & " File chat.db has refreshed"