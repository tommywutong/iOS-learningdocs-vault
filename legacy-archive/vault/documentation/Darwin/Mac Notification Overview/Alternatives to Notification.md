---
title: Mac Notification Overview
apple_id: TP40005947
resource_type: Guide
platform: macOS
topic: Interapplication Communication
technology: null
published: '2009-05-01'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/MacOSXNotifcationOv/AlternativestoNotification/AlternativestoNotification.html
archived_at: '2026-07-15T07:23:14.236110Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Mac Notification Overview](Introduction%20to%20OS%20X%20Notification%20Overview.md)


[Next](Document%20Revision%20History.md)[Previous](Darwin%20Notification%20Concepts.md)

# Alternatives to Notification

Notifications are just one possible solution. They are usually a good solution, but in some cases, you may want to use a different means of interprocess data sharing. This chapter describes some alternative mechanisms.

Distributed objects, Apple events, and other similar technologies are good solutions when you need to receive a response to indicate that the client has received a state change notification. This section briefly describes these technologies and provides pointers to further documentation.

Apple events is a Carbon message passing API. The Apple Events API enables you to send an event notification to another application and receive a response message. You can learn more in _[Apple Events Programming Guide](../../Apple%20Script/Apple%20Events%20Programming%20Guide/Introduction%20to%20Apple%20Events%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbz)_.

Distributed objects is a Cocoa remote procedure call API. Distributed objects enable one application to call Objective-C methods in another application and receive the return value. You can learn more in _[Distributed Objects Programming Topics](../../Cocoa/Distributed%20Objects%20Programming%20Topics/Introduction%20to%20Distributed%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeyde2i)_.

Other message-passing techniques in OS X include Mach messaging, sockets, pipes, and standard input and output. These techniques are explained in [Cross-Architecture Plug-in Support](https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/64bitPorting/Cross-ArchitecturePluginSupport/Cross-ArchitecturePluginSupport.html#//apple_ref/doc/uid/TP40001064-CH225) in _[64-Bit Transition Guide](../64-Bit%20Transition%20Guide/Introduction%20to%2064-Bit%20Transition%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanru)_.

Memory mapping and other shared memory techniques provide a good way to move large quantities of data between two applications. When two applications need to move data on a continuous basis, polling can be more efficient than notifications. For example, two audio applications connected by a buffer would be a poor match for notifications because the receiving application must read data on a regular basis even in the absence of a notification.

OS X provides several ways to share memory, depending on your needs.

For audio, you should use the Audio Queue API (part of the Core Audio framework). This API is described in _[Audio Queue Services Programming Guide](../../Music%20Audio/Audio%20Queue%20Services%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbt)_ and _[Audio Queue Services Reference](https://developer.apple.com/documentation/audiotoolbox/audio_queue_services)_.

For general memory sharing, the easiest mechanism to use is the [mmap(2)](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/mmap.2.html#//apple_ref/doc/man/2/mmap) system call. This system call allows you to map a file or portion thereof into the memory space of your process, effectively giving you a read-only or read-write pointer into the contents of the file itself. By mapping a file simultaneously into multiple processes, you can easily create shared memory between these processes. (Note that before calling this system call, you must first create the file, then extend it to an appropriate size.)

Two other ways to share memory are the POSIX and System V shared memory APIs. Because the POSIX shared memory API is newer and more flexible, you should favor the POSIX shared memory API for new applications unless you need to support other computing platforms where it are not available.

You can learn more about POSIX shared memory in the [shm_open(2)](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/shm_open.2.html#//apple_ref/doc/man/2/shm_open) and [shm_unlink(2)](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/shm_unlink.2.html#//apple_ref/doc/man/2/shm_unlink) manual pages.

You can learn more about System V shared memory in the [shmat(2)](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/shmat.2.html#//apple_ref/doc/man/2/shmat), [shmctl(2)](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/shmctl.2.html#//apple_ref/doc/man/2/shmctl), [shmget(2)](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/shmget.2.html#//apple_ref/doc/man/2/shmget), and [shmdt(2)](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/shmdt.2.html#//apple_ref/doc/man/2/shmdt) manual pages.

You can learn how to memory map files in the [mmap(2)](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/mmap.2.html#//apple_ref/doc/man/2/mmap) manual page. To find a simple example of this technique, see [Cross-Architecture Plug-in Support](https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/64bitPorting/Cross-ArchitecturePluginSupport/Cross-ArchitecturePluginSupport.html#//apple_ref/doc/uid/TP40001064-CH225) in _[64-Bit Transition Guide](../64-Bit%20Transition%20Guide/Introduction%20to%2064-Bit%20Transition%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanru)_.

[Next](Document%20Revision%20History.md)[Previous](Darwin%20Notification%20Concepts.md)

