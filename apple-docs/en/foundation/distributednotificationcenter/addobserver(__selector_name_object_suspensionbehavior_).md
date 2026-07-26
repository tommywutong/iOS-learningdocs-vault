---
title: 'addObserver(_:selector:name:object:suspensionBehavior:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/distributednotificationcenter/addobserver(_:selector:name:object:suspensionbehavior:)'
source_url: 'https://developer.apple.com/documentation/foundation/distributednotificationcenter/addobserver(_:selector:name:object:suspensionbehavior:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/distributednotificationcenter/addobserver%28_%3Aselector%3Aname%3Aobject%3Asuspensionbehavior%3A%29.json'
content_hash: 'sha256:bf9ebc4407540ca6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DistributedNotificationCenter](../distributednotificationcenter.md)

# addObserver(_:selector:name:object:suspensionBehavior:)

<sub>Instance Method</sub>

Adds an entry to the receiver’s dispatch table with a specific observer and suspended-notifications behavior, and optional notification name and sender.

<sub>Mac Catalyst, macOS</sub>

```swift
func addObserver(_ observer: Any, selector: Selector, name: NSNotification.Name?, object: String?, suspensionBehavior: DistributedNotificationCenter.SuspensionBehavior)
```

## Parameters

- `observer` — Object registering as an observer. Must not be `nil`.

- `selector` — Selector that specifies the message the receiver sends `notificationObserver` to notify it of the notification posting. Must not be `0`.

- `name` — The name of the notification for which to register the observer; that is, only notifications with this name are delivered to the observer. When `nil`, the notification center doesn’t use a notification’s name to decide whether to deliver it to the observer.

- `object` — The object whose notifications the observer wants to receive; that is, only notifications sent by this sender are delivered to the observer. When `nil`, the notification center doesn’t use a notification’s sender to decide whether to deliver it to the observer.

- `suspensionBehavior` — Notification posting behavior when notification delivery is suspended.

## Discussion

The receiver does not retain `notificationObserver`. Therefore, you should always send `NotificationCenter/removeObserver(_:)` or [- removeObserver:name:object:](<removeobserver(__name_object_).md>) to the receiver before releasing `notificationObserver`.

## See Also

### Related Documentation

- [- postNotificationName:object:userInfo:deliverImmediately:](<postnotificationname(__object_userinfo_deliverimmediately_).md>) — Creates a notification with information and an immediate-delivery specifier, and posts it to the receiver.

### Managing Observers

- [- addObserver:selector:name:object:](<addobserver(__selector_name_object_).md>) — Adds an entry to the notification center’s dispatch table with an observer, a selector, and an optional notification name and sender.
- [- removeObserver:name:object:](<removeobserver(__name_object_).md>) — Removes matching entries from the receiver’s dispatch table.
