---
title: targetedToAnyEntity()
framework: RealityKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/gesture/targetedtoanyentity()
source_url: 'https://developer.apple.com/documentation/swiftui/gesture/targetedtoanyentity()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/gesture/targetedtoanyentity%28%29.json'
content_hash: 'sha256:41522698bdb0f017'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Gesture](../gesture.md)

# targetedToAnyEntity()

<sub>Instance Method</sub>

Requires this gesture to target an entity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor @preconcurrency func targetedToAnyEntity() -> some Gesture<EntityTargetValue<Self.Value>>

```

## Return Value

A `RealityCoordinateSpaceConvertible`value containing the original gesture value along with the targeted entity.

## See Also

### Using a gesture with a RealityKit entity

- [targetedToEntity(_:)](<targetedtoentity(__).md>) — Requires this gesture to target an entity or a descendant of entity.
- [targetedToEntity(where:)](<targetedtoentity(where_).md>) — Requires this gesture to target an entity that can be found in the results of the query.
