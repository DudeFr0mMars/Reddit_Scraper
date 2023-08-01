So to get started the first thing you need is a Reddit account, If you don’t have one you can go and make one for free.

The next step is to install Praw and Fire. Praw is an API which lets you connect your python code to Reddit .

To install praw all you need to do is open your command line and install the python package praw.

pip install praw
pip install fire

The next step after making a Reddit account and installing praw is to go to this page and click create app or create another app and select script. 

https://www.reddit.com/prefs/apps

In the form that will open, you should enter your name, description and uri. For the redirect uri you should choose http://localhost:8080

"secret" is your client_secret, "name" is your user_agent and the text below "script" is your client_id
