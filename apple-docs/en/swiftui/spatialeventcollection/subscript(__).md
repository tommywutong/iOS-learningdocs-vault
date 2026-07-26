---
title: 'subscript(_:)'
framework: SwiftUI
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, visionOS 1.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/spatialeventcollection/subscript(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/spatialeventcollection/subscript(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/spatialeventcollection/subscript%28_%3A%29.json'
content_hash: 'sha256:829badae1e8df9b2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SpatialEventCollection](../spatialeventcollection.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Retrieves an event using its unique identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
subscript(index: SpatialEventCollection.Event.ID) -> SpatialEventCollection.Event? { get }
```

## Overview

Returns `nil` if the `Event` no longer exists in the collection.

## See Also

### Accessing the collection’s events

- [Event](event.md) — A spatial event generated from an input like a touch or click that can drive gestures in the system.
