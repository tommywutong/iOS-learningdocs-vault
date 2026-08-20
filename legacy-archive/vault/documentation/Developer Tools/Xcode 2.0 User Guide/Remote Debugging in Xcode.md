---
title: Xcode 2.0 User Guide
apple_id: TP40001440
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2006-11-07'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/XcodeUserGuide20/Contents/Resources/en.lproj/db_remote_debug/db_remote_debug.html
archived_at: '2026-07-15T07:29:22.923790Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode 2.0 User Guide](Introduction%20to%20Xcode%202.0%20User%20Guide.md)


[Next](Customizing%20Xcode.md)[Previous](Using%20Fix%20and%20Continue.md)

# Remote Debugging in Xcode

Xcode’s integrated debugger supports remote
graphical debugging when debugging with GDB. Remote debugging lets
you debug a program running on another computer. This is good for
programs that you cannot easily debug on the host on which they
are running. For example, you may be trying to debug a full-screen
application, such as a game, or a problem with event handling in
your application’s GUI. Interacting with the debugger on the same
computer interferes with the execution of the program you are trying
to debug. In these cases, you have to debug the program remotely.

With Xcode’s remote graphical debugging, you can debug a
program running on a remote machine within the Xcode debugger, as
you would any local executable, without resorting to the command-line.

This chapter introduces remote debugging in Xcode and walks
you through enabling remote debugging in Xcode. To set up your project
for remote debugging, you must perform the steps described in the
following three sections:

1. [Configuring Remote Login](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmruguwugrkhi5ceorkf) describes
   how to configure your local computer and the remote host to allow
   remote login using SSH public key authentication.
2. [Creating a Shared Build Location](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmruguwugrkhjjeukq2c) describes how to set up a
   shared build directory that both computers can access via the same
   path.
3. [Configuring Your Executable for Remote Debugging](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmruguwugrkhi5ceorkj) describes how
   to configure the executable of the program you wish to debug for
   remote debugging in Xcode.

Remote debugging in Xcode relies on SSH public key authentication
to create a secure connection with the remote computer. To facilitate
authentication, Xcode integrates with `ssh-agent`.
This lets you use encrypted private keys for added security without
having to re-enter your passphrase each time Xcode establishes a
connection to the remote host. If you already use a third party
utility to set up the environment variables used by `ssh-agent`,
Xcode attempts to use those settings. Otherwise, Xcode uses its
own agent for authentication.

Before starting a remote debugging session, you need to be
able to login to the remote computer. To do this, you must:

1. Enable remote
   login on the computer that will host the program being debugged.
   In the Sharing pane of System Preferences, under “Services,”
   select Remote Login. This allows access to the remote computer via
   SSH.
2. Ensure that you can connect to the remote host using SSH public
   key authentication. If you are unsure whether you are using SSH
   public key authentication, you can test this by logging in to the
   remote computer with `ssh`.
   If you are prompted for the user’s password, you are not using
   public key authentication. If you are prompted for a passphrase—or
   for nothing at all—you are already using public key authentication.

If you are not set up to log in to the remote host using SSH
public key authentication, you need to create a public/private key
pair, and configure the local and host computers to use it. You
can do so with the following steps:

1. Generate
   a public / private key pair using `ssh-keygen`.
   On the command line, type the following line:

   `ssh-keygen
   -b 2048 -t dsa`

   This generates
   2048-bit DSA keys. You should see output similar to the following:

```
Generating public/private dsa key pair.
Enter file in which to save the key (/Users/admin/.ssh/id_dsa):
/Users/admin/.ssh/id_dsa already exists.
Overwrite (y/n)? y
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /Users/admin/.ssh/id_dsa.
Your public key has been saved in /Users/admin/.ssh/id_dsa.pub.
The key fingerprint is:
```
2. Copy the public key to the `authorized_keys` file
   on the remote computer. This file is usually stored at `~/.ssh/authorized_keys`.
   If the `authorized_keys` file
   already exists on the remote computer, be careful not to overwrite
   the file. You can add the public key, which is stored in the file
   you specified to `ssh-keygen` (`id_dsa.pub` by
   default), by entering the following on the command line:

   `cat
   id_dsa.pub >>! ~/.ssh/authorized_keys`
3. Make sure that the `authorized_keys` file
   is not readable by anybody else. Change the permissions on the file
   by entering the following on the command line:

   `chmod
   go-rwx ~/.ssh/authorized_keys`
4. Test the connection by logging in to the remote computer using `ssh`.
   From the command-line, type “`ssh` _username_`@`_hostname_”.
   Ensure that you are not asked for the user’s password. If you
   did not leave it empty in Step 1, you should be prompted for your passphrase,
   as in the following example:

   `Enter passphrase
   for key '/Users/admin/.ssh/id_dsa':`

If you are debugging a GUI application, you must be logged
into the remote computer as the same user that you connect to using `ssh`.
This user must have permission to read the build products.

For remote debugging to work, both computers—both the local
computer running Xcode and the remote host running the program you
are debugging—must have access to your project’s build products
and intermediate files via the same access path. You can do this
in either of two ways:

- Create a
  single shared location. This is easiest with a network home directory,
  although you can use any shared folder that both computers can access.
  In Xcode, set the build products and intermediates location to this
  shared folder. If necessary, create symlinks to the build folder
  on the remote host so the path to the build products is the same
  on both computers. For details on how to set the location of the
  build folder in your Xcode project, see [Build Locations](Building%20a%20Product.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydqmztfvbecssdjfeugqy).
- Copy the files to the remote host. Alternatively, you can
  copy the build products and intermediate files over to the remote
  host after each build, although this is considerably less convenient.
  These must be located at the same path on the remote computer.

Once you have configured both computers to allow for remote
login and set up a common build products location, the last step
is configuring the executable you want to debug remotely. You may
consider creating a separate custom executable environment for remote
debugging. Using separate executable environments, you can specify
different options for debugging remotely and debugging locally and
easily switch between the two modes.

To configure an executable for remote debugging:

1. Select the
   executable and open an inspector or Info window. Click Debugging
   to open the debugging pane.
2. Make sure that “GDB” is selected in the “When using”
   pop-up menu at the top of the Debugging pane. Select the option
   for “Debug executable remotely via SSH.” In the Host field,
   type in the user you will log in as and the address of the remote
   host; for example, “`admin@cowpuppy.apple.com`.”
3. From the “Use _<device>_ for standard
   input /output” menu, choose “Pipe.”

To start a remote debugging session, make sure the active
executable is correctly set, then build and debug your product as
normal. Before it launches the executable, Xcode displays an authentication
dialog that asks you to type in your passphrase. After you have authenticated
once, Xcode does not prompt you for your pass phrase again until
the next time you initiate a remote debugging session after restarting
Xcode.

If you are experiencing problems debugging on the remote host,
look in the debugger console for error messages. To view the debugger
console, choose Debugger > Console Log.

[Next](Customizing%20Xcode.md)[Previous](Using%20Fix%20and%20Continue.md)

