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
doc_path: /documentation/foundation/notificationqueue/default
source_url: 'https://developer.apple.com/documentation/foundation/notificationqueue/default'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/notificationqueue/default.json'
content_hash: 'sha256:53338541d50b757f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NotificationQueue](../notificationqueue.md)

# default

<sub>Type Property</sub>

Returns the default notification queue for the current thread.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var `default`: NotificationQueue { get }
```

## Return Value

Returns the default notification queue for the current thread.

## Discussion

This notification queue uses the default notification center.
