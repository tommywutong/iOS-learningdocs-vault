---
title: Edge
framework: SwiftUI
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/edge
source_url: 'https://developer.apple.com/documentation/swiftui/edge'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/edge.json'
content_hash: 'sha256:39643e99eae87c79'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# Edge

<sub>Enumeration</sub>

An enumeration to indicate one edge of a rectangle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen enum Edge
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [CaseIterable](../swift/caseiterable.md), [Copyable](../swift/copyable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting the edges

- [Edge.top](edge/top.md)
- [Edge.bottom](edge/bottom.md)
- [Edge.leading](edge/leading.md)
- [Edge.trailing](edge/trailing.md)

### Creating an edge

- [init(_:)](<edge/init(__).md>) — Converts a 3D edge to a 2D edge, if possible.

### Accessing sets of edges

- [Set](edge/set.md) — An efficient set of edges.

### Enumerations

- [Corner](edge/corner.md) — An enumeration to indicate one corner of a rectangle.

## See Also

### Accessing edges, regions, and layouts

- [Edge3D](edge3d.md) — An edge or face of a 3D volume.
- [HorizontalEdge](horizontaledge.md) — An edge on the horizontal axis.
- [VerticalEdge](verticaledge.md) — An edge on the vertical axis.
- [EdgeInsets](edgeinsets.md) — The inset distances for the sides of a rectangle.
- [EdgeInsets3D](edgeinsets3d.md) — The inset distances for the faces of a 3D volume.
