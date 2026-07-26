---
title: DistributedNotificationCenter
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/distributednotificationcenter
source_url: 'https://developer.apple.com/documentation/foundation/distributednotificationcenter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/distributednotificationcenter.json'
content_hash: 'sha256:71aab0d6c986a9c0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# DistributedNotificationCenter

<sub>Class</sub>

A notification dispatch mechanism that enables the broadcast of notifications across task boundaries.

<sub>Mac Catalyst, macOS</sub>

```swift
class DistributedNotificationCenter
```

## Overview

A [DistributedNotificationCenter](distributednotificationcenter.md) instance broadcasts [NSNotification](nsnotification.md) objects to objects in other tasks that have registered for the notification with their task’s default distributed notification center.

### Principal Attributes

- Notification dispatch table. See “Class at a Glance” \> “Principal Attributes” in [NotificationCenter](notificationcenter.md) for information about the dispatch table.

In addition to the notification name and sender, dispatch table entries for distributed notification centers specify when the notification center delivers notifications to its observers. See the [- postNotificationName:object:userInfo:deliverImmediately:](<distributednotificationcenter/postnotificationname(__object_userinfo_deliverimmediately_).md>) method, Suspending and Resuming Notification Delivery, and [SuspensionBehavior](distributednotificationcenter/suspensionbehavior.md) for details.

### Commonly Used Methods

- **[+ defaultCenter](<distributednotificationcenter/default().md>)** — Accesses the default distributed notification center.
- **[- addObserver:selector:name:object:suspensionBehavior:](<distributednotificationcenter/addobserver(__selector_name_object_suspensionbehavior_).md>)** — Registers an object to receive a notification with a specified behavior when notification delivery is suspended.
- **[- postNotificationName:object:userInfo:deliverImmediately:](<distributednotificationcenter/postnotificationname(__object_userinfo_deliverimmediately_).md>)** — Creates and posts a notification.
- **[- removeObserver:name:object:](<distributednotificationcenter/removeobserver(__name_object_).md>)** — Specifies that an object no longer wants to receive certain notifications.

### Overview

Each task has a default distributed notification center that you access with the [+ defaultCenter](<distributednotificationcenter/default().md>) class method. There may be different types of distributed notification centers. Currently there is a single type—`NSLocalNotificationCenterType`. This type of distributed notification center handles notifications that can be sent between tasks on a single computer. For communication between tasks on different computers, use [Distributed Objects Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DistrObjects/DistrObjects.html#//apple_ref/doc/uid/10000102i).

Posting a _distributed notification_ is an expensive operation. The notification gets sent to a system-wide server that distributes it to all the tasks that have objects registered for distributed notifications. The latency between posting the notification and the notification’s arrival in another task is unbounded. In fact, when too many notifications are posted and the server’s queue fills up, notifications may be dropped.

Distributed notifications are delivered via a task’s run loop. A task must be running a run loop in one of the “common” modes, such as `NSDefaultRunLoopMode`, to receive a distributed notification. For multithreaded applications running in macOS 10.3 and later, distributed notifications are always delivered to the main thread. For multithreaded applications running in OS X v10.2.8 and earlier, notifications are delivered to the thread that first used the distributed notifications API, which in most cases is the main thread.

> [!important] Important
> `NSDistributedNotificationCenter` does not implement a secure communications protocol. When using distributed notifications, your app should treat any data passed in the notification as untrusted. See [Security Overview](https://developer.apple.com/library/archive/documentation/Security/Conceptual/Security_Overview/Introduction/Introduction.html#//apple_ref/doc/uid/TP30000976) for general guidance on secure coding practices.

> [!note] Note
> `NSDistributedNotificationCenter` objects should not be used to send notifications between threads within the same task. Use [Distributed Objects Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DistrObjects/DistrObjects.html#//apple_ref/doc/uid/10000102i) or the [NSObject](../objectivec/nsobject-swift.class.md) method [performSelector(onMainThread:with:waitUntilDone:)](<../objectivec/nsobject-swift.class/performselector(onmainthread_with_waituntildone_).md>), instead. You can also setup an [Port](port.md) object to receive and distribute messages from other threads.

## Relationships

- **Inherits From**: [NotificationCenter](notificationcenter.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting Distributed Notification Centers

- [+ defaultCenter](<distributednotificationcenter/default().md>) — Returns the default distributed notification center, representing the local notification center for the computer.
- [+ notificationCenterForType:](<distributednotificationcenter/fortype(__).md>) — Returns the distributed notification center for a particular notification center type.

### Managing Observers

- [- addObserver:selector:name:object:](<distributednotificationcenter/addobserver(__selector_name_object_).md>) — Adds an entry to the notification center’s dispatch table with an observer, a selector, and an optional notification name and sender.
- [- addObserver:selector:name:object:suspensionBehavior:](<distributednotificationcenter/addobserver(__selector_name_object_suspensionbehavior_).md>) — Adds an entry to the receiver’s dispatch table with a specific observer and suspended-notifications behavior, and optional notification name and sender.
- [- removeObserver:name:object:](<distributednotificationcenter/removeobserver(__name_object_).md>) — Removes matching entries from the receiver’s dispatch table.

### Posting Notifications

- [- postNotificationName:object:](<distributednotificationcenter/post(name_object_).md>) — Creates a notification, and posts it to the receiver.
- [- postNotificationName:object:userInfo:](<distributednotificationcenter/post(name_object_userinfo_).md>) — Creates a notification with information, and posts it to the receiver.
- [- postNotificationName:object:userInfo:deliverImmediately:](<distributednotificationcenter/postnotificationname(__object_userinfo_deliverimmediately_).md>) — Creates a notification with information and an immediate-delivery specifier, and posts it to the receiver.
- [- postNotificationName:object:userInfo:options:](<distributednotificationcenter/postnotificationname(__object_userinfo_options_).md>) — Creates a notification with information, and posts it to the receiver.

### Suspending and Resuming Notification Delivery

- [suspended](distributednotificationcenter/suspended.md) — Suspends or resumes notification delivery.

### Constants

- [Options](distributednotificationcenter/options.md) — These constants specify the behavior of notifications posted using the [- postNotificationName:object:userInfo:options:](<distributednotificationcenter/postnotificationname(__object_userinfo_options_).md>) method.
- [CenterType](distributednotificationcenter/centertype.md) — This constant specifies the notification center type.
- [SuspensionBehavior](distributednotificationcenter/suspensionbehavior.md) — These constants specify the types of notification delivery suspension behaviors.

### Initializers

- [init(forType:)](<distributednotificationcenter/init(fortype_).md>)
