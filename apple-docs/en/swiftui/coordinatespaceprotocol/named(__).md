---
title: 'named(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/coordinatespaceprotocol/named(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/coordinatespaceprotocol/named(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/coordinatespaceprotocol/named%28_%3A%29.json'
content_hash: 'sha256:4b48313c0838a8d1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [CoordinateSpaceProtocol](../coordinatespaceprotocol.md)

# named(_:)

<sub>Type Method</sub>

Creates a named coordinate space using the given value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func named(_ name: some Hashable) -> NamedCoordinateSpace
```

## Parameters

- `name` — A unique value that identifies the coordinate space.

## Return Value

A named coordinate space identified by the given value.

## Discussion

Use the `coordinateSpace(_:)` modifier to assign a name to the local coordinate space of a  parent view. Child views can then refer to that coordinate space using `.named(_:)`.

## See Also

### Getting built-in coordinate spaces

- [immersiveSpace](immersivespace.md) — The named coordinate space that represents the currently opened [ImmersiveSpace](../immersivespace.md) scene. If no immersive space is currently opened, this CoordinateSpace provides the same behavior as the `.global` coordinate space.
- [global](global.md) — The global coordinate space at the root of the view hierarchy.
- [local](local.md) — The local coordinate space of the current view.
- [scrollView](scrollview.md) — The named coordinate space that is added by the system for the innermost containing scroll view.
- [scrollView(axis:)](<scrollview(axis_).md>) — The named coordinate space that is added by the system for the innermost containing scroll view that allows scrolling along the provided axis.
