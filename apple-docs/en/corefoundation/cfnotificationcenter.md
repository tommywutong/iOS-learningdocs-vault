---
title: CFNotificationCenter
framework: Core Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfnotificationcenter
source_url: 'https://developer.apple.com/documentation/corefoundation/cfnotificationcenter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfnotificationcenter.json'
content_hash: 'sha256:5a51958a1a21ee87'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFNotificationCenter

<sub>Class</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CFNotificationCenter
```

## Overview

A CFNotificationCenter object provides the means by which you can send a message, or notification, to any number of recipients, or observers, without having to know anything about the recipients. A notification message consists of a notification name (a CFString), a pointer value that identifies the object posting the notification, and an optional dictionary that contains additional information about the particular notification.

To register as an observer of a notification, you call [CFNotificationCenterAddObserver](<cfnotificationcenteraddobserver(____________).md>), providing an identifier for your observer, the callback function that should be called when the notification is posted, and the name of the notification and the object in which you are interested. The observer identifier is passed back to the callback function, along with the notification information. You can use the identifier to distinguish multiple observers using the same callback function. The identifier is also used to unregister the observer with [CFNotificationCenterRemoveObserver](<cfnotificationcenterremoveobserver(________).md>) and [CFNotificationCenterRemoveEveryObserver](<cfnotificationcenterremoveeveryobserver(____).md>).

To send a notification, you call [CFNotificationCenterPostNotification](<cfnotificationcenterpostnotification(__________).md>), passing in the notification information. The notification center then looks up all the observers that registered for this notification and sends the notification information to their callback functions.

There are three types of CFNotificationCenter—a distributed notification center, a local notification center, and a Darwin notification center—an application may have at most one of each type. The distributed notification is obtained with [CFNotificationCenterGetDistributedCenter](<cfnotificationcentergetdistributedcenter().md>). A distributed notification center delivers notifications between applications. In this case, the notification object must always be a CFString object and the notification dictionary must contain only property list values. The local and Darwin notification centers are available in macOS 10.4 and later, and obtained using [CFNotificationCenterGetLocalCenter](<cfnotificationcentergetlocalcenter().md>) and [CFNotificationCenterGetDarwinNotifyCenter](<cfnotificationcentergetdarwinnotifycenter().md>) respectively.

Unlike some other Core Foundation opaque types with names similar to a Cocoa Foundation class (such as CFString and `NSString`), CFNotificationCenter objects cannot be cast (“toll-free bridged”) to [NotificationCenter](../foundation/notificationcenter.md) objects or vice-versa.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Accessing a Notification Center

- [CFNotificationCenterGetDarwinNotifyCenter](<cfnotificationcentergetdarwinnotifycenter().md>) — Returns the application’s Darwin notification center.
- [CFNotificationCenterGetDistributedCenter](<cfnotificationcentergetdistributedcenter().md>) — Returns the application’s distributed notification center.
- [CFNotificationCenterGetLocalCenter](<cfnotificationcentergetlocalcenter().md>) — Returns the application’s local notification center.

### Posting a Notification

- [CFNotificationCenterPostNotification](<cfnotificationcenterpostnotification(__________).md>) — Posts a notification for an object.
- [CFNotificationCenterPostNotificationWithOptions](<cfnotificationcenterpostnotificationwithoptions(__________).md>) — Posts a notification for an object using specified options.

### Adding and Removing Observers

- [CFNotificationCenterAddObserver](<cfnotificationcenteraddobserver(____________).md>) — Registers an observer to receive notifications.
- [CFNotificationCenterRemoveEveryObserver](<cfnotificationcenterremoveeveryobserver(____).md>) — Stops an observer from receiving any notifications from any object.
- [CFNotificationCenterRemoveObserver](<cfnotificationcenterremoveobserver(________).md>) — Stops an observer from receiving certain notifications.

### Getting the CFNotificationCenter Type ID

- [CFNotificationCenterGetTypeID](<cfnotificationcentergettypeid().md>) — Returns the type identifier for the CFNotificationCenter opaque type.

### Callbacks

- [CFNotificationCallback](cfnotificationcallback.md) — Callback function invoked for each observer of a notification when the notification is posted.

### Constants

- [CFNotificationSuspensionBehavior](cfnotificationsuspensionbehavior.md) — Suspension flags that indicate how distributed notifications should be handled when the receiving application is in the background.
- [Notification Posting Options](1569610-notification-posting-options.md) — Possible options when posting notifications.

## See Also

### Related Documentation

- [Notification Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Notifications/Introduction/introNotifications.html#//apple_ref/doc/uid/10000043i)

### Opaque Types

- [CFAllocator](cfallocator.md)
- [CFArray](cfarray.md)
- [CFAttributedString](cfattributedstring.md)
- [CFBag](cfbag.md)
- [CFBinaryHeap](cfbinaryheap.md)
- [CFBitVector](cfbitvector.md)
- [CFBoolean](cfboolean.md)
- [CFBundle](cfbundle.md)
- [CFCalendar](cfcalendar.md)
- [CFCharacterSet](cfcharacterset.md)
- [CFData](cfdata.md)
- [CFDate](cfdate.md)
- [CFDateFormatter](cfdateformatter.md)
- [CFDictionary](cfdictionary.md)
- [CFError](cferror.md)
