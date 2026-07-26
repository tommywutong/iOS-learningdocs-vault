---
title: default
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/notificationcenter/default
source_url: 'https://developer.apple.com/documentation/foundation/notificationcenter/default'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/notificationcenter/default.json'
content_hash: 'sha256:1b9fe9ed7a8befdc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NotificationCenter](../notificationcenter.md)

# default

<sub>Type Property</sub>

The app’s default notification center.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var `default`: NotificationCenter { get }
```

## Discussion

All system notifications sent to an app are posted to the [defaultCenter](default.md) notification center. You can also post your own notifications there.

If your app uses notifications extensively, you may want to create and post to your own notification centers rather than posting only to the [defaultCenter](default.md) notification center. When a notification is posted to a notification center, the notification center scans through the list of registered observers, which may slow down your app. By organizing notifications functionally around one or more notification centers, less work is done each time a notification is posted, which can improve performance throughout your app.

## See Also

### Related Documentation

- [Notification Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Notifications/Introduction/introNotifications.html#//apple_ref/doc/uid/10000043i)
