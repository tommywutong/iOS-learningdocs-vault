---
title: 'addObserver(_:selector:name:object:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/distributednotificationcenter/addobserver(_:selector:name:object:)'
source_url: 'https://developer.apple.com/documentation/foundation/distributednotificationcenter/addobserver(_:selector:name:object:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/distributednotificationcenter/addobserver%28_%3Aselector%3Aname%3Aobject%3A%29.json'
content_hash: 'sha256:0425e96f056f2258'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DistributedNotificationCenter](../distributednotificationcenter.md)

# addObserver(_:selector:name:object:)

<sub>Instance Method</sub>

Adds an entry to the notification center’s dispatch table with an observer, a selector, and an optional notification name and sender.

<sub>Mac Catalyst, macOS</sub>

```swift
func addObserver(_ observer: Any, selector aSelector: Selector, name aName: NSNotification.Name?, object anObject: String?)
```

## Parameters

- `observer` — An object registering as an observer.

- `aSelector` — A selector that the notification center sends `notificationObserver` to notify when posting the notification.

- `aName` — The name of the notification for which to register the observer; that is, only notifications with this name are delivered to the observer. When `nil`, the notification center doesn’t use a notification’s name to decide whether to deliver it to the observer.

- `anObject` — The object whose notifications the observer wants to receive; that is, only notifications sent by this sender are delivered to the observer. When `nil`, the notification center doesn’t use a notification’s sender to decide whether to deliver it to the observer.

## Discussion

This method calls [- addObserver:selector:name:object:suspensionBehavior:](<addobserver(__selector_name_object_suspensionbehavior_).md>), passing [NSNotificationSuspensionBehaviorCoalesce](suspensionbehavior/coalesce.md) for `suspensionBehavior`.

## See Also

### Managing Observers

- [- addObserver:selector:name:object:suspensionBehavior:](<addobserver(__selector_name_object_suspensionbehavior_).md>) — Adds an entry to the receiver’s dispatch table with a specific observer and suspended-notifications behavior, and optional notification name and sender.
- [- removeObserver:name:object:](<removeobserver(__name_object_).md>) — Removes matching entries from the receiver’s dispatch table.
