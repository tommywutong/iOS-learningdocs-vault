---
title: Porting UNIX/Linux Applications to OS X
apple_id: TP30001003
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2012-06-11'
source_url: https://developer.apple.com/library/archive/documentation/Porting/Conceptual/PortingUnix/io_porting/io_porting.html
archived_at: '2026-07-18T01:50:47.721022Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Porting UNIX/Linux Applications to OS X](Introduction%20to%20Porting%20UNIX-Linux%20Applications%20to%20OS%20X.md)


[Next](Distributing%20Your%20Application.md)[Previous](Using%20Traditional%20UNIX%20Graphical%20Environments.md)

# Porting File, Device, and Network I/O

OS X offers most of the standard UNIX mechanisms for file and device I/O. There are, however, differences to be aware of when porting your application to OS X from other UNIX-based and UNIX-like platforms.

This chapter describes file I/O and device I/O in OS X, including APIs that will enhance the user experience such as the file manager APIs for file access.

If you are a commercial software developer or if your application will be used by end users, you should read this chapter.

If you are writing a port of an open source application or an in-house UNIX application, you should read this chapter only if your application already uses or plans to use alternate file APIs for other platforms or if you need to do device I/O.

OS X contains all of the standard UNIX and POSIX file I/O functionality. For a basic port of an application to OS X, you generally do not need to make any changes in this area unless your application assumes that the file system stores files in a case-sensitive manner. (HFS+, the default Mac file system, is case-preserving, but not case-sensitive.)

However, traditional Mac applications have some enhanced behavior that you may want to incorporate in your application. The most powerful of these is the use of aliases to find files when their location has changed. It is not possible to use this capability through standard UNIX APIs. To obtain this functionality, you must use either Carbon or Cocoa APIs.

For example, some Mac applications also take advantage of the HFS+ file system’s ability to handle multi-forked files. This could be used, for example, to store disposable information about a file such as last window position. It is not recommended that crucial information be stored in resource forks when writing new applications. However, for compatibility reasons, you may need to access data stored in resource forks if your application needs to read files created by older Mac applications, or if you are writing a backup tool that needs to retain the entire contents of a file.

Also, Mac applications present the file system in a different way than POSIX applications in open and save dialogs. Mac applications have a directory structure multiply rooted from the individual volumes instead of singly rooted from the root volume. Using the Carbon or Cocoa APIs achieves this view of the file system automatically. These APIs also present standard file open and save dialogs that match the standard user experience that Mac users have come to expect.

Before moving to a Carbon or Cocoa file browser interface, you should consider what kinds of users are likely to use your application on the Mac platform. Are they mostly experienced in using another UNIX-based platform, or are they largely Mac users?

If they are mostly UNIX users, the Mac file dialog may be confusing to them. If they are mostly Mac users, a traditional UNIX file dialog may be equally confusing. You should generally choose which file API to use based on long-term expectations rather than the current user base to avoid problems down the line.

Carbon APIs are useful when writing file I/O entirely in C. They provide very basic access much like the traditional POSIX APIs.

__Table 7-1__  POSIX versus Carbon APIs

| POSIX function | Carbon Function | Description |
| `open`, `fopen` | `FSOpenFork` | Takes a filesystem reference (`FSRef`) as an argument and returns a fork reference number. |
| `close`, `fclose` | `FSClose` | Takes a fork reference number as an argument. |
| `create` | `FSCreateFileUnicode` | Takes the `FSRef` of the parent directory and the name of the file to be created. |
| `mkdir` | `FSCreateDirectoryUnicode` | Takes the `FSRef` of the parent directory and the name of the directory to be created. |
| `rmdir` | `FSDeleteObject` | Deletes a file or folder (by `FSRef`). |
| `unlink` | `FSDeleteObject` or `FSDeleteFork` | Deletes a file or folder (by `FSRef`) or delete a single fork of a file. |

Note that these functions use `FSSpec` and `FSRef` structures rather than file names. The functions `FSRefMakePath` and `FSPathMakeRef` convert an `FSRef` to a path and vice versa. Similarly, `FSpMakeFSRef` converts an `FSSpec` to an `FSRef`.

Cocoa file APIs are very different from traditional POSIX APIs. An explanation of the Cocoa APIs is beyond the scope of this book. For more information on Cocoa file APIs, see _[File System Programming Guide](../../File%20Management/File%20System%20Programming%20Guide/About%20Files%20and%20Directories.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydmnzs)_.

File open and save dialog boxes can be presented in OS X using Carbon or Cocoa file dialog APIs. If you choose to use the standard dialog boxes, use the same API you used for the rest of your GUI.

The Carbon file dialog API, Navigation Services, is described in _Navigation Services Reference_ in Carbon Documentation.

