---
title: File System Events Programming Guide
apple_id: TP40005289
resource_type: Guide
platform: macOS
topic: Data Management
technology: CoreServices
published: '2012-12-13'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/FSEvents_ProgGuide/TechnologyOverview/TechnologyOverview.html
archived_at: '2026-07-15T07:23:04.159170Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [File System Events Programming Guide](Introduction.md)


[Next](Using%20the%20File%20System%20Events%20API.md)[Previous](Introduction.md)

# Technology Overview

The File System Events API is a new technology available in OS X v10.5 and later. With it, you can register for notification of any changes that occur to a directory hierarchy or the contents thereof.

The file system events mechanism consists of three parts: kernel code that passes raw event notification to user space through a special device (also used by spotlight), a daemon which filters this stream and sends out notifications, and a persistent database which stores a record of all changes throughout time.

When your application registers for notification, the file system events daemon will post a notification every time that any file in the monitored directory hierarchy changes. It will also post a notification if the directory itself is modified (for example, if its permissions change or a new file is added). The important point to take away is that the granularity of notifications is at a directory level. It tells you _only_ that something in the directory has changed, but does not tell you _what_ changed.

In addition to collapsing notifications for changes to multiple files into a single, per-directory notification, the file system events daemon also coalesces multiple notifications on a given directory if they occur in a short period of time. You will always receive at least one notification after the last change is made. Beyond that, the temporal granularity can be as coarse or as fine as you desire; you choose the minimum time between events when you register for notification.

To better understand this technology, you should first understand what it is not. It is not a mechanism for registering for fine-grained notification of filesystem changes. It was not intended for virus checkers or other technologies that need to immediately learn about changes to a file and preempt those changes if needed. The best way to support these is through a kernel extension that registers for interest in changes at the VFS level.

The file system events API is also not designed for finding out when a particular file changes. For such purposes, the kqueues mechanism is more appropriate.

The file system events API is designed for passively monitoring a large tree of files for changes. The most obvious use for this technology is for backup software. Indeed, the file system events API provides the foundation for Apple’s backup technology.

Another good use for the file system events API is providing consistency guarantees for applications that store data as a loose collection containing a project and dozens or hundreds of related files potentially scattered across the disk. When one of the related files is modified by another application, your application needs to know about it so that it can choose how to incorporate the change into the project.

Of course, this use can also potentially be satisfied through the use of kqueues, but file system events provide the convenience of being able to see changes that occurred even while your application was not running, which can make consistency checking easier when your application opens a project initially.

[Next](Using%20the%20File%20System%20Events%20API.md)[Previous](Introduction.md)

