# morning-highlights
Send a quote from your Kindle library to your mobile phone each morning to continuously reinforce what you have read

## Compatibility
Currently supported on MacOS only, since the scheduling capability is powered by a daemon on **launchd**. If you use a different OS, you will need to replace the daemon defined in `launchd.kindle.daemon.plist` with a **cron job** for Linux or **Task Scheduler** job for Windows.

## Instructions
### Export your Kindle highlights 
1. Plug your Kindle into your machine via USB
2. A drive titled Kindle should appear on your Desktop
3. Move the My Clippings.txt file to your Desktop
4. Eject the Kindle drive

### Install the program
1. If you don't have Python installed, [install it from here](https://www.python.org/downloads/)
2. Clone this repository
3. Navigate to the project folder and create a virtual environment
4. Install package dependencies via `pip3 install -r requirements.txt`
5. Move the `My Clippings.txt` file into your project folder
6. Input the absolute file path of 'My Clippings.txt' to your .env file
7. Input your Twilio API credentials and phone numbers into the .env file
8. Run main.py in your IDE to ensure program is working

### Schedule daily SMS using a daemon
1. Navigate to the `launch.kindle.daemon.plist` file. Here is where you configure the behavior of your daemon
2. Set the `StartCalendarInterval` key to the time to send the daily SMS
3. Set the `StandardErrorPath`, `StandardOutPath`, and `ProgramArguments` as instructed in the file comments
3. If you have trouble with setup, check out my launchd tutorial at [simple-launchd-template](https://github.com/bennett-diaz/simple-launchd-template)

### Deploy your daemon
1. Configure the `launchd.kindle.daemon.plist` file as instructed the file comments
2. Open your terminal 
3. Get your current user_id by running `id -u`
4. Run the daemon using `launchctl bootstrap gui/<user_id> <your absolute filepath to launchd.kindle.daemon.plist>`
5. Your daemon will run in the background whenever your machine is on and awake
6. Terminate the daemon using `launchctl bootout gui/<user_id> <your absolute filepath to launchd.kindle.daemon.plist>`

## References
- https://www.twilio.com/blog/schedule-a-daily-sms-reminder-on-linux-macos-or-windows
