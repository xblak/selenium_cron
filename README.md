# selenium_cron

testing selenium\
stay healthy\
To use it, fork to a new repo, go to settings->secrets->Repository secrets\
add your USERNAME, PASSWORD, and the magical URL (make sure all UPPERCASE)\
You can change the scheduled time (UTC) in selenium_cron/.github/workflows/cron.yml. \
'0 8 * * *' means it will run at 0 minute, 8 am, every day(month), every month, every day(week) \
'0 8 * * 1-5' only weekdays\
'0 8 * * 1,3,5' only MWF\
'0 8 * * 2,4' only TTH
