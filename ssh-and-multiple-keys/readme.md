# SSH
Used to connect to a remote computer, by default the user name used is the current user name of the system
```
ssh domain.name.com
```
for any other user name need to specify the username
```
ssh username@domain.name.com
```

## SSH Keys:  [[Credits]](https://youtu.be/33dEcCKGBO4?si=rwWkNkj_0tY1t6O8)
to generate ssh key pair, by default it makes it in `$HOME/.ssh`,use th following to generate the ssh key
```
ssh-keygen -b 4096
```
after this give a path+name for saveing, default may overwrite an exiting, after filling in all the required field two files will be created
1. filename - this is the private key
2. filename.pub - this is the public key

to copy the public key to the required server use
```
ssh-copy-id username@domain.name.com
```
after its coppied you can directly ssh into the machine and it will only ask for the passphrase for the generated key if any was set


## Multiple ssh keys: [[Credits]](https://youtu.be/pE3EuiyShoM?si=bflu6eF4VQvLBnIh)
for generating second key need to give custom path+name
to copy the ssh keys to the respective servers used the following
```
ssh-copy-id -i <path-to-key> <username>@<server-address>
```
do this for each servers to copy the keys; to not have to specify all the details everytime you can use ssh config which is of the following format
```
Host <alias-name>
    Hostname <domain.name.com>
    User <username>
    Port <port-number>
    IdentityFile <path-to-ssh-private-key>
```
using this will only prompt for the key passphrase, if you want to avaid that too use can run the ssh-agent in the backgroud using `eval $(ssh-agent)` this will print the process id for the service, then add then add the keys using `ssh-add <private-key-path>` and then enter your passphrase and till the terminal is open you wont be promted for the passphrase in the that teminal shell
