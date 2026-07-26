---
title: 'removeObserver(_:name:object:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/notificationcenter/removeobserver(_:name:object:)'
source_url: 'https://developer.apple.com/documentation/foundation/notificationcenter/removeobserver(_:name:object:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/notificationcenter/removeobserver%28_%3Aname%3Aobject%3A%29.json'
content_hash: 'sha256:d387fa7e4b9ba266'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NotificationCenter](../notificationcenter.md)

# removeObserver(_:name:object:)

<sub>Instance Method</sub>

Removes matching entries from the notification center’s dispatch table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func removeObserver(_ observer: Any, name aName: NSNotification.Name?, object anObject: Any?)
```

## Parameters

- `observer` — The observer to remove from the dispatch table. Specify an observer to remove only entries for this observer.

- `aName` — The name of the notification to remove from the dispatch table. Specify a notification name to remove only entries with this notification name. When `nil`, the receiver does not use notification names as criteria for removal.

- `anObject` — The sender to remove from the dispatch table. Specify a notification sender to remove only entries with this sender. When `nil`, the receiver does not use a sender as criteria for removal.

## Discussion

Removing the observer stops it from receiving notifications.

If you used [- addObserverForName:object:queue:usingBlock:](<addobserver(forname_object_queue_using_).md>) to create your observer, you should call this method or `NotificationCenter/removeObserver(_:)` before the system deallocates any object that [- addObserverForName:object:queue:usingBlock:](<addobserver(forname_object_queue_using_).md>) specifies.

If your app targets iOS 9.0 and later or macOS 10.11 and later, and you used [- addObserver:selector:name:object:](<addobserver(__selector_name_object_).md>) to create your observer, you do not need to unregister the observer. If you forget or are unable to remove the observer, the system cleans up the next time it would have posted to it.

When unregistering an observer, use the most specific detail possible. For example, if you used a name and object to register the observer, use [- removeObserver:name:object:](<removeobserver(__name_object_).md>) with the name and object.

## See Also

### Adding and removing notification observers

- [- addObserverForName:object:queue:usingBlock:](<addobserver(forname_object_queue_using_).md>) — Adds an entry to the notification center to receive notifications that passed to the provided block.
- [- addObserver:selector:name:object:](<addobserver(__selector_name_object_).md>) — Adds an entry to the notification center to call the provided selector with the notification.
- [- removeObserver:](<removeobserver(__)-2yciv.md>) — Removes all entries specifying an observer from the notification center’s dispatch table.
