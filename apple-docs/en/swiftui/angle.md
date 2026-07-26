---
title: Angle
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/angle
source_url: 'https://developer.apple.com/documentation/swiftui/angle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/angle.json'
content_hash: 'sha256:102b3607c597a1a5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# Angle

<sub>Structure</sub>

A geometric angle whose value you access in either radians or degrees.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct Angle
```

## Relationships

- **Conforms To**: [Animatable](animatable.md), [BitwiseCopyable](../swift/bitwisecopyable.md), [Comparable](../swift/comparable.md), [Copyable](../swift/copyable.md), [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting constant angles

- [zero](angle/zero.md)
- [degrees(_:)](<angle/degrees(__).md>)
- [radians(_:)](<angle/radians(__).md>)

### Creating an angle

- [init()](<angle/init().md>)
- [init(degrees:)](<angle/init(degrees_).md>)
- [init(radians:)](<angle/init(radians_).md>)
- [init(_:)](<angle/init(__).md>)

### Getting the angle size

- [degrees](angle/degrees.md)
- [radians](angle/radians.md)

## See Also

### Accessing geometric constructs

- [Axis](axis.md) — The horizontal or vertical dimension in a 2D coordinate system.
- [UnitPoint](unitpoint.md) — A normalized 2D point in a view’s coordinate space.
- [UnitPoint3D](unitpoint3d.md) — A normalized 3D point in a view’s coordinate space.
- [Anchor](anchor.md) — An opaque value derived from an anchor source and a particular view.
- [DepthAlignmentID](depthalignmentid.md)
- [Alignment3D](alignment3d.md) — An alignment in all three axes.
- [GeometryProxyCoordinateSpace3D](geometryproxycoordinatespace3d.md) — A representation of a `GeometryProxy3D` which can be used for `CoordinateSpace3D` based conversions.
