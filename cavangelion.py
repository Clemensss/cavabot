import atexit
from flask import Flask
from flask import request
from flask import render_template
import tweepy
import re
from random import randrange
from apscheduler.schedulers.background import BackgroundScheduler


app = Flask(__name__, 
	    static_url_path='',
	    static_folder='/templates')

@app.route('/')
def hellow():
    return render_template('base.html')

@app.route('/goman', methods=['POST', 'GET'])
def theServer():
    if request.method == 'POST':
        doTheThing(request)
        print(tuite)
        return render_template('vlw.html')
def job_function():
    tweeteDaShit()

scheduler = BackgroundScheduler()
scheduler.add_job(func=job_function, trigger="interval", seconds=30)
scheduler.start()

#@cron.interval_schedule(hours=24)
atexit.register(lambda: scheduler.shutdown())

# Shutdown your cron thread if the web process is stopped

if __name__ == '__main__':
    app.run()

sim = "sim! cava viu evangelion hoje"
nao = "cava nao viu evangelion hoje"
chorou = False
tuite = nao
simhj = False

def tweeteDaShit():
    # Authenticate to Twitter

    auth = tweepy.OAuthHandler("yThtDD41cHPCYkvnItxAVsFYA", 
        "ONbfTVBvwdb5cvQQBoDcqmQfUxOAG61iEYaJ2x8uVhA6UzdGyu")
    auth.set_access_token("1249863058408837121-EoFzySDnu9R9vwwTuY11w2IGzoDgy2",
        "CMf4RSr7DFWIlSsXh5lBnMk3ngLsQ7Kkzpj0xOhdVpmrO")
    api = tweepy.API(auth)

    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")

    # Create API object
    api = tweepy.API(auth, wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True)

    oBotFazCoisas(api, get_quote())

def oBotFazCoisas(api, quote):
    global chorou
    global nao
    global tuite

    if chorou:
       tuite = tuite + " e ainda chorou" 
    
    tuite = "{0}\n\n{1}".format(tuite, quote)
    api.update_status(tuite)

    chorou = False
    tuite = nao

def clean_quote(quote):
    return quote.replace(r'\N', r' ')

def get_quote():
    quote = None

    with open('legendas.txt', 'r') as subs:
        lines = subs.readlines()
        randnum = randrange(len(lines)) 
        quote = lines[randnum] 
        quote = quote.strip("\n")
        return clean_quote(quote)

def doTheThing(request):
    global sim
    global nao
    global tuite
    global chorou
    global simhj

    print(request.form)
    if not simhj:
        if request.form.get("1question") == 'sim':
            tuite = sim 
            simhj = True
        if request.form.get('2question') == 'sim':
            if tuite == sim:
                chorou = True

