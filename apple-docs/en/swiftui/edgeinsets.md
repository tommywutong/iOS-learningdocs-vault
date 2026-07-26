---
title: EdgeInsets
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/edgeinsets
source_url: 'https://developer.apple.com/documentation/swiftui/edgeinsets'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/edgeinsets.json'
content_hash: 'sha256:6a2a3a3b3469cbd3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# EdgeInsets

<sub>Structure</sub>

The inset distances for the sides of a rectangle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct EdgeInsets
```

## Relationships

- **Conforms To**: [Animatable](animatable.md), [BitwiseCopyable](../swift/bitwisecopyable.md), [Copyable](../swift/copyable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting edge insets

- [top](edgeinsets/top.md)
- [bottom](edgeinsets/bottom.md)
- [leading](edgeinsets/leading.md)
- [trailing](edgeinsets/trailing.md)

### Creating an edge inset

- [init()](<edgeinsets/init().md>)
- [init(top:leading:bottom:trailing:)](<edgeinsets/init(top_leading_bottom_trailing_).md>)
- [init(_:)](<edgeinsets/init(__).md>) — Creates a 2D `EdgeInsets` from an `EdgeInsets3D`, dropping its `front` and `back` values.

### Instance Methods

- [inset(by:edges:)](<edgeinsets/inset(by_edges_).md>) — Returns an inset that has been modified by the corner sizes in the specified edges. When two corner insets diverge in their values for the specified edge, the maximum inset value will be used. For example, when the top edge is specified, the top inset will be adjusted by the larger of the two heights from the top leading and trailing corner inset sizes.

## See Also

### Accessing edges, regions, and layouts

- [Edge](edge.md) — An enumeration to indicate one edge of a rectangle.
- [Edge3D](edge3d.md) — An edge or face of a 3D volume.
- [HorizontalEdge](horizontaledge.md) — An edge on the horizontal axis.
- [VerticalEdge](verticaledge.md) — An edge on the vertical axis.
- [EdgeInsets3D](edgeinsets3d.md) — The inset distances for the faces of a 3D volume.
