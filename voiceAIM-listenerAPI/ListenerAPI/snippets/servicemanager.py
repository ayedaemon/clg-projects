import subprocess


def service_manager(voicetext):
    text = voicetext.strip().lower().split()
    name = text[text.index("service")+1]
    state = text[text.index("service")-1]
    
    if state in ("start", "started"):
        state = "started"
    elif state in ("stopped","stop"):
        state = "stopped"
    elif state in ("restart", "restarted"):
        state = "restarted"
        
        
    ansible_data = '''
    - hosts: localhost
      tasks:
        - name: "Handling Service... "
          service:
            name: "{0}"
            state: "{1}"
    '''.format(name, state)

    with open("./playbooks/service_manager.yml","w") as f:
        f.write(ansible_data)

    output = subprocess.getoutput("ansible-playbook ./playbooks/service_manager.yml")
    return(output)
