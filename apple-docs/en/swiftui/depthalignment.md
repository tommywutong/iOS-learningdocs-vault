---
title: DepthAlignment
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/depthalignment
source_url: 'https://developer.apple.com/documentation/swiftui/depthalignment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/depthalignment.json'
content_hash: 'sha256:6873e0b77fcd5669'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# DepthAlignment

<sub>Structure</sub>

An alignment position along the depth axis.

<sub>visionOS</sub>

```swift
@frozen struct DepthAlignment
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting guides

- [back](depthalignment/back.md) — A guide marking the bottom edge of the view.
- [center](depthalignment/center.md) — A guide marking the vertical center of the view.
- [front](depthalignment/front.md) — A guide marking the top edge of the view.

### Initializers

- [init(_:)](<depthalignment/init(__).md>)

### Instance Methods

- [combineExplicit(_:)](<depthalignment/combineexplicit(__).md>)

## See Also

### Aligning views

- [Aligning views within a stack](aligning-views-within-a-stack.md) — Position views inside a stack using alignment guides.
- [Aligning views across stacks](aligning-views-across-stacks.md) — Create a custom alignment and use it to align views across multiple stacks.
- [alignmentGuide(_:computeValue:)](<view/alignmentguide(__computevalue_).md>) — Sets the view’s horizontal alignment.
- [Alignment](alignment.md) — An alignment in both axes.
- [HorizontalAlignment](horizontalalignment.md) — An alignment position along the horizontal axis.
- [VerticalAlignment](verticalalignment.md) — An alignment position along the vertical axis.
- [AlignmentID](alignmentid.md) — A type that you use to create custom alignment guides.
- [ViewDimensions](viewdimensions.md) — A view’s size and alignment guides in its own coordinate space.
- [ViewDimensions3D](viewdimensions3d.md) — A view’s 3D size and alignment guides in its own coordinate space.
- [SpatialContainer](spatialcontainer.md) — A layout container that aligns overlapping content in 3D space.
