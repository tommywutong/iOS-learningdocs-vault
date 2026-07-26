---
title: ViewDimensions3D
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/viewdimensions3d
source_url: 'https://developer.apple.com/documentation/swiftui/viewdimensions3d'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/viewdimensions3d.json'
content_hash: 'sha256:371893e048f087ec'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ViewDimensions3D

<sub>Structure</sub>

A view’s 3D size and alignment guides in its own coordinate space.

<sub>visionOS</sub>

```swift
struct ViewDimensions3D
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md)

## Topics

### Instance Properties

- [depth](viewdimensions3d/depth.md) — The view’s depth.
- [height](viewdimensions3d/height.md) — The view’s height.
- [width](viewdimensions3d/width.md) — The view’s width.

### Subscripts

- [subscript(_:)](<viewdimensions3d/subscript(__).md>) — Gets the value of the given depth guide.
- [subscript(explicit:)](<viewdimensions3d/subscript(explicit_).md>) — Gets the explicit value of the given depth alignment guide

## See Also

### Aligning views

- [Aligning views within a stack](aligning-views-within-a-stack.md) — Position views inside a stack using alignment guides.
- [Aligning views across stacks](aligning-views-across-stacks.md) — Create a custom alignment and use it to align views across multiple stacks.
- [alignmentGuide(_:computeValue:)](<view/alignmentguide(__computevalue_).md>) — Sets the view’s horizontal alignment.
- [Alignment](alignment.md) — An alignment in both axes.
- [HorizontalAlignment](horizontalalignment.md) — An alignment position along the horizontal axis.
- [VerticalAlignment](verticalalignment.md) — An alignment position along the vertical axis.
- [DepthAlignment](depthalignment.md) — An alignment position along the depth axis.
- [AlignmentID](alignmentid.md) — A type that you use to create custom alignment guides.
- [ViewDimensions](viewdimensions.md) — A view’s size and alignment guides in its own coordinate space.
- [SpatialContainer](spatialcontainer.md) — A layout container that aligns overlapping content in 3D space.
