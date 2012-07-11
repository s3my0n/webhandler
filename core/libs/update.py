from subprocess import Popen, PIPE
from os import path, getcwd

from core.libs.menu import Colors


def update():
    if not path.exists(path.join(getcwd(), ".git")):
        errmsg = '\n[!]".git" directory doesn\'t exist here.'
        errmsg += '[!] Clone webhandler (e.g. git clone https://github.com/lnxg33k/webhandler.git webhandler)'
        print '{0}{1}{2}'.format(Colors.RED, errmsg, Colors.END)
    else:
        f = Popen('git rev-parse --short HEAD', shell=True, stdout=PIPE, stderr=PIPE)
        current_commit = f.communicate()[0]
        msg = '\n[+] WebHandler current commit: {0}'.format(current_commit)
        msg += '[+] Updating webhandler to the latest commit'
        msg += '\n[+] update in progress, please wait ..'
        print ('{0}{1}{2}'.format(Colors.GREEN, msg, Colors.END))
        f = Popen('git pull; git rev-parse --short HEAD', shell=True, stdout=PIPE, stderr=PIPE)
        out, err = f.communicate()
        if out and not err:
            msg = '[+] Updated successfully to {0}'.format(out.split()[-1])
            print '{0}{1}{2}'.format(Colors.GREEN, msg, Colors.END)
        else:
            errmsg = '\n[!] git is required to update webhandler from CLI'
            errmsg += '\n[!] To install it (e.g. sudo apt-get install git)'
            print '{0}{1}{2}'.format(Colors.RED, errmsg, Colors.END)
