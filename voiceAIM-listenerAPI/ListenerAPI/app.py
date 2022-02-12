from flask import Flask
from snippets.packagemanager import package_manager 
from snippets.servicemanager import service_manager 
from snippets.usermanager import user_manager
from snippets.inframanager import infra_manager

import subprocess


app = Flask(__name__)

def listener(voicetext):
    reply = 'Done!!'
    try:
        if "package" in voicetext:
            task = "package"
        elif "service" in voicetext:
            task = "service"
        elif "user" in voicetext:
            task = "user"
        elif "infra" in voicetext:
            task = "infra"
        
        print("INVOKED:--> "+ task +"_manager(voicetext)")
        exec(task+"_manager(voicetext)")
    except Exception as e:
        print(f"Invalid Command...Mind your words...\n\n{e}")

    return reply


@app.route("/<command>")
def index(command):
    voicetext = command.lower()
    print("\n\nVOICE TEXT:--> "+ voicetext)
    reply =  listener(voicetext)
    print("REPLY:--> "+ reply, end="\n\n")
    return reply



if __name__ == "__main__":
    host = "0.0.0.0"
    port = 5000
    debug = True
    app.run(host, port, debug)
