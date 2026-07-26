---
title: 'CFNotificationCenterAddObserver(_:_:_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfnotificationcenteraddobserver(_:_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfnotificationcenteraddobserver(_:_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfnotificationcenteraddobserver%28_%3A_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:2e450faff5a9e804'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFNotificationCenterAddObserver(_:_:_:_:_:_:)

<sub>Function</sub>

Registers an observer to receive notifications.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFNotificationCenterAddObserver(_ center: CFNotificationCenter!, _ observer: UnsafeRawPointer!, _ callBack: CFNotificationCallback!, _ name: CFString!, _ object: UnsafeRawPointer!, _ suspensionBehavior: CFNotificationSuspensionBehavior)
```

## Parameters

- `center` — The notification center to which to add the observer.

- `observer` — The observer. In macOS 10.3 and later, this parameter may be `NULL`.

- `callBack` — The callback function to call when `object` posts the notification named `name`.

- `name` — The name of the notification to observe. If `NULL`, `callback` is called for any notification posted by `object`. If `center` is a Darwin notification center, this value must _not_ be `NULL`.

- `object` — The object to observe. For distributed notifications, `object` must be a CFString object. If `NULL`, `callback` is called when a notification named `name` is posted by any object. If `center` is a Darwin notification center, this value is ignored.

- `suspensionBehavior` — Flag indicating how notifications should be handled when the application is in the background. See [CFNotificationSuspensionBehavior](cfnotificationsuspensionbehavior.md) for the list of available values. If `center` is a Darwin notification center, this value is ignored.

## Discussion

Notification delivery is registered for the main thread.

If you need to control which thread processes a notification, your callback function must be able to forward the notification to the proper thread. You can use a `CFMessagePort` object or a custom `CFRunLoopSource` object to send notifications to the correct thread’s run loop.

## See Also

### Related Documentation

- [CFRunLoopSource](cfrunloopsource.md)
- [CFMessagePort](cfmessageport.md)

### Adding and Removing Observers

- [CFNotificationCenterRemoveEveryObserver](<cfnotificationcenterremoveeveryobserver(____).md>) — Stops an observer from receiving any notifications from any object.
- [CFNotificationCenterRemoveObserver](<cfnotificationcenterremoveobserver(________).md>) — Stops an observer from receiving certain notifications.
