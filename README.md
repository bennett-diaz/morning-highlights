# morning-highlights
Send a quote from your Kindle library to your mobile phone each morning to continuously reinforce what you have read

## Compatibility
Currently supported on MacOS only, since the scheduling capability is powered by a daemon on Mac's launchd. If you use a different OS, you will need to replace the daemon defined in `launchd.kindle.daemon.plist` with a cron job (for Linux) or Task Schedule job (for Windows).

## Instructions
# Export your Kindle highlights 
1. Plug your Kindle into your machine via USB
2. A drive titled Kindle should appear on your Desktop
3. Move the My Clippings.txt file to your Desktop
4. Eject the Kindle drive

# Install the program
1. Clone this repository
2. Move the `My Clippings.txt` file into your project folder.
3. Input the absolute file path of 'My Clippings.txt' to your .env file.
4. Input your Twilio API credentials and phone numbers into the .env file.
5. Run main.py in your IDE to ensure program is working

# Schedule daily SMS using a daemon
1. Navigate to the `launch.kindle.daemon.plist` file. Here is where you configure the behavior of your daemon.
2. Set the `StartCalendarInterval` key to the time to send the daily SMS
3. Set the `StandardErrorPath`, `StandardOutPath`, and `ProgramArguments` as directed in the file comments. 
3. If you have trouble with setup, I have a tutorial repo at simple-launchd-template<link>

# Deploy your daemon
1. Open your terminal 
2. Get your current user_id by running `id -u`
3. Run the daemon using `launchctl bootstrap gui/<user_id> <your absolute filepath to launchd.kindle.daemon.plist>`
4. Your daemon will run in the background whenever your machine is on and awake.
5. Terminate the daemon using `launchctl bootout gui/<user_id> <your absolute filepath to launchd.kindle.daemon.plist>`

## References
- https://www.twilio.com/blog/schedule-a-daily-sms-reminder-on-linux-macos-or-windows
