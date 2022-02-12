import subprocess

def package_manager(voicetext):
    text = voicetext.strip().lower().split()
    name = text[text.index("package")+1]
    state = text[text.index("package")-1]
    if state in ("install", "present", "download"):
        state = "present"
    else:
        state = "absent"

    ansible_data = '''
    - hosts: localhost
      tasks:
        - name: "Handling package... "
          package:
            name: "{0}"
            state: "{1}"
    '''.format(name, state)

    with open("./playbooks/package_manager.yml","w") as f:
        f.write(ansible_data)

    output = subprocess.getoutput("ansible-playbook ./playbooks/package_manager.yml")
    return(output)
