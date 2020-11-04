# A quick introduction to `ssh`

## Connecting to a remote server

    ssh -p number user@remote_adress

## Copy directories and files using `scp`

Using `scp` command to copy files:

    scp -P 8888 ./teste.txt user@server2:directory/teste.txt

### From local to a remote server

*Keeps the same directory name*. Notice that we are not giving `/` after the local directory name.

    scp -r local/directory user@server2:/home/documents/

What happens if I didn't use `/` after `:` in the example above?

Options:

    -r means in a recursive way
    -P port number

To validate the transfer on the remote server

    ll /home/documents/directory

*Changing the directory name* in the remote server:

    scp -r /localdocs/directory/* user@server2:/whatever/path/you/want/

As one can notice, the forward-slash `/` is important for `scp`. Don't forget it.

### From remote server to local

Keeping the "same" directory name.

    scp -r user@host:whatever/path/you/inform  /my_local/directory/

The remote path doesn't has a forward slash `/` after the source directory in order to keep the same directory name in the local copy -- in this example the local directory name will be `inform`.

Changing the directory name. As a matter of fact, it copies all the files and subdirectories from a directory in a remote server to a new directory in local.

    scp -r user@remotehost:/home/documents/directory/*  /home/documents/newer_directory/

## Copy directories and files using `rsync`

Once we've learned how to use `scp` the `rsync` command is pretty straightforward.

---

I got to know all this content from this blog post: <https://www.golinuxcloud.com/ssh-copy-folder-local-to-remote-server-linux>. Accessed in November 3th, 2020.
