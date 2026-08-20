---
title: Secure Coding Guide
apple_id: TP40002415
resource_type: Guide
platform: macOS
topic: Security
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Security/Conceptual/SecureCodingGuide/Articles/AccessControl.html
archived_at: '2026-07-18T02:06:18.237857Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Secure Coding Guide](Introduction%20to%20Secure%20Coding%20Guide.md)


[Next](Designing%20Secure%20User%20Interfaces.md)[Previous](Race%20Conditions%20and%20Secure%20File%20Operations.md)

# Elevating Privileges Safely

By default, applications run as the currently logged in user. Different users have different rights when it comes to accessing files, changing systemwide settings, and so on, depending on whether they are admin users or ordinary users. Some tasks require additional privileges above and beyond what even an admin user can do by default. An application or other process with such additional rights is said to be running with elevated privileges. Running code with root or administrative privileges can intensify the dangers posed by security vulnerabilities. This chapter explains the risks, provides alternatives to privilege elevation, and describes how to elevate privileges safely when you can’t avoid it.

Regardless of whether a user is logged in as an administrator, a program might have to obtain administrative or root privileges in order to accomplish a task. Examples of tasks that require elevated privileges include:

- manipulating file permissions, ownership
- creating, reading, updating, or deleting system and user files
- opening privileged ports (those with port numbers less than 1024) for TCP and UDP connections
- opening raw sockets
- managing processes
- reading the contents of virtual memory
- changing system settings
- loading kernel extensions

If you have to perform a task that requires elevated privileges, you must be aware of the fact that running with elevated privileges means that if there are any security vulnerabilities in your program, an attacker can obtain elevated privileges as well, and would then be able to perform any of the operations listed above.

Any program can come under attack, and probably will. By default, every process runs with the privileges of the user or process that started it. As a result, if an attacker uses a buffer overflow or other security vulnerability (see [Types of Security Vulnerabilities](Types%20of%20Security%20Vulnerabilities.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdkmrzfvjvomq)) to execute code on someone else’s computer, they can generally run their code with whatever privileges the logged-in user has.

If a user has logged on with restricted privileges, your program should run with those restricted privileges. This effectively limits the amount of damage an attacker can do, even after successfully hijacking your program into running malicious code. Do not assume that the user is logged in with administrator privileges; you should be prepared to run a helper application with elevated privileges if you need them to accomplish a task. However, keep in mind that, if you elevate your process’s privileges to run as root, an attacker can gain those elevated privileges and potentially take over control of the whole system.

If an attacker can gain administrator privileges, they can elevate to root privileges and gain access to any data on the user’s computer. Therefore, it is good security practice to log in as an administrator only when performing the rare tasks that require admin privileges. Because the default setting for macOS is to make the computer’s owner an administrator, you should encourage your users to create a separate non-admin login and to use that for their everyday work. In addition, if possible, you should not require admin privileges to install your software.

The idea of limiting risk by limiting access goes back to the “need to know” policy followed by government security agencies (no matter what your security clearance, you are not given access to information unless you have a specific need to know that information). In software security, this policy is often called the principle of least privilege.

The principle of least privilege states:

**“Every program and every user of the system should operate using the least set of privileges necessary to complete the job.”**
: —Saltzer, J.H. AND Schroeder, M.D., “The Protection of Information in Computer Systems,” _Proceedings of the IEEE_, vol. 63, no. 9, Sept 1975.

In practical terms, the principle of least privilege means you should avoid running as root, or—if you absolutely must run as root to perform some task—you should run a separate helper application to perform the privileged task (see [Writing a Privileged Helper](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdkobzfvjvomq)). Also, to the extent possible your software (or portions thereof) should run in a sandbox that restricts its privileges even further, as described in [Designing Secure Helpers and Daemons](Designing%20Secure%20Helpers%20and%20Daemons.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdimjvfvbuqmrnknltc).

By running with the least privilege possible, you:

- Limit damage from accidents and errors, including maliciously introduced accidents and errors
- Reduce interactions of privileged components, and therefore reduce unintentional, unwanted, and improper uses of privilege (side effects)

Keep in mind that, even if your code is free of errors, vulnerabilities in any libraries your code links in can be used to attack your program. For example, no program with a graphical user interface should run with privileges because the large number of libraries used in any GUI application makes it virtually impossible to guarantee that the application has no security vulnerabilities.

There are a number of ways an attacker can take advantage of your program if you run as root. Some possible approaches are described in the following sections.

