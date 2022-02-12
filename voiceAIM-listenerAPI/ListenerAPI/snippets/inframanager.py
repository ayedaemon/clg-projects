import subprocess

def infra_manager(voicetext):
    text = voicetext.strip().lower().split()
    todo = text[text.index("infra")-1]
    infra_code = text[text.index("infra")+1]

    if todo in ("create", "apply"):
        todo = "apply"
    elif todo in ("remove", "destroy", "delete"):
        todo = "destroy"

    print("\n\n INFRA: "+ todo +"  "+ infra_code)
    init = subprocess.getoutput(f"terraform init ./terraform_proj/{infra_code}")
    print(init)
    print(f"terraform {todo} --auto-approve ./terraform_proj/{infra_code}")
    
    output = subprocess.getoutput(f"terraform {todo} --auto-approve ./terraform_proj/{infra_code}")
    return(output)
