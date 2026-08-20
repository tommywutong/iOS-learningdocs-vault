---
title: Xcode Debugging Guide
apple_id: TP40007057
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2011-03-08'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/XcodeDebugging/300-Debugging_Programs_Remotely/remote_debugging.html
archived_at: '2026-07-15T07:28:00.977851Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode Debugging Guide](Introduction.md)


[Next](Mac%20OS%20X%20Low-Level%20Debugging.md)[Previous](Modifying%20Running%20Code.md)

# Debugging Programs Remotely

With remote graphical debugging in Xcode, you can debug a program running on another computer as you would any local executable, without resorting to the command line. Use remote debugging when you cannot easily debug your program on the computer that it is running on. For example, you may be trying to debug a full-screen application, such as a game, or a problem with event handling in your application’s GUI. Interacting with the debugger on the same computer interferes with the execution of the program you are trying to debug. In these cases, you have to debug the program remotely.

This chapter introduces remote debugging in Xcode and walks you through enabling remote debugging in Xcode. To set up your project for remote debugging, you must perform the steps described in the following sections:

- [Configuring Remote Log-in](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tanjxfvbuqmjrfvjvomzs) describes how to configure your local computer and the remote host to allow remote login using SSH public key authentication.
- [Creating a Shared Build Location](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tanjxfvbuqmjrfvjvomzt) describes how to set up a shared build directory that both computers can access via the same path.
- [Configuring an Executable for Remote Debugging](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tanjxfvbuqmjrfvjvomzu) describes how to configure the executable of the program you wish to debug for remote debugging in Xcode.

Remote debugging in Xcode relies on SSH public key authentication to create a secure connection with the remote computer. To facilitate authentication, Xcode integrates with `ssh-agent`. This lets you use encrypted private keys for added security without having to reenter your passphrase each time Xcode establishes a connection to the remote host. If you already use a third-party utility to set up the environment variables used by `ssh-agent`, Xcode attempts to use those settings. Otherwise, Xcode uses its own agent for authentication.

Before starting a remote debugging session, you need to be able to log in to the remote computer. To do this, you must:

1. Turn on remote login on the computer that will host the program being debugged.

   In System Preferences, choose Sharing, Remote Login.
2. Ensure that you can connect to the remote host using SSH public key authentication.

   If you are unsure whether you are using SSH public key authentication, you can test this by logging in to the remote computer with `ssh`.

   - If you are prompted for the user’s password, you are not using public key authentication.
   - If you are prompted for a passphrase—or for nothing at all—you are already using public key authentication.

If you are not set up to log in to the remote host using SSH public key authentication, you need to create a public/private key pair, and configure the local and host computers to use it. You can do so with the following steps:

1. Generate a public and private key pair using `ssh-keygen`.

   On the command line, type the following line:

   `ssh-keygen -t dsa`

   You should see output similar to the following:

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
2. Copy the public key to the `authorized_keys` file on the remote computer.

   This file is usually stored at `~/.ssh/authorized_keys`. If the `authorized_keys` file already exists on the remote computer, be careful not to overwrite the file. You can add the public key, which is stored in the file you specified to `ssh-keygen` (`id_dsa.pub` by default), by entering the following on the command line:

   `cat id_dsa.pub >> ~/.ssh/authorized_keys`
3. Make sure that the `authorized_keys` file is not readable by anybody else.

   Change the permissions on the file by entering the following on the command line:

   `chmod go-rwx ~/.ssh/authorized_keys`
4. Test the connection by logging in to the remote computer using `ssh`.

   From the command-line, type `ssh <username>@<hostname>`. Ensure that you are not asked for the user’s password. If you did not leave it empty in step 1, you should be prompted for your passphrase, as in the following example:

   `Enter passphrase for key '/Users/admin/.ssh/id_dsa':`

If you are debugging a GUI application, you must be logged in to the remote computer as the same user that you connect to using `ssh`. This user must have permission to read the build products.

For remote debugging to work, both computers—both the local computer running Xcode and the remote host running the program you are debugging—must have access to your project’s build products and intermediate files. You can do this in either of two ways:

- __Create a single shared location.__ This is easiest with a network home directory, although you can use any shared folder that both computers can access. In Xcode, set the build products and intermediates location to this shared folder. If necessary, create symbolic links to the build folder on the remote host so the path to the build products is the same on both computers. For details on how to set the location of the build folder in your Xcode project, see [Build Locations](../Xcode%20Project%20Management%20Guide/Building%20Products.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmojtfvjvomjq).
- __Copy the files to the remote host.__ Alternatively, you can copy the build products and intermediate files over to the remote host after each build, although this is considerably less convenient. These files must be located at the same path on the remote computer.

After you have configured both computers to allow for remote login and have set up a common build products location, the last step is configuring the executable you want to debug remotely. You may consider creating a separate custom executable environment for remote debugging. Using separate executable environments, you can specify different options for debugging remotely and debugging locally and easily switch between the two modes.

See [Executable-Environment Debugging Information](../Xcode%20Project%20Management%20Guide/Defining%20Executable%20Environments.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmojyfvbuuqsjinduusi) to learn how to configure an executable for remote debugging.

To start a remote debugging session, make sure the active executable is correctly set, then build and debug your product as normal. Before it launches the executable, Xcode displays an authentication dialog that asks you to type in your passphrase. After you have authenticated once, Xcode does not prompt you for your passphrase again until the next time you initiate a remote debugging session after restarting Xcode.

If you are experiencing problems debugging on the remote host, look in the console for error messages. To view the console, choose Run > Console.

[Next](Mac%20OS%20X%20Low-Level%20Debugging.md)[Previous](Modifying%20Running%20Code.md)