The Cocoa file dialog API consists of the functions `NSOpenPanel` and `NSSavePanel`, for open and save dialogs. These are described in _[Application File Management](../../Cocoa/Application%20File%20Management/Introduction%20to%20Application%20File%20Management.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2tm2i)_ in Cocoa Documentation.

OS X provides many of the traditional UNIX mechanisms for device I/O. However, individual device driver designs determine whether or not to use these mechanisms.

In OS X, disk devices, serial port devices, the random-number generator pseudo-device, and pseudo-tty devices (pttys) are traditionally accessed through standard UNIX-style block and character devices. Other pseudo-devices (devices without hardware backing) can also be implemented as BSD devices. You can use these device files in the same way as you would use them on any other UNIX-based or UNIX-like system.

Most actual hardware devices, however, such as USB and FireWire devices are not handled with block or character devices in OS X. Instead, the primary mechanism for accessing hardware devices is through I/O Kit user clients, which are basically remote procedure call or system call interfaces that allow you to call functions within a kernel driver from an application.

To access a hardware device, you must use APIs to search the device tree for a device matching various parameters. You then call functions within the driver. The mechanism used to call these functions depends on the design of the device interface, as do the functions themselves. You can also get information about the device using a standardized mechanism provided by the I/O Kit to examine its properties in the device tree.

A device cannot be controlled from an application unless there is a driver in the kernel. In many cases, the driver may be a simple pass-through that presents a device interface that allows the real device driver to be part of the application itself. In other cases, it may be a full driver for the device that presents a device interface for configuration. The device interface may be provided by OS X itself (such as the user space device interface for USB HID devices) or it may be provided by the individual hardware vendor (such as an audio card driver).

The implementation of a user client is beyond the scope of this document. It is described in detail in the book _[Accessing Hardware From Applications](../../Device%20Drivers/Accessing%20Hardware%20From%20Applications/Introduction%20to%20Accessing%20Hardware%20From%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgnzw)_. Since the design of a user client is also heavily dependent on the design of the device interface to which it is connecting, you may also need to read documentation specific to the technology area in question. In the case of device interfaces created by hardware vendors, you may also need to contact the hardware vendor for additional programming information.

The OS X file system organization is slightly different from that of most UNIX environments, and is described in detail in the man page `hier`. This section presents only the most important differences between a typical UNIX environment and OS X.

First, OS X has a number of folders intended primarily for use with GUI applications or for parts of OS X itself. These paths generally start with a capital letter, and include:

- `/Applications`—contains GUI applications
- `/System`—contains system frameworks and parts of the OS itself
- `/Library`—contains primarily user-installed frameworks
- `/Developer`—contains the developer tools (if installed)
- `/Users`—contains the home directories of local users

In addition, various ports collections are available, and install files in various locations, such as `/sw` (fink), `/usr/local` (GNU-Darwin), and `/opt/local/` (Darwin Ports).

A few directories, including `/etc` and `/tmp` are actually symbolic links into `/private`. You should be careful not to stomp on these symbolic links.

Finally, you should be aware that by default, a number of directories are hidden from users when viewing the file system using the OS X GUI. These directories include most of the standard system directories, including `/bin`, `/dev`, `/etc`, `/sbin`, `/tmp`, and `/usr`. These directories still appear and behave in the expected manner when accessed from the command line. For more information on making these visible from GUI applications, see [File-System Structure and Visibility](Additional%20Features.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnjwfvkfawcsivddcmbx).

OS X has different privilege sets for file system access. Users by default have write access to their home directory and certain other directories created in previous versions of Mac OS. Admin users have write access to additional parts of the system, including various application directories and configuration files, without the need to become the root user. Finally, the directories containing the OS itself are read-only except as root.

OS X provides the usual POSIX and BSD networking functionality. For more information on the actual APIs, see _OS X Man Pages_.

For the most part, this networking behaves just like it does on any other UNIX system. OS X differs in one crucial way, however. It does not use `/etc/hosts`, `/etc/resolv.conf`, and other similar configuration files for network configuration. (More precisely, the file `/etc/resolv.conf` is provided for read-only use, but should not be modified directly. The file `/etc/hosts` is provided, but is not used by default.)

If you need to configure name server settings (or other network settings), you should use the System Configuration framework (described in _[System Configuration Programming Guidelines](../../Networking/System%20Configuration%20Programming%20Guidelines/Introduction%20to%20System%20Configuration%20Programming%20Guidelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrv)_ and _[System Configuration Framework Reference](https://developer.apple.com/documentation/systemconfiguration)_).

If you need to add static host entries, you should use Directory Services (described in _Directory Service Framework Reference_, the `dscl` manual page, and [Open Directory and the dscl Tool](Additional%20Features.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnjwfvbeeq2dinbusri) elsewhere in this document).

[Next](Distributing%20Your%20Application.md)[Previous](Using%20Traditional%20UNIX%20Graphical%20Environments.md)

