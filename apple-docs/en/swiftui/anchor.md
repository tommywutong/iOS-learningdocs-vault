---
title: Anchor
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/anchor
source_url: 'https://developer.apple.com/documentation/swiftui/anchor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/anchor.json'
content_hash: 'sha256:8203b3e0bb92f4f5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# Anchor

<sub>Structure</sub>

An opaque value derived from an anchor source and a particular view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct Anchor<Value>
```

## Overview

You can convert the anchor to a `Value` in the coordinate space of a target view by using a [GeometryProxy](geometryproxy.md) to specify the target view.

## Relationships

- **Conforms To**: [CoordinateSpaceValue3D](../spatial/coordinatespacevalue3d.md), [Copyable](../swift/copyable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting the anchor’s source

- [Source](anchor/source.md) — A type-erased geometry value that produces an anchored value of a given type.

## See Also

### Accessing geometric constructs

- [Axis](axis.md) — The horizontal or vertical dimension in a 2D coordinate system.
- [Angle](angle.md) — A geometric angle whose value you access in either radians or degrees.
- [UnitPoint](unitpoint.md) — A normalized 2D point in a view’s coordinate space.
- [UnitPoint3D](unitpoint3d.md) — A normalized 3D point in a view’s coordinate space.
- [DepthAlignmentID](depthalignmentid.md)
- [Alignment3D](alignment3d.md) — An alignment in all three axes.
- [GeometryProxyCoordinateSpace3D](geometryproxycoordinatespace3d.md) — A representation of a `GeometryProxy3D` which can be used for `CoordinateSpace3D` based conversions.
