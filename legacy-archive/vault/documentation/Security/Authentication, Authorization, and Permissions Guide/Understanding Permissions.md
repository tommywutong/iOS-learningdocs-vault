---
title: Authentication, Authorization, and Permissions Guide
apple_id: TP40011200
resource_type: Guide
platform: macOS
topic: Security
technology: null
published: '2013-01-28'
source_url: https://developer.apple.com/library/archive/documentation/Security/Conceptual/AuthenticationAndAuthorizationGuide/Permissions/Permissions.html
archived_at: '2026-07-18T02:06:11.257733Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Authentication, Authorization, and Permissions Guide](About%20Authentication%2C%20Authorization%2C%20and%20Permissions.md)


[Next](Additional%20Resources.md)[Previous](Using%20Authorization.md)

# Understanding Permissions

An important aspect of security on a computer system is the granting or denying of permissions (sometimes called _access rights_). A permission is the ability to perform a specific operation such as to gain access to data or to execute code. Permissions can be granted at the level of directories, subdirectories, files or applications, or specific data within files or functions within applications.

Permissions in macOS are controlled at many levels, from the Mach and BSD components of the kernel, through higher levels of the operating system and, for networked applications, through the networking protocols.

This chapter describes the basic permissions policies at various levels in macOS.

At the deepest level of macOS system architecture, the basis for the operating system’s built-in security features is provided by the Mach and BSD components of the kernel. This section provides only a very brief and cursory introduction to Mach. For more information on Mach in macOS and Mach programming, see _[Kernel Programming Guide](../../Darwin/Kernel%20Programming%20Guide/About%20This%20Document.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbv)_.

Mach security is based on ports and port rights. A _Mach port_ is an endpoint of a communication channel between a client who requests a service and a server that provides the service. Mach ports are unidirectional; a reply to a service request must use a second port.

A port has a set of associated port rights, which are owned by tasks. A port right specifies that a particular task can use that port. Each port has one receive right, the owner of which can receive messages on that port. Each port has one or more send rights; the owners of send rights can send messages to the port. Rights can be transferred between tasks by attaching them to a Mach message.

A single task (or other Mach object, such as a thread or the host itself) may have multiple ports that provide access to resources it supports. For example, a task might have a name port and a control port. Access to the control port allows the task to be manipulated. In contrast, access to the name port merely allows the client to obtain information about the task or perform other nonprivileged operations on it.

Each process has a port right namespace, which maps small integers known as _port right names_ to their corresponding port rights. A port right name is meaningful only within that task’s port right namespace. A task can transfer a port right to another task by sending it the corresponding port right name. However, unless it sends the name correctly, the receiving task won’t be able use the right. The only way to transmit a port right between two tasks is by sending a Mach message and attaching the right name to that message using the correct syntax and message structure.

When you use Mach to create a task, Mach returns a port right name that references a send right for the port (the receive right for a task port is always owned by the kernel). You can send messages to this port to start and stop the task, kill the task, manipulate the task’s address space, and so forth. Therefore, whoever owns a send right for a task’s port effectively owns the task and can manipulate the task’s state without regard to BSD security policies or any higher-level security policies. In other words, an expert in Mach programming with local administrator access to an macOS machine can bypass BSD and higher-level security features. Therefore, it is very important to use strong administrator passwords, keep them secure, and control physical security for any computer containing sensitive information.

The BSD portion of the macOS kernel enforces access to applications and files. The most familiar aspect of BSD security is the file system security policy, which controls access to files and directories. BSD file permissions are described in [File System Security Policy](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytembqfvbuqnjnkrifqusfiyytcny).

In addition to the file system security policy, BSD defines two other security policies used in special cases: the owner or root security policy, and the root EUID security policy. Each of these policies is described briefly in the following subsections.

The BSD security model is based on matching up attributes of a file system object (a file or directory) with attributes of the process attempting to gain access to that object. For example, suppose a file has an owning user ID of 1234 and the file permissions specify that the owning user has read and write access to that file. Suppose further that Alice has an effective user ID (EUID) of 1234. When Alice attempts to read the file, BSD matches her EUID with the file’s owning UID and grants Alice access to read the file.

Each process has three user IDs: the real user ID (RUID), the effective user ID (EUID), and the saved user ID (SUID). The RUID is always inherited from the user or process that executes the process. The EUID is normally the same as the RUID, but it can differ in special circumstances as described in Owner-or-Root Security Policy below. In most cases, it is the EUID that BSD checks to determine permissions. The SUID is used by BSD to enable a privileged process to switch into and out of privileged mode.

