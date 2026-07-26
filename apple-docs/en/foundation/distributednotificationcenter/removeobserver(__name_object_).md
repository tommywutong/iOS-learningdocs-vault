---
title: 'removeObserver(_:name:object:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/distributednotificationcenter/removeobserver(_:name:object:)'
source_url: 'https://developer.apple.com/documentation/foundation/distributednotificationcenter/removeobserver(_:name:object:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/distributednotificationcenter/removeobserver%28_%3Aname%3Aobject%3A%29.json'
content_hash: 'sha256:7277878694d5cc46'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DistributedNotificationCenter](../distributednotificationcenter.md)

# removeObserver(_:name:object:)

<sub>Instance Method</sub>

Removes matching entries from the receiver’s dispatch table.

<sub>Mac Catalyst, macOS</sub>

```swift
func removeObserver(_ observer: Any, name aName: NSNotification.Name?, object anObject: String?)
```

## Parameters

- `observer` — Observer to remove from the dispatch table. Specify an observer to remove only entries for this observer. When `nil`, the receiver does not use notification observers as criteria for removal.

- `aName` — Name of the notification to remove from dispatch table. Specify a notification name to remove only entries that specify this notification name. When `nil`, the receiver does not use notification names as criteria for removal.

- `anObject` — Sender to remove from the dispatch table. Specify a notification sender to remove only entries that specify this sender. When `nil`, the receiver does not use notification senders as criteria for removal.

## Discussion

Be sure to invoke this method with `notificationName:nil notificationSender:nil` (or `NotificationCenter/removeObserver(_:)`) before deallocating the observer object.

## See Also

### Managing Observers

- [- addObserver:selector:name:object:](<addobserver(__selector_name_object_).md>) — Adds an entry to the notification center’s dispatch table with an observer, a selector, and an optional notification name and sender.
- [- addObserver:selector:name:object:suspensionBehavior:](<addobserver(__selector_name_object_suspensionbehavior_).md>) — Adds an entry to the receiver’s dispatch table with a specific observer and suspended-notifications behavior, and optional notification name and sender.
