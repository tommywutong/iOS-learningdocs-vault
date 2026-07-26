---
title: Edge3D
framework: SwiftUI
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/edge3d
source_url: 'https://developer.apple.com/documentation/swiftui/edge3d'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/edge3d.json'
content_hash: 'sha256:a0690b06a35e053c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# Edge3D

<sub>Enumeration</sub>

An edge or face of a 3D volume.

<sub>visionOS</sub>

```swift
@frozen enum Edge3D
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [CaseIterable](../swift/caseiterable.md), [Copyable](../swift/copyable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting the edges

- [Edge3D.top](edge3d/top.md)
- [Edge3D.bottom](edge3d/bottom.md)
- [Edge3D.leading](edge3d/leading.md)
- [Edge3D.trailing](edge3d/trailing.md)
- [Edge3D.front](edge3d/front.md)
- [Edge3D.back](edge3d/back.md)

### Creating an edge

- [init(_:)](<edge3d/init(__).md>)

### Accessing sets of edges

- [Set](edge3d/set.md) — An efficient set of 3D edges.

## See Also

### Accessing edges, regions, and layouts

- [Edge](edge.md) — An enumeration to indicate one edge of a rectangle.
- [HorizontalEdge](horizontaledge.md) — An edge on the horizontal axis.
- [VerticalEdge](verticaledge.md) — An edge on the vertical axis.
- [EdgeInsets](edgeinsets.md) — The inset distances for the sides of a rectangle.
- [EdgeInsets3D](edgeinsets3d.md) — The inset distances for the faces of a 3D volume.
