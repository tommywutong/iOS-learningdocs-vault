---
title: CoordinateSpace
framework: SwiftUI
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/coordinatespace
source_url: 'https://developer.apple.com/documentation/swiftui/coordinatespace'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/coordinatespace.json'
content_hash: 'sha256:96df815620e29109'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# CoordinateSpace

<sub>Enumeration</sub>

A resolved coordinate space created by the coordinate space protocol.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum CoordinateSpace
```

## Overview

You don’t typically use `CoordinateSpace` directly. Instead, use the static properties and functions of `CoordinateSpaceProtocol` such as `.global`, `.local`, and `.named(_:)`.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Getting coordinate spaces

- [CoordinateSpace.global](coordinatespace/global.md) — The global coordinate space at the root of the view hierarchy.
- [CoordinateSpace.local](coordinatespace/local.md) — The local coordinate space of the current view.
- [CoordinateSpace.named(_:)](<coordinatespace/named(__).md>) — A named reference to a view’s local coordinate space.

### Testing a space

- [isGlobal](coordinatespace/isglobal.md)
- [isLocal](coordinatespace/islocal.md)

## See Also

### Measuring a view

- [GeometryReader](geometryreader.md) — A container view that defines its content as a function of its own size and coordinate space.
- [GeometryReader3D](geometryreader3d.md) — A container view that defines its content as a function of its own size and coordinate space.
- [GeometryProxy](geometryproxy.md) — A proxy for access to the size and coordinate space (for anchor resolution) of the container view.
- [GeometryProxy3D](geometryproxy3d.md) — A proxy for access to the size and coordinate space of the container view.
- [coordinateSpace(_:)](<view/coordinatespace(__).md>) — Assigns a name to the view’s coordinate space, so other code can operate on dimensions like points and sizes relative to the named space.
- [CoordinateSpaceProtocol](coordinatespaceprotocol.md) — A frame of reference within the layout system.
- [PhysicalMetric](physicalmetric.md) — Provides access to a value in points that corresponds to the specified physical measurement.
- [PhysicalMetricsConverter](physicalmetricsconverter.md) — A physical metrics converter provides conversion between point values and their extent in 3D space, in the form of physical length measurements.
