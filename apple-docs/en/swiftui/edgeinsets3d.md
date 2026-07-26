---
title: EdgeInsets3D
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/edgeinsets3d
source_url: 'https://developer.apple.com/documentation/swiftui/edgeinsets3d'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/edgeinsets3d.json'
content_hash: 'sha256:915b081031e43869'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# EdgeInsets3D

<sub>Structure</sub>

The inset distances for the faces of a 3D volume.

<sub>visionOS</sub>

```swift
@frozen struct EdgeInsets3D
```

## Relationships

- **Conforms To**: [Animatable](animatable.md), [BitwiseCopyable](../swift/bitwisecopyable.md), [Copyable](../swift/copyable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting edge insets

- [top](edgeinsets3d/top.md) — The inset distance along the top face of a 3D volume.
- [bottom](edgeinsets3d/bottom.md) — The inset distance along the bottom face of a 3D volume.
- [leading](edgeinsets3d/leading.md) — The inset distance along the leading face of a 3D volume.
- [trailing](edgeinsets3d/trailing.md) — The inset distance along the top trailing of a 3D volume.
- [front](edgeinsets3d/front.md) — The inset distance along the top front of a 3D volume.
- [back](edgeinsets3d/back.md) — The inset distance along the top back of a 3D volume.

### Creating an edge inset

- [init(horizontal:vertical:depth:)](<edgeinsets3d/init(horizontal_vertical_depth_).md>) — Creates an `EdgeInsets3D` value with values provided for each axis.
- [init(top:leading:bottom:trailing:front:back:)](<edgeinsets3d/init(top_leading_bottom_trailing_front_back_).md>) — Creates an `EdgeInsets3D` value with values provided for each face.

## See Also

### Accessing edges, regions, and layouts

- [Edge](edge.md) — An enumeration to indicate one edge of a rectangle.
- [Edge3D](edge3d.md) — An edge or face of a 3D volume.
- [HorizontalEdge](horizontaledge.md) — An edge on the horizontal axis.
- [VerticalEdge](verticaledge.md) — An edge on the vertical axis.
- [EdgeInsets](edgeinsets.md) — The inset distances for the sides of a rectangle.
