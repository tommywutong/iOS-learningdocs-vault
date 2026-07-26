---
title: 'publisher(for:object:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/notificationcenter/publisher(for:object:)'
source_url: 'https://developer.apple.com/documentation/foundation/notificationcenter/publisher(for:object:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/notificationcenter/publisher%28for%3Aobject%3A%29.json'
content_hash: 'sha256:3f0ceb997bf69875'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NotificationCenter](../notificationcenter.md)

# publisher(for:object:)

<sub>Instance Method</sub>

Returns a publisher that emits events when broadcasting notifications.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func publisher(for name: Notification.Name, object: AnyObject? = nil) -> NotificationCenter.Publisher
```

## Parameters

- `name` — The name of the notification to publish.

- `object` — The object posting the named notification. If `nil`, the publisher emits elements for any object producing a notification with the given name.

## Return Value

A [Publisher](../../combine/publisher.md) that emits events when broadcasting notifications.

## See Also

### Receiving notifications as a Combine publisher

- [Publisher](publisher.md) — A publisher that emits elements when broadcasting notifications.
