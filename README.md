# morning-highlights
Send a quote from your Kindle library to your mobile phone each morning to continuously reinforce what you have read

## Compatibility
Currently supported on MacOS only, since the scheduling capability is powered by a daemon on Mac's launchd. If you use a different OS, you will need to replace the daemon defined in `launchd.kindle.daemon.plist` with a cron job (for Linux) or Task Schedule job (for Windows).

## Instructions
# Export your Kindle highlights 
1. Plug your Kindle into your machine via USB
2. A 'Kindle' drive should appear on your Desktop
3. Move the 'My Clippings.txt' file to your Desktop.
4. Eject your Kindle

# Install the program
1. Clone this repository
2. Move the 'My Clippings.txt' file into your project folder.
3. Input the absolute file path of 'My Clippings.txt' to your .env file.
4. Input your Twilio API credentials and phone numbers into the .env file.
5. TBD

## References
- https://www.twilio.com/blog/schedule-a-daily-sms-reminder-on-linux-macos-or-windows
