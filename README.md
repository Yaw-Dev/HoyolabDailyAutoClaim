# Hoyolab Daily Rewards Auto Claim
A simple python script written to make the task of claiming dailies on genshin automatic!
> This possibly works for their other games as well but I haven't tested it.

Contributions are appreciated :)

## Setup:
1) Login to Hoyolab.com
2) Get all your cookies and input them in their respective places within the code (`hoyo_cookies`)
3) Go into the daily claim page and paste the url on `hoyolab_dailies_url` (line 6) | Not every part of it is needed:
 [check the reference image](https://i.e-z.host/0lkg6jl1.png)
4) Compile into an executable (recommended) or leave it as is.
- recommended command: *`pyinstaller autoclaim.py --onefile --icon NONE --noconsole`*
5) Open your **Task Scheduler** and setup the script to autorun under your prefered parameters.