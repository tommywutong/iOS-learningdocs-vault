---
title: Mac Notification Overview
apple_id: TP40005947
resource_type: Guide
platform: macOS
topic: Interapplication Communication
technology: null
published: '2009-05-01'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/MacOSXNotifcationOv/ChoosingaNotificationMechanism/ChoosingaNotificationMechanism.html
archived_at: '2026-07-15T07:23:14.242855Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Mac Notification Overview](Introduction%20to%20OS%20X%20Notification%20Overview.md)


[Next](Darwin%20Notification%20Concepts.md)[Previous](Notification%20Basics.md)

# Choosing a Notification Technology

For the most part, the notification technology you choose should be appropriate for the type of programming you are doing. Command-line tools and daemons should generally use Darwin notifications. High-level applications should generally use either Core Foundation or Cocoa notifications.

This is not always true, however. In some cases, it may be more appropriate to choose a low-level notification scheme even in a high-level application. This chapter describes some environments in which you should choose a different technology than the most obvious choice.

When applications and daemons must communicate with notifications, the best choice is not always obvious.

- If the daemon is written with Cocoa or Core Foundation, you can use the Cocoa, Core Foundation, or Darwin notification mechanism, at your option.
- If the daemon is not based on Core Foundation (for example, most cross-platform open source software), it is usually much easier to use Darwin notifications in the daemon because you can do so without creating a run loop.
- Darwin notifications are also easier to tie into existing UNIX/Linux daemons because these daemons often already use signal handlers for event handling, and Darwin offers signal delivery as one of its supported delivery methods.
- For daemons that use file descriptors ([select(2)](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/select.2.html#//apple_ref/doc/man/2/select) loops), Darwin notifications can be integrated more easily because it offers file descriptors as a supported delivery method. Using Darwin notifications directly is significantly easier than rewriting the main program loop as a CFRunLoop (and, for open source projects, is much more likely to be accepted into their official source tree).

Of course, you do not have to use the same API in your application as in the daemon. As long as you limit your use of the Core Foundation or Cocoa notification APIs to empty messages (that is, messages with only a name), you can use those APIs in your application and still use the Darwin notification API in your daemon.

Cocoa notifications ([NSNotificationCenter](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNotificationCenter/Description.html#//apple_ref/occ/cl/NSNotificationCenter)) and Core Foundation notifications ([CFNotificationCenterRef](https://developer.apple.com/documentation/corefoundation/cfnotificationcenterref)) can communicate with each other, making it easy to provide notifications between Carbon and Cocoa applications. However, because these types are not toll-free bridged, you cannot cast between them.

For the most part, this is not a problem. However, if you need to post notifications from portions of your application written in Carbon, it may be easier to use Core Foundation notifications throughout. This will make it easier to share data structures between C and Objective-C portions of your code without introducing redundancy.

Similarly, if you are adding notifications to Carbon and Cocoa applications simultaneously and need to write any glue code that is common to both your Carbon and Cocoa applications, you may find it more convenient to write a single notification module based on Core Foundation notifications in order to avoid maintaining multiple versions of your glue code.

Many parts of OS X provide notifications in other ways. Examples include the I/O Kit, Disk Arbitration, System Configuration (`configd`), and kernel queues. To lean how to receive these notifications, you should read Apple’s documentation about those technologies.

Kernel queues and kernel event notifications are a much better alternative to polling for file changes. Kernel event notifications also provide a way to find out about a number of other kernel-related events. The kernel queues mechanism is described in _[File System Events Programming Guide](../File%20System%20Events%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2teobz)_ and in the manual pages for [kevent(2)](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/kevent.2.html#//apple_ref/doc/man/2/kevent) and [kqueue(2)](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/kqueue.2.html#//apple_ref/doc/man/2/kqueue).

The I/O Kit notification mechanism is based around the [IOService](https://developer.apple.com/documentation/kernel/ioservice) class. Registering for and posting notifications is described in _[IOKit Fundamentals](../../Device%20Drivers/IOKit%20Fundamentals/Introduction%20to%20I-O%20Kit%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridambqgaydcmi)_.

System Configuration notifications are provided through the System Configuration framework. You can learn more about this framework by reading _[System Configuration Programming Guidelines](../../Networking/System%20Configuration%20Programming%20Guidelines/Introduction%20to%20System%20Configuration%20Programming%20Guidelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrv)_ and _[System Configuration Framework Reference](https://developer.apple.com/documentation/systemconfiguration)_.

Disk Arbitration notifications can tell you when a volume is mounted or unmounted. (You can also learn when volumes are mounted or unmounted using the File System Events API in OS X v10.5 and later.) You can learn more about Disk Arbitration notifications in _[Disk Arbitration Framework Reference](https://developer.apple.com/documentation/diskarbitration)_.

[Next](Darwin%20Notification%20Concepts.md)[Previous](Notification%20Basics.md)