Each process also has real and saved group IDs (RGID and SGID) and up to 16 effective group IDs (EGIDs), which work in a way analogous to the process’s user IDs.

For more details on these UIDs and GIDs, see _The Design and Implementation of the 4.4 BSD Operating System_, by Marshall Kirk McKusick and others.)

Starting in macOS 10.5, the kernel includes an implementation of the TrustedBSD Mandatory Access Control (MAC) framework. A formal requirements language suitable for third-party developer use was added in macOS 10.7. Mandatory access control, also known as sandboxing, is discussed in [Sandboxing and the Mandatory Access Control Framework](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytembqfvbuqnjnknlti).

macOS supports both the standard UNIX user-group-other permissions model (supplemented by BSD file flags) and POSIX access control lists (ACLs).

In the user-group-other permission model, the access rights to a file depend on the effective user ID (EUID) and effective group ID (EGID) of the calling process as follows:

1. If the application’s sandbox forbids the requested access, the request is denied.
2. If ownership checking has been disabled for the volume in question by the system administrator (with a checkbox in its Finder Get Info window), the request is granted.
3. If an access control entry exists on the file, it is evaluated and used to determine access rights.
4. If a BSD file flag prohibits the operation, the operation is denied.
5. Otherwise, if the user ID matches the owner of the file, the “user” permissions (also called “owner” permissions) are used.
6. Otherwise, if the group ID matches the group for the file, the “group” permissions are used.
7. Otherwise, the “other” permissions are used.

For more details, read [OS X File System Security](../../File%20Management/File%20System%20Programming%20Guide/File%20System%20Details.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydmnzsfvbuqobnknlts) in _[File System Programming Guide](../../File%20Management/File%20System%20Programming%20Guide/About%20Files%20and%20Directories.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydmnzs)_.

The owner-or-root security policy is used to control execution of a few specific operations. Under this policy, a specific operation on an object can be performed by any process whose EUID is the same as the object’s owner or whose EUID is zero (0). The user with a UID of zero is called the _root user_ (also called the _superuser_), and a process running with an EUID of zero is said to be running as`root`.

This policy is used in three primary places:

- Changing permissions on files with the `chmod` system call.

  Only the owner of the file or a process running as `root` can change a file’s permissions.
- Deleting or renaming files within a directory whose sticky bit is set.

  Only the owner of the file, the owner of the enclosing directory, and `root` can delete or rename the file.
- Sending signals to running processes (including killing the process).

  A process can only send a signal to another process if their EUIDs match or if the sending process has an EUID of 0.

Under the root EUID security policy, an operation can be performed only by a process with an EUID of 0. Such operations are sometimes referred to as _privileged operations_. Some of the common situations where the root EUID security policy applies are:

- Changing the owner of a file system object
- Binding TCP/IP sockets to low-numbered ports
- Making changes to the network configuration
- Certain I/O Kit operations
- Getting the Mach host privileged special port

Because a process running with an EUID of 0 has many special privileges, such a process can be a target of malicious hackers. To minimize such risks, you should factor your application into privileged and nonprivileged processes. See [Using Authorization](Using%20Authorization.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytembqfvbuqmznknltc) for more information and for references that describe and illustrate this technique.

Processes can change their EUID and EGID by calling `setuid`, `setgid`, and related system calls. For example, a process can run as root temporarily and then switch to a less privileged EUID to minimize exposure to malicious attacks. This technique is complicated by the confusing semantics of the `setuid` call and by the fact that these calls operate somewhat differently on different implementations of UNIX (including different versions of macOS). For a detailed discussion of the issues involved, see _Setuid Demystified_ by Chen, Wagner, and Dean in Proceedings of the 11th USENIX Security Symposium, 2002, available at the [USENIX website](http://www.usenix.org/publications/library/proceedings/sec02/full_papers/chen/chen.pdf). For more information on the system calls, see the man pages for `setuid`, `setreuid`, and `setregid`. The `setuid` man page includes information about `seteuid`, `setgid`, and `setegid` as well.

Sandboxing provides fine-grained control over the ability of processes to access system resources. For example, you can prevent a process from connecting to any network, from writing any files, or from writing any files outside of specific directories. This feature limits the amount of damage that can be done by a malicious hacker that gains control of an application.

Under the hood, sandboxing support is provided by the macOS Mandatory Access Control (MAC) framework, which is an implementation of the [TrustedBSD MAC framework](http://www.trustedbsd.org/mac.html).

[Next](Additional%20Resources.md)[Previous](Using%20Authorization.md)

