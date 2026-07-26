---
title: 'CFNotificationCenterRemoveObserver(_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfnotificationcenterremoveobserver(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfnotificationcenterremoveobserver(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfnotificationcenterremoveobserver%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:07b9f54292c35cf2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFNotificationCenterRemoveObserver(_:_:_:_:)

<sub>Function</sub>

Stops an observer from receiving certain notifications.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFNotificationCenterRemoveObserver(_ center: CFNotificationCenter!, _ observer: UnsafeRawPointer!, _ name: CFNotificationName!, _ object: UnsafeRawPointer!)
```

## Parameters

- `center` — The notification center to modify.

- `observer` — The observer. This value must not be `NULL`.

- `name` — The name of the notification to stop observing. If `NULL`, `observer` stops receiving callbacks for all notifications posted by `object`.

- `object` — The object to stop observing. For distributed notifications, `object` must be a CFString object. If `NULL`, `observer` stops receiving callbacks for all objects posting notifications named `name`. If `center` is a Darwin notification center, this value is ignored.

## Discussion

If both `name` and `object` are `NULL`, this function unregisters `observer` from all the notifications for which it had previously registered with `center`.

## See Also

### Adding and Removing Observers

- [CFNotificationCenterAddObserver](<cfnotificationcenteraddobserver(____________).md>) — Registers an observer to receive notifications.
- [CFNotificationCenterRemoveEveryObserver](<cfnotificationcenterremoveeveryobserver(____).md>) — Stops an observer from receiving any notifications from any object.
