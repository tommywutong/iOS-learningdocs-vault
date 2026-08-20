---
title: File-System Performance Guidelines
apple_id: 10000161i
resource_type: Guide
platform: iOS|macOS
topic: Data Management
technology: null
published: '2014-03-10'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/FileSystem/Articles/TrackingChanges.html
archived_at: '2026-07-18T01:48:45.228676Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [File-System Performance Guidelines](Introduction%20to%20File-System%20Performance%20Guidelines.md)


[Next](Document%20Revision%20History.md)[Previous](Resolving%20Domain%20Names.md)

# Tracking File-System Changes

Many applications need to watch the file system for changes:

- Applications with Finder-style file list views need to update the file lists based on changes made by the user in the Finder or in another application.
- Document-based applications should watch for filename modifications and change the document’s window title accordingly. They might also want to close a document window when the associated file is moved to the Trash.
- 

  A small number of applications need to watch a particular directory and process files dropped onto that directory.

The problem with any of these tasks is that the most common solution to the problem is to poll the operating system. Unfortunately, as is explained in _[Performance Overview](../Performance%20Overview/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytimjq)_, applications should never poll the system for information. In particular, polling the file system uses an excessive amount of I/O bandwidth and degrades system performance. It also tends to fill low-level file-system caches with less-useful information.

Instead of polling the system, your application should wait for system events and then synchronize information as appropriate. For example, when the application or document window becomes active, you can update the window title appropriately. For Cocoa applications, the NSDocument class implements this behavior for you. For Carbon applications, you can implement this behavior in a Carbon Event Manager `kWindowActivateEvent` event handler

For more global changes, the Carbon File Manager provides the `FNNotify` and `FNSubscribe` functions that allow applications to receive notifications whenever another application explicitly publishes changes to a directory. However, this service is strictly voluntary for both applications and does not provide notifications over the network. You can use it to supplement the file synchronization strategy mentioned above, but you cannot rely on it alone. For information on how to use the `FNNotify` and `FNSubscribe` family of functions see the _File Manager Reference_.

For Cocoa developers, the NSWorkspace class provides behavior similar to that provided by FNNotify and FNSubscribe. Your application can register to receive workspace notifications and use them to update files when changes occur. For information on how to send and receive notifications in cocoa, see [Receiving Workspace Notifications](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Workspace/Articles/WorkspaceNotifications.html#//apple_ref/doc/uid/20001009) in _[Workspace Services Programming Topics](../../Cocoa/Workspace%20Services%20Programming%20Topics/Introduction%20to%20Workspace%20Services.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeyda2i)_. See also the [NSWorkspace](https://developer.apple.com/documentation/appkit/nsworkspace) class documentation.

The kqueue mechanism in BSD provides another way to be notified of system changes. Using this mechanism you can request notifications when specific events occur or when a specific condition becomes true. You can use this to monitor files and other system entities such as ports and processes.

When you only want to track changes on a file or directory, be sure to open it using the `O_EVTONLY` flag. This flag prevents the file or directory from being marked as open or in use. This is important if you are tracking files on a removable volume and the user tries to unmount the volume. With this flag in place, the system knows it can dismiss the volume. If you had opened the files or directories without this flag, the volume would be marked as busy and would not be unmounted.

For more information about kqueues and kevents, see the `kqueue` man page.

[Next](Document%20Revision%20History.md)[Previous](Resolving%20Domain%20Names.md)

