import subprocess

def user_manager(voicetext): #create user harry
    text = voicetext.strip().lower().split()
    name = text[text.index("user")+1]
    action = text[text.index("user")-1]
    
    
    if action in ("create", "add"):
        ansible_data = '''
- hosts: localhost
  tasks:
    - name: "Adding User..."
      user:
        name: "{}"
        generate_ssh_key: yes
        ssh_key_bits: 2048
        ssh_key_file: .ssh/id_rsa
        '''.format(name)
    elif action in ("remove", "delete"):
        ansible_data = '''
- hosts: localhost
  tasks:
    - name: "removing User..."
      user:
        name: "{}"
        state: absent
        remove: yes
        '''.format(name)
        
    with open("./playbooks/user_manager.yml","w") as f:
        f.write(ansible_data)

    output = subprocess.getoutput("ansible-playbook ./playbooks/user_manager.yml")
    return(output)
