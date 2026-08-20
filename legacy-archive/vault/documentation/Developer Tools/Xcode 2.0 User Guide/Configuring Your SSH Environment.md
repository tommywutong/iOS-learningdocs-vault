---
title: Xcode 2.0 User Guide
apple_id: TP40001440
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2006-11-07'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/XcodeUserGuide20/Contents/Resources/en.lproj/SSHEnvironment/SSHEnvironment.html
archived_at: '2026-07-15T07:28:50.814107Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode 2.0 User Guide](Introduction%20to%20Xcode%202.0%20User%20Guide.md)


[Next](Document%20Revision%20History.md)[Previous](Using%20Subversion.md)

# Configuring Your SSH Environment

This appendix explains how to configure SSH
access from one computer (the server) to another (the client) for
a single user. This allows you to connect securely from your workstation
to the computer where your repository is located.

1. The server’s
   administrator must create a user account for you on that computer.
   Make sure you can log in to the server.

```
% ssh ernest@server.apple.com
ernest@server.apple.com's password:
Last login: Thu Sep 30 15:56:52 2004 from xx.xx.xx.xx
Welcome to Darwin!
```
2. If it doesn’t already exist, create the `.ssh` directory
   in your home directory in the server computer.

```shell
% mkdir ~/.ssh
% exit
```
3. Using the `ssh-keygen` command,
   create a private and public key pair and store it in your home directory
   in the client computer:

```shell
% ssh-keygen -t dsa
Generating public/private dsa key pair.
Enter file in which to save the key (/Volumes/Athene/ernest/.ssh/id_dsa:
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has ben saved in /Volumes/Athene/ernest/.ssh/id_dsa.
Your public key has been saved in /Volumes/Athene/ernest/.ssh/id_dsa.pub.
The key fingerprint is:
##:##:##:##:##:##:##:##:##:##:##:##:##:##:##:## ernest@work.apple.com
% cd ~/.ssh
% ls
id_dsa    id_dsa.pub    known_hosts
```
4. Using the `scp` command,
   copy the public key file (`id_dsa.pub`)
   to your home directory in the server as `authorized_keys` (unless
   the `authorized_keys` file
   already exists there):

```
% scp id_dsa.pub ernest@server.apple.com:~/.ssh/authorized_keys
ernest@server.apple.com's password:
id_dsa.pub                                100%  613     1.2MB/s    00:00
```

   If the `authorized_keys` file
   if it already exists, add your public key to it using a text editor.
5. Ensure you can connect to the server using your passphrase:

```
% ssh ernest@server.apple.com
Enter passphrase for key '/Users/ernest/.ssh/id_dsa':
Last login: Thu Sep 30 16:06:45 2004 from xx.xx.xx.xx
Welcome to Darwin!
```

[Next](Document%20Revision%20History.md)[Previous](Using%20Subversion.md)

