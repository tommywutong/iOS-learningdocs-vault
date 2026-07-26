---
title: 'init(center:name:object:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/notificationcenter/publisher/init(center:name:object:)'
source_url: 'https://developer.apple.com/documentation/foundation/notificationcenter/publisher/init(center:name:object:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/notificationcenter/publisher/init%28center%3Aname%3Aobject%3A%29.json'
content_hash: 'sha256:08046b0b5abedf1b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NotificationCenter](../../notificationcenter.md) · [Publisher](../publisher.md)

# init(center:name:object:)

<sub>Initializer</sub>

Creates a publisher that emits events when broadcasting notifications.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(center: NotificationCenter, name: Notification.Name, object: AnyObject? = nil)
```

## Parameters

- `center` — The notification center to publish notifications for.

- `name` — The name of the notification to publish.

- `object` — The object posting the named notfication. If `nil`, the publisher emits elements for any object producing a notification with the given name.
