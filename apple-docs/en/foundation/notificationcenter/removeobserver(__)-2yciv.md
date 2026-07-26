---
title: 'removeObserver(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/notificationcenter/removeobserver(_:)-2yciv'
source_url: 'https://developer.apple.com/documentation/foundation/notificationcenter/removeobserver(_:)-2yciv'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/notificationcenter/removeobserver%28_%3A%29-2yciv.json'
content_hash: 'sha256:9c5001a59d3f6d78'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NotificationCenter](../notificationcenter.md)

# removeObserver(_:)

<sub>Instance Method</sub>

Removes all entries specifying an observer from the notification center’s dispatch table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func removeObserver(_ observer: Any)
```

## Parameters

- `observer` — The observer to remove from the dispatch table. Specify an observer to remove only entries for this observer.

## Discussion

Removing the observer stops it from receiving notifications.

If you used [- addObserverForName:object:queue:usingBlock:](<addobserver(forname_object_queue_using_).md>) to create your observer, you should call this method or [- removeObserver:name:object:](<removeobserver(__name_object_).md>) before the system deallocates any object that [- addObserverForName:object:queue:usingBlock:](<addobserver(forname_object_queue_using_).md>) specifies.

If your app targets iOS 9.0 and later or macOS 10.11 and later, and you used [- addObserver:selector:name:object:](<addobserver(__selector_name_object_).md>), you do not need to unregister the observer. If you forget or are unable to remove the observer, the system cleans up the next time it would have posted to it.

When removing an observer, remove it with the most specific detail possible. For example, if you used a name and object to register the observer, use [- removeObserver:name:object:](<removeobserver(__name_object_).md>) with the name and object.

> [!important] Important
> You shouldn’t use this method to remove all observers from a long-lived object because your code may not be the only code adding observers that involve the object.

The following example illustrates how to unregister `someObserver` for all previously registered notifications. This is safe to do in the [dealloc](../../objectivec/nsobject-swift.class/dealloc.md) method, but you shouldn’t use it otherwise (use [- removeObserver:name:object:](<removeobserver(__name_object_).md>) instead).

**Swift**

```swift
NotificationCenter.default.removeObserver(someObserver)
```

**Objective-C**

```objc
[[NSNotificationCenter defaultCenter] removeObserver:someObserver];
```

## See Also

### Adding and removing notification observers

- [- addObserverForName:object:queue:usingBlock:](<addobserver(forname_object_queue_using_).md>) — Adds an entry to the notification center to receive notifications that passed to the provided block.
- [- addObserver:selector:name:object:](<addobserver(__selector_name_object_).md>) — Adds an entry to the notification center to call the provided selector with the notification.
- [- removeObserver:name:object:](<removeobserver(__name_object_).md>) — Removes matching entries from the notification center’s dispatch table.
