# A quick introduction to `ssh`

## Connecting

    ssh -p number user@remote_adress

## Copy directories and files between local and remote server

Use `scp` command

    scp -r local/directory user@server2:home/directory

     scp -P 9048 ./README.md giliardalmeida@200.134.18.71:projects/README.md


---

I got to know all this content from this blog post <https://www.golinuxcloud.com/ssh-copy-folder-local-to-remote-server-linux>. Acessed in November 3th, 2020.
