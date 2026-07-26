---
title: Alignment3D
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/alignment3d
source_url: 'https://developer.apple.com/documentation/swiftui/alignment3d'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/alignment3d.json'
content_hash: 'sha256:58434cbcffcd0646'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# Alignment3D

<sub>Structure</sub>

An alignment in all three axes.

<sub>visionOS</sub>

```swift
@frozen struct Alignment3D
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(horizontal:vertical:depth:)](<alignment3d/init(horizontal_vertical_depth_).md>) — Creates a custom alignment value with the specified horizontal, vertical and depth alignment guides.

### Instance Properties

- [depth](alignment3d/depth.md) — The alignment on the depth axis.
- [horizontal](alignment3d/horizontal.md) — The alignment on the horizontal axis.
- [vertical](alignment3d/vertical.md) — The alignment on the vertical axis.

### Type Properties

- [back](alignment3d/back.md) — A guide representing a point at the center of the horizontal axis, center of the vertical axis, and back of the depth axis.
- [bottom](alignment3d/bottom.md) — A guide representing a point at the center of the horizontal axis, bottom of the vertical axis, and center of the depth axis.
- [bottomBack](alignment3d/bottomback.md) — A guide representing a point at the center of the horizontal axis, bottom of the vertical axis, and back of the depth axis.
- [bottomFront](alignment3d/bottomfront.md) — A guide representing a point at the center of the horizontal axis, bottom of the vertical axis, and front of the depth axis.
- [bottomLeading](alignment3d/bottomleading.md) — A guide representing a point at the leading edge of the horizontal axis, bottom of the vertical axis, and center of the depth axis.
- [bottomLeadingBack](alignment3d/bottomleadingback.md) — A guide representing a point at the leading edge of the horizontal axis, bottom of the vertical axis, and back of the depth axis.
- [bottomLeadingFront](alignment3d/bottomleadingfront.md) — A guide representing a point at the leading edge of the horizontal axis, bottom of the vertical axis, and front of the depth axis.
- [bottomTrailing](alignment3d/bottomtrailing.md) — A guide representing a point at the trailing edge of the horizontal axis, bottom of the vertical axis, and center of the depth axis.
- [bottomTrailingBack](alignment3d/bottomtrailingback.md) — A guide representing a point at the trailing edge of the horizontal axis, bottom of the vertical axis, and back of the depth axis.
- [bottomTrailingFront](alignment3d/bottomtrailingfront.md) — A guide representing a point at the trailing edge of the horizontal axis, bottom of the vertical axis, and front of the depth axis.
- [center](alignment3d/center.md) — A guide representing a point at the center of the horizontal axis, center of the vertical axis, and center of the depth axis.
- [front](alignment3d/front.md) — A guide representing a point at the center of the horizontal axis, center of the vertical axis, and front of the depth axis.
- [leading](alignment3d/leading.md) — A guide representing a point at the leading edge of the horizontal axis, center of the vertical axis, and center of the depth axis.
- [leadingBack](alignment3d/leadingback.md) — A guide representing a point at the leading edge of the horizontal axis, center of the vertical axis, and back of the depth axis.
- [leadingFront](alignment3d/leadingfront.md) — A guide representing a point at the leading edge of the horizontal axis, center of the vertical axis, and front of the depth axis.
- [top](alignment3d/top.md) — A guide representing a point at the center of the horizontal axis, top of the vertical axis, and center of the depth axis.
- [topBack](alignment3d/topback.md) — A guide representing a point at the center of the horizontal axis, top of the vertical axis, and back of the depth axis.
- [topFront](alignment3d/topfront.md) — A guide representing a point at the center of the horizontal axis, top of the vertical axis, and front of the depth axis.
- [topLeading](alignment3d/topleading.md) — A guide representing a point at the center of the horizontal axis, top of the vertical axis, and center of the depth axis.
- [topLeadingBack](alignment3d/topleadingback.md) — A guide representing a point at the leading edge of the horizontal axis, top of the vertical axis, and back of the depth axis.
- [topLeadingFront](alignment3d/topleadingfront.md) — A guide representing a point at the leading edge of the horizontal axis, top of the vertical axis, and front of the depth axis.
- [topTrailing](alignment3d/toptrailing.md) — A guide representing a point at the trailing edge of the horizontal axis, top of the vertical axis, and center of the depth axis.
- [topTrailingBack](alignment3d/toptrailingback.md) — A guide representing a point at the trailing edge of the horizontal axis, top of the vertical axis, and back of the depth axis.
- [topTrailingFront](alignment3d/toptrailingfront.md) — A guide representing a point at the trailing edge of the horizontal axis, top of the vertical axis, and front of the depth axis.
- [trailing](alignment3d/trailing.md) — A guide representing a point at the trailing edge of the horizontal axis, center of the vertical axis, and center of the depth axis.
- [trailingBack](alignment3d/trailingback.md) — A guide representing a point at the trailing edge of the horizontal axis, center of the vertical axis, and back of the depth axis.
- [trailingFront](alignment3d/trailingfront.md) — A guide representing a point at the trailing edge of the horizontal axis, center of the vertical axis, and front of the depth axis.

## See Also

### Accessing geometric constructs

- [Axis](axis.md) — The horizontal or vertical dimension in a 2D coordinate system.
- [Angle](angle.md) — A geometric angle whose value you access in either radians or degrees.
- [UnitPoint](unitpoint.md) — A normalized 2D point in a view’s coordinate space.
- [UnitPoint3D](unitpoint3d.md) — A normalized 3D point in a view’s coordinate space.
- [Anchor](anchor.md) — An opaque value derived from an anchor source and a particular view.
- [DepthAlignmentID](depthalignmentid.md)
- [GeometryProxyCoordinateSpace3D](geometryproxycoordinatespace3d.md) — A representation of a `GeometryProxy3D` which can be used for `CoordinateSpace3D` based conversions.
