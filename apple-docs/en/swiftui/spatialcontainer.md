---
title: SpatialContainer
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/spatialcontainer
source_url: 'https://developer.apple.com/documentation/swiftui/spatialcontainer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/spatialcontainer.json'
content_hash: 'sha256:af3357d5c9f1b652'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# SpatialContainer

<sub>Structure</sub>

A layout container that aligns overlapping content in 3D space.

<sub>visionOS</sub>

```swift
@frozen struct SpatialContainer
```

## Overview

The container will take the max size of each dimension of each of its children, aligning its children based on the `alignment`.

## Relationships

- **Conforms To**: [Animatable](animatable.md), [Copyable](../swift/copyable.md), [Escapable](../swift/escapable.md), [Layout](layout.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(alignment:)](<spatialcontainer/init(alignment_).md>) — Creates a spatial container layout with the specified 3D alignment.

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
- [ViewDimensions3D](viewdimensions3d.md) — A view’s 3D size and alignment guides in its own coordinate space.
