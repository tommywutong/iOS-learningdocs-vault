---
title: 'targetedToEntity(where:)'
framework: RealityKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/gesture/targetedtoentity(where:)'
source_url: 'https://developer.apple.com/documentation/swiftui/gesture/targetedtoentity(where:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/gesture/targetedtoentity%28where%3A%29.json'
content_hash: 'sha256:5a95f049548201a5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Gesture](../gesture.md)

# targetedToEntity(where:)

<sub>Instance Method</sub>

Requires this gesture to target an entity that can be found in the results of the query.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor @preconcurrency func targetedToEntity(where query: QueryPredicate<Entity>) -> some Gesture<EntityTargetValue<Self.Value>>

```

## Parameters

- `query` — A query to filter which entity the gesture targets.

## Return Value

A `RealityCoordinateSpaceConverting` value containing the original gesture value along with the targeted entity.

## See Also

### Using a gesture with a RealityKit entity

- [targetedToAnyEntity()](<targetedtoanyentity().md>) — Requires this gesture to target an entity.
- [targetedToEntity(_:)](<targetedtoentity(__).md>) — Requires this gesture to target an entity or a descendant of entity.
