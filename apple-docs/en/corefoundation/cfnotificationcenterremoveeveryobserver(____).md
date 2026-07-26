---
title: 'CFNotificationCenterRemoveEveryObserver(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfnotificationcenterremoveeveryobserver(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfnotificationcenterremoveeveryobserver(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfnotificationcenterremoveeveryobserver%28_%3A_%3A%29.json'
content_hash: 'sha256:bc20a699f8227c73'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFNotificationCenterRemoveEveryObserver(_:_:)

<sub>Function</sub>

Stops an observer from receiving any notifications from any object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFNotificationCenterRemoveEveryObserver(_ center: CFNotificationCenter!, _ observer: UnsafeRawPointer!)
```

## Parameters

- `center` — The notification center from which to remove observers.

- `observer` — The observer. This value must not be `NULL`.

## Discussion

If you no longer want an observer to receive any notifications, perhaps because the observer is being deallocated, you can call this function to unregister the observer from all the notifications for which it had previously registered.

## See Also

### Adding and Removing Observers

- [CFNotificationCenterAddObserver](<cfnotificationcenteraddobserver(____________).md>) — Registers an observer to receive notifications.
- [CFNotificationCenterRemoveObserver](<cfnotificationcenterremoveobserver(________).md>) — Stops an observer from receiving certain notifications.