Because any new process runs with the privileges of the process that launched it, if an attacker can trick your process into launching malicious code, the malicious code runs with the privileges of your process. Therefore, if your process is running with root privileges and is vulnerable to attack, the attacker can gain control of the system. There are many ways an attacker can trick your code into launching malicious code, including buffer overflows, race conditions, and social engineering attacks (see [Types of Security Vulnerabilities](Types%20of%20Security%20Vulnerabilities.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdkmrzfvjvomq)).

Because all command-line arguments, including the program name (`argv[0]`), are under the control of the user, you should not trust `argv[0]` to point to your program. If you use the command line to re-execute your own application or tool, for example, a malicious user might have substituted a different app for `argv[0]`. If you then pass that to a function that uses the first argument as the name of the program to run, you are now executing the attacker’s code with your privileges.

In addition, if you must run external tools, be sure to do so in a safe way. See [C-Language Command Execution and Shell Scripts](Avoiding%20Injection%20Attacks%20and%20XSS.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdimjvfvbuqmznknltm) for more information. However, where possible, software running as the root user should avoid running external tools.

When you create a new process, the child process inherits its own copy of the parent process’s file descriptors (see the manual page for `fork`). Therefore, if you have a handle on a file, network socket, shared memory, or other resource that’s pointed to by a file descriptor and you fork off a child process, you must be careful to either close the file descriptor or you must make sure that the child process cannot be tampered with. Otherwise, a malicious user can use the subprocess to tamper with the resources referenced by the file descriptors.

For example, if you open a password file and don’t close it before forking a process, the new subprocess has access to the password file.

