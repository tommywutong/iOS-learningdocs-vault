---
title: NotificationCenter.Publisher
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/notificationcenter/publisher
source_url: 'https://developer.apple.com/documentation/foundation/notificationcenter/publisher'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/notificationcenter/publisher.json'
content_hash: 'sha256:6d421e6384b5e8ea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NotificationCenter](../notificationcenter.md)

# NotificationCenter.Publisher

<sub>Structure</sub>

A publisher that emits elements when broadcasting notifications.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Publisher
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Publisher](../../combine/publisher.md)

## Topics

### Declaring Publisher Topography

- [Output](publisher/output.md) — The kind of values published by this publisher.
- [Failure](publisher/failure.md) — The kind of errors this publisher might publish.

### Creating a Notification Publisher

- [init(center:name:object:)](<publisher/init(center_name_object_).md>) — Creates a publisher that emits events when broadcasting notifications.

### Inspecting Notification Center Properties

- [center](publisher/center.md) — The notification center this publisher uses as a source.
- [name](publisher/name.md) — The name of notifications published by this publisher.
- [object](publisher/object.md) — The object posting the named notfication.

## See Also

### Receiving notifications as a Combine publisher

- [publisher(for:object:)](<publisher(for_object_).md>) — Returns a publisher that emits events when broadcasting notifications.