To set a file descriptor so that it closes automatically when you execute a new process (such as by using the [execve](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/execve.2.html#//apple_ref/doc/man/2/execve) system call), use the [fcntl](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/fcntl.2.html#//apple_ref/doc/man/2/fcntl) system call to set the close-on-exec flag. You must set this flag individually for each file descriptor; there’s no way to set it for all.

Most libraries and utilities use environment variables. Sometimes environment variables can be attacked with buffer overflows or by inserting inappropriate values. If your program links in any libraries or calls any utilities, your program is vulnerable to attacks through any such problematic environment variables. If your program is running as root, the attacker might be able to bring down or gain control of the whole system in this way. Examples of environment variables in utilities and libraries that have been attacked in the past include:

1. The dynamic loader: `LD_LIBRARY_PATH`, `DYLD_LIBRARY_PATH` are often misused, causing unwanted side effects.
2. libc: `MallocLogFile`
3. Core Foundation: `CF_CHARSET_PATH`
4. perl: `PERLLIB`, `PERL5LIB`, `PERL5OPT`

   [2CVE-2005-2748 (corrected in Apple Security Update 2005-008) 3CVE-2005-0716 (corrected in Apple Security Update 2005-003) 4CVE-2005-4158]

Environment variables are also inherited by child processes. If you fork off a child process, your parent process should validate the values of all environment variables before it uses them in case they were altered by the child process (whether inadvertently or through an attack by a malicious user).

You can use the [setrlimit](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/setrlimit.2.html#//apple_ref/doc/man/2/setrlimit) system call to limit the consumption of system resources by a process. For example, you can set the largest size of file the process can create, the maximum amount of CPU time the process can consume, and the maximum amount of physical memory a process may use. These process limits are inherited by child processes.

If an attacker uses `setrlimit` to alter these limits, it can cause operations to fail when they ordinarily would not have failed. For example, a vulnerability was reported for a version of Linux that made it possible for an attacker, by decreasing the maximum file size, to limit the size of the `/etc/passwd` and `/etc/shadow` files. Then, the next time a utility accessed one of these files, it truncated the file, resulting in a loss of data and denial of service. [CVE-2002-0762]

Similarly, if a piece of software does not do proper error checking, a failure in one operation could change the behavior of a later operation. For example, if lowering the file descriptor limit prevents a file from being opened for writing, a later piece of code that reads the file and acts on it could end up working with a stale copy of the data.

If you’re running with elevated privileges in order to write or read files in a world-writable directory or a user’s directory, you must be aware of time-of-check–time-of-use problems; see [Time of Check Versus Time of Use](Race%20Conditions%20and%20Secure%20File%20Operations.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdkobvfvjvomq).

In many cases, you can accomplish your task without needing elevated privileges. For example, suppose you need to configure the environment (add a configuration file to the user’s home directory or modify a configuration file in the user’s home directory) for your application. You can do this from an installer running as root (the `installer` command requires administrative privileges; see the `installer` manual page). However, if you have the application configure itself, or check whether configuration is needed when it starts up, then you don’t need to run as root at all.

An example of using an alternate design in order to avoid running with elevated privileges is given by the BSD `ps` command, which displays information about processes that have controlling terminals. Originally, BSD used the `setgid` bit to run the `ps` command with a group ID of `kmem`, which gave it privileges to read kernel memory. More recent implementations of the `ps` command use the `sysctl` utility to read the information it needs, removing the requirement that `ps` run with any special privileges.

If you do need to run code with elevated privileges, there are several approaches you can take:

- You can run a daemon with elevated privileges that you call on when you need to perform a privileged task. The preferred method of launching a daemon is to use the `launchd` daemon (see [launchd](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdkobzfvjvona)). It is easier to use `launchd` to launch a daemon and easier to communicate with a daemon than it is to fork your own privileged process.
- You can use the `authopen` command to read, create, or update a file (see [authopen](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdkobzfvjvoni)).
- You can use a BSD system call to change privilege level (see [Calls to Change Privilege Level](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdkobzfvjvomy)). These commands have confusing semantics. You must be careful to use them correctly, and it’s very important to check the return values of these calls to make sure they succeeded.

  Note that in general, unless your process was initially running as root, it cannot elevate its privilege with these calls or take on the privileges of any other user. However, a process running as root can discard (temporarily or permanently) those privileges. Any process can change from acting on behalf of one group to another (within the set of groups to which it belongs).

However you decide to run your privileged code, you should make it do as little as possible, and ensure that the code drops any additional privilege as soon as it has accomplished its task (see [Writing a Privileged Helper](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdkobzfvjvomq)). Although architecturally this is often the best solution, it is very difficult to do correctly, especially the first time you try. Unless you have a lot of experience with forking off privileged processes, you might want to try one of the other solutions first.

There are several commands you can use to change the privilege level of a program. The semantics of these commands are tricky, and vary depending on the operating system on which they’re used.

Here are some notes on the most commonly used system calls for changing privilege level:

- The [setuid](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/setuid.2.html#//apple_ref/doc/man/2/setuid) function sets the real and effective user IDs and the saved user ID of the current process to a specified value. The `setuid` function is the most confusing of the UID-setting system calls. Not only does the permission required to use this call differ among different UNIX-based systems, but the action of the call differs among different operating systems and even between privileged and unprivileged processes. If you are trying to set the effective UID, you should use the `seteuid` function instead.
- The [setreuid](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/setreuid.2.html#//apple_ref/doc/man/2/setreuid) function modifies the real UID and effective UID, and in some cases, the saved UID. The permission required to use this call differs among different UNIX-based systems, and the rule by which the saved UID is modified is complicated. For this function as well, if your intent is to set the effective UID, you should use the `seteuid` function instead.
- The [seteuid](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/seteuid.2.html#//apple_ref/doc/man/2/seteuid) function sets the effective UID, leaving the real UID and saved UID unchanged. In macOS, the effective user ID may be set to the value of the real user ID or of the saved set-user-ID. (In some UNIX-based systems, this function allows you to set the EUID to any of the real UID, saved UID, or EUID.) Of the functions available on macOS that set the effective UID, the `seteuid` function is the least confusing and the least likely to be misused.
- The [setgid](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/setgid.2.html#//apple_ref/doc/man/2/setgid) function acts similarly to the `setuid` function, except that it sets group IDs rather than user IDs. It suffers from the same shortcomings as the `setuid` function; use the `setegid` function instead.
- The [setregid](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/setregid.2.html#//apple_ref/doc/man/2/setregid) function acts similarly to the `setreuid` function, with the same shortcomings; use the `setegid` function instead.
- The [setegid](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/setegid.2.html#//apple_ref/doc/man/2/setegid) function sets the effective GID. This function is the preferred call to use if you want to set the EGID.

For more information on permissions, see the [Understanding Permissions](https://developer.apple.com/library/archive/documentation/Security/Conceptual/AuthenticationAndAuthorizationGuide/Permissions/Permissions.html#//apple_ref/doc/uid/TP40011200-CH5) chapter in _[Authentication, Authorization, and Permissions Guide](../Authentication%2C%20Authorization%2C%20and%20Permissions%20Guide/About%20Authentication%2C%20Authorization%2C%20and%20Permissions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytembq)_. For information on `setuid` and related commands, see _Setuid Demystified_ by Chen, Wagner, and Dean (Proceedings of the 11th USENIX Security Symposium, 2002), available at [http://www.usenix.org/publications/library/proceedings/sec02/full_papers/chen/chen.pdf](http://www.usenix.org/publications/library/proceedings/sec02/full_papers/chen/chen.pdf) and the manual pages for [setuid](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/setuid.2.html#//apple_ref/doc/man/2/setuid), [setreuid](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/setreuid.2.html#//apple_ref/doc/man/2/setreuid), [setregid](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/setregid.2.html#//apple_ref/doc/man/2/setregid), and [setgroups](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/setgroups.2.html#//apple_ref/doc/man/2/setgroups). The `setuid(2)` manual page includes information about `seteuid`, `setgid`, and `setegid` as well.

There are a couple of functions you might be able to use to avoid forking off a privileged helper application. The `authopen` command lets you obtain temporary rights to create, read, or update a file. You can use the `launchd` daemon to start a process with specified privileges and a known environment.

When you run the `authopen` command, you provide the pathname of the file that you want to access. There are options for reading the file, writing to the file, and creating a new file. Before carrying out any of these operations, the `authopen` command requests authorization from the system security daemon, which authenticates the user (through a password dialog or other means) and determines whether the user has sufficient rights to carry out the operation. See the manual page for `authopen(1)` for the syntax of this command.

Starting with macOS 10.4, the `launchd` daemon is used to launch daemons and other programs automatically, without user intervention. (If you need to support systems running versions of the OS earlier than 10.4, you can use startup items.)

The `launchd` daemon can launch both systemwide daemons and per-user agents, and can restart those daemons and agents after they quit if they are still needed. You provide a configuration file that tells `launchd` the level of privilege with which to launch your routine.

You can also use `launchd` to launch a privileged helper. By factoring your application into privileged and unprivileged processes, you can limit the amount of code running as the root user (and thus the potential attack surface). Be sure that you do not request higher privilege than you actually need, and always drop privilege or quit execution as soon as possible.

There are several reasons to use `launchd` in preference to writing a daemon running as the root user or a factored application that forks off a privileged process:

- Because `launchd` launches daemons on demand, your daemon needs not worry about whether other services are available yet. When it makes a request for one of those services, the service gets started automatically in a manner that is transparent to your daemon.
- Because `launchd` itself runs as the root user, if your only reason for using a privileged process is to run a daemon on a low-numbered port, you can let `launchd` open that port on your daemon’s behalf and pass the open socket to your daemon, thus eliminating the need for your code to run as the root user.
- Because `launchd` can launch a routine with elevated privileges, you do not have to set the `setuid` or `setgid` bits for the helper tool. Any routine that has the `setuid` or `setgid` bit set is likely to be a target for attack by malicious users.
- A privileged routine started by `launchd` runs in a controlled environment that can’t be tampered with. If you launch a helper tool that has the `setuid` bit set, it inherits much of the launching application’s environment, including:

  - Open file descriptors (unless their close-on-exec flag is set).
  - Environment variables (unless you use [posix_spawn](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/posix_spawn.2.html#//apple_ref/doc/man/2/posix_spawn), [posix_spawnp](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/posix_spawnp.2.html#//apple_ref/doc/man/2/posix_spawnp), or an `exec` variant that takes an explicit environment argument, such as [execve](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/execve.2.html#//apple_ref/doc/man/2/execve)).
  - Resource limits.
  - The command-line arguments passed to it by the calling process.
  - Anonymous shared memory regions (unattached, but available to reattach, if desired).
  - Mach port rights.

  There are probably others. It is much safer to use `launchd`, which completely controls the launch environment.
- It’s much easier to understand and verify the security of a protocol between your controlling application and a privileged daemon than to handle the interprocess communication needed for a process you forked yourself. When you fork a process, it inherits its environment from your application, including file descriptors and environment variables, which might be used to attack the process (see [The Hostile Environment and the Principle of Least Privilege](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdkobzfvjvonq)). You can avoid these problems by using `launchd` to launch a daemon.
- It’s easier to write a daemon and launch it with `launchd` than to write factored code and fork off a separate process.
- Because `launchd` is a critical system component, it receives a lot of peer review by in-house developers at Apple. It is less likely to contain security vulnerabilities than most production code.
- The `launchd.plist` file includes key-value pairs that you can use to limit the system services—such as memory, number of files, and cpu time—that the daemon can use.

For more information on `launchd`, see the manual pages for `launchd`, `launchctl`, and `launchd.plist`, and _[Daemons and Services Programming Guide](../../Mac%20OSX/Daemons%20and%20Services%20Programming%20Guide/About%20Daemons%20and%20Services.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3te2i)_. For more information about startup items, see _[Daemons and Services Programming Guide](../../Mac%20OSX/Daemons%20and%20Services%20Programming%20Guide/About%20Daemons%20and%20Services.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3te2i)_.

In addition to `launchd`, the following lesser methods can be used to obtain elevated privileges. In each case, you must understand the limitations and risks posed by the method you choose.

- __setuid__

  If an executable's `setuid` bit is set, the program runs as whatever user owns the executable regardless of which process launches it. There are two approaches to using `setuid` to obtain root (or another user’s) privileges while minimizing risk:

  - Launch your program with root privileges, perform whatever privileged operations are necessary immediately, and then permanently drop privileges.
  - Launch a `setuid` helper tool that runs only as long as necessary and then quits.

  If the operation you are performing needs a group privilege or user privilege other than root, you should launch your program or helper tool with that privilege only, not with root privilege, to minimize the damage if the program is hijacked.

  It’s important to note that if you are running with both a group ID (GID) and user ID (UID) that are different from those of the user, you have to drop the GID before dropping the UID. Once you’ve changed the UID, you can no longer change the GID. As with every security-related operation, you must check the return values of your calls to [setuid](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/setuid.2.html#//apple_ref/doc/man/2/setuid), [setgid](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/setgid.2.html#//apple_ref/doc/man/2/setgid), and related routines to make sure they succeeded.

  For more information about the use of the `setuid` bit and related routines, see [Elevating Privileges Safely](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdkobzfvjvomi).
- __SystemStarter__

  When you put an executable in the `/Library/StartupItems` directory, it is started by the `SystemStarter` program at boot time. Because `SystemStarter` runs with root privileges, you can start your program with any level of privilege you wish. Be sure to use the lowest privilege level that you can use to accomplish your task, and to drop privilege as soon as possible.

  Startup items run daemons with root privilege in a single global session; these processes serve all users.

  For macOS 10.4 and later, the use of startup items is deprecated; use the `launchd` daemon instead. For more information on startup items and startup item privileges, see [Startup Items](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/StartupItems.html#//apple_ref/doc/uid/10000172i-SW9) in _[Daemons and Services Programming Guide](../../Mac%20OSX/Daemons%20and%20Services%20Programming%20Guide/About%20Daemons%20and%20Services.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3te2i)_.
- __AuthorizationExecWithPrivilege__

  The Authorization Services API provides the [AuthorizationExecuteWithPrivileges](https://developer.apple.com/documentation/security/1540038-authorizationexecutewithprivileg) function, which launches a privileged helper as the root user.

  Although this function can execute any process temporarily with root privileges, it is not recommended except for installers that have to be able to run from CDs and self-repairing `setuid` tools. See _[Authorization Services Programming Guide](../Authorization%20Services%20Programming%20Guide/Introduction%20to%20Authorization%20Services%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojv)_ for more information.
- __xinetd__

  In earlier versions of macOS, the `xinetd` daemon was launched with root privileges at system startup and subsequently launched internet services daemons when they were needed. The `xinetd.conf` configuration file specified the UID and GID of each daemon started and the port to be used by each service.

  Starting with macOS 10.4, you should use `launchd` to perform the services formerly provided by `xinetd`. See _[Daemons and Services Programming Guide](../../Mac%20OSX/Daemons%20and%20Services%20Programming%20Guide/About%20Daemons%20and%20Services.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3te2i)_ for information about converting from `xinetd` to `launchd`. See the manual pages for `xinetd(8)` and `xinetd.conf(5)` for more information about `xinetd`.
- __Other__

  If you are using some other method to obtain elevated privilege for your process, you should switch to one of the methods described here and follow the cautions described in this chapter and in [Elevating Privileges Safely](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdkobzfvjvomi).

If you’ve read this far and you’re still convinced that part of your application needs elevated privileges, this section provides some tips and sample code. In addition, see _[Authorization Services Programming Guide](../Authorization%20Services%20Programming%20Guide/Introduction%20to%20Authorization%20Services%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojv)_ for more advice on the use of Authorization Services and the proper way to factor an application.

As explained in the Authorization Services documentation, it is very important that you check the user’s rights to perform the privileged operation, both before and after launching your privileged helper tool. Your helper tool, owned by root and with the `setuid` bit set, has sufficient privileges to perform whatever task it has to do. However, if the user doesn’t have the rights to perform this task, you shouldn’t launch the tool and—if the tool gets launched anyway—the tool should quit without performing the task. Your nonprivileged process should first use Authorization Services to determine whether the user is authorized and to authenticate the user if necessary (this is called _preauthorizing_; see [Listing 5-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdkobzfvjvony)). Then launch your privileged process. The privileged process then should authorize the user again, before performing the task that requires elevated privileges; see [Listing 5-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdkobzfvjvooa). As soon as the task is complete, the privileged process should terminate.

In determining whether a user has sufficient privileges to perform a task, you should use rights that you have defined and put into the policy database yourself. If you use a right provided by the system or by some other developer, the user might be granted authorization for that right by some other process, thus gaining privileges to your application or access to data that you did not authorize or intend. For more information about policies and the policy database, (see the section “The Policy Database” in the [Authorization Concepts](https://developer.apple.com/library/archive/documentation/Security/Conceptual/authorization_concepts/02authconcepts/authconcepts.html#//apple_ref/doc/uid/TP30000995-CH205) chapter of _[Authorization Services Programming Guide](../Authorization%20Services%20Programming%20Guide/Introduction%20to%20Authorization%20Services%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojv)_).

In the code samples shown here, the task that requires privilege is killing a process that the user does not own.

If a user tries to kill a process owned by another user, the application has to make sure the user is authorized to do so. The following numbered items correspond to comments in the code sample:

1. If the process is owned by the user, and the process is not the window server or the login window, go ahead and kill it.
2. Call the [permitWithRight:flags:](https://developer.apple.com/documentation/securityfoundation/sfauthorization/1417641-permitwithright) method to determine whether the user has the right to kill the process. The application must have previously added this right—in this example, called `com.apple.processkiller.kill`—to the policy database. The `permitWithRight:flags:` method handles the interaction with the user (such as an authentication dialog). If this method returns `0`, it completed without an error and the user is considered preauthorized.
3. Obtain the authorization reference.
4. Create an external form of the authorization reference.
5. Create a data object containing the external authorization reference.
6. Pass this serialized authorization reference to the `setuid` tool that will kill the process ([Listing 5-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdkobzfvjvooa)).

__Listing 5-1__  Non-privileged process

```
if (ownerUID == _my_uid && ![[contextInfo processName]
    isEqualToString:@"WindowServer"] && ![[contextInfo processName]
    isEqualToString:@"loginwindow"]) {
        [self killPid:pid withSignal:signal];                                      // 1
} else {
    SFAuthorization *auth = [SFAuthorization authorization];
    if (![auth permitWithRight:"com.apple.proccesskiller.kill" flags:
          kAuthorizationFlagDefaults|kAuthorizationFlagInteractionAllowed|
          kAuthorizationFlagExtendRights|kAuthorizationFlagPreAuthorize])    // 2
    {
            AuthorizationRef authRef = [auth authorizationRef];                        // 3
            AuthorizationExternalForm authExtForm;
            OSStatus status = AuthorizationMakeExternalForm(authRef, &authExtForm);    // 4
            if (errAuthorizationSuccess == status) {
                NSData *authData = [NSData dataWithBytes: authExtForm.bytes
                                    length: kAuthorizationExternalFormLength];    // 5
                [_agent killProcess:pid signal:signal authData: authData];                 // 6
            }
    }
}
```

The external tool is owned by root and has its `setuid` bit set so that it runs with root privileges. It imports the externalized authorization rights and checks the user’s authorization rights again. If the user has the rights, the tool kills the process and quits. The following numbered items correspond to comments in the code sample:

1. Convert the external authorization reference to an authorization reference.
2. Create an authorization item array.
3. Create an authorization rights set.
4. Call the [AuthorizationCopyRights](https://developer.apple.com/documentation/security/1395770-authorizationcopyrights) function to determine whether the user has the right to kill the process. You pass this function the authorization reference. If the credentials issued by the Security Server when it authenticated the user have not yet expired, this function can determine whether the user is authorized to kill the process without reauthentication. If the credentials have expired, the Security Server handles the authentication (for example, by displaying a password dialog). (You specify the expiration period for the credentials when you add the authorization right to the policy database.)
5. If the user is authorized to do so, kill the process.
6. If the user is not authorized to kill the process, log the unsuccessful attempt.
7. Release the authorization reference.

__Listing 5-2__  Privileged process

```
AuthorizationRef authRef = NULL;
OSStatus status = AuthorizationCreateFromExternalForm(
  (AuthorizationExternalForm *)[authData bytes], &authRef);              // 1
if ((errAuthorizationSuccess == status) && (NULL != authRef)) {
AuthorizationItem right = {"com.apple.proccesskiller.kill",
                                                0L, NULL, 0L};           // 2
AuthorizationItemSet rights = {1, &right};                               // 3
status = AuthorizationCopyRights(authRef, &rights, NULL,
        kAuthorizationFlagDefaults | kAuthorizationFlagInteractionAllowed |
        kAuthorizationFlagExtendRights,    NULL);                        // 4
if (errAuthorizationSuccess == status)
kill(pid, signal);                                                       // 5
else
NSLog(@"Unauthorized attempt to signal process %d with %d",
            pid, signal);                                                // 6
AuthorizationFree(authRef, kAuthorizationFlagDefaults);                  // 7
}
```


If you write a privileged helper tool, you need to be very careful to examine your assumptions. For example, you should always check the results of function calls; it is dangerous to assume they succeeded and to proceed on that assumption. You must be careful to avoid any of the pitfalls discussed in this document, such as buffer overflows and race conditions.

If possible, avoid linking in any extra libraries. If you do have to link in a library, you must not only be sure that the library has no security vulnerabilities, but also that it doesn’t link in any other libraries. Any dependencies on other code potentially open your code to attack.

In order to make your helper tool as secure as possible, you should make it as short as possible—have it do only the very minimum necessary and then quit. Keeping it short makes it less likely that you made mistakes, and makes it easier for others to audit your code. Be sure to get a security review from someone who did not help write the tool originally. An independent reviewer is less likely to share your assumptions and more likely to spot vulnerabilities that you missed.

In addition to the basic permissions provided by BSD, the macOS Authorization Services API enables you to use the policy database to determine whether an entity should have access to specific features or data within your application. Authorization Services includes functions to read, add, edit, and delete policy database items.

You should define your own trust policies and put them in the policy database. If you use a policy provided by the system or by some other developer, the user might be granted authorization for a right by some other process, thus gaining privileges to your application or access to data that you did not authorize or intend. Define a different policy for each operation to avoid having to give broad permissions to users who need only narrow privileges. For more information about policies and the policy database, see the section “The Policy Database” in the [Authorization Concepts](https://developer.apple.com/library/archive/documentation/Security/Conceptual/authorization_concepts/02authconcepts/authconcepts.html#//apple_ref/doc/uid/TP30000995-CH205) chapter of _[Authorization Services Programming Guide](../Authorization%20Services%20Programming%20Guide/Introduction%20to%20Authorization%20Services%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojv)_.

Authorization Services does not enforce access controls; rather, it authenticates users and lets you know whether they have permission to carry out the action they wish to perform. It is up to your program to either deny the action or carry it out.

Because kernel extensions have no user interface, you cannot call Authorization Services to obtain permissions that you do not already have. However, in portions of your code that handle requests from user space, you can determine what permissions the calling process has, and you can evaluate access control lists (ACLs; see the section “ACLs” in the [OS X File System Security](../../File%20Management/File%20System%20Programming%20Guide/File%20System%20Details.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydmnzsfvbuqobnknlts) section in the [File System Details](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/FileSystemDetails/FileSystemDetails.html#//apple_ref/doc/uid/TP40010672-CH8) chapter of _[File System Programming Guide](../../File%20Management/File%20System%20Programming%20Guide/About%20Files%20and%20Directories.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydmnzs)_).

In macOS 10.4 and later, you can also use the Kernel Authorization (Kauth) subsystem to manage authorization. For more information on Kauth, see Technical Note TN2127, _Kernel Authorization_ ([http://developer.apple.com/technotes/tn2005/tn2127.html](https://developer.apple.com/technotes/tn2005/tn2127.html)).

[Next](Designing%20Secure%20User%20Interfaces.md)[Previous](Race%20Conditions%20and%20Secure%20File%20Operations.md)

