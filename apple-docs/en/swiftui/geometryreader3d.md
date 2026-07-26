---
title: GeometryReader3D
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/geometryreader3d
source_url: 'https://developer.apple.com/documentation/swiftui/geometryreader3d'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/geometryreader3d.json'
content_hash: 'sha256:1410e0a9cce4f7d3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# GeometryReader3D

<sub>Structure</sub>

A container view that defines its content as a function of its own size and coordinate space.

<sub>visionOS</sub>

```swift
@frozen nonisolated struct GeometryReader3D<Content> where Content : View
```

## Overview

This view returns a flexible preferred size to its own container view.

This container differs from [GeometryReader](geometryreader.md) in that it also reads available depth, and thus also returns a flexible preferred depth to its parent layout. Use the 3D version only in situations where you need to read depth, because it affects depth layout when used in a container like a [ZStack](zstack.md).

## Relationships

- **Conforms To**: [View](view.md)

## Topics

### Creating a geometry reader

- [init(content:)](<geometryreader3d/init(content_).md>)
- [content](geometryreader3d/content.md)

## See Also

### Measuring a view

- [GeometryReader](geometryreader.md) — A container view that defines its content as a function of its own size and coordinate space.
- [GeometryProxy](geometryproxy.md) — A proxy for access to the size and coordinate space (for anchor resolution) of the container view.
- [GeometryProxy3D](geometryproxy3d.md) — A proxy for access to the size and coordinate space of the container view.
- [coordinateSpace(_:)](<view/coordinatespace(__).md>) — Assigns a name to the view’s coordinate space, so other code can operate on dimensions like points and sizes relative to the named space.
- [CoordinateSpace](coordinatespace.md) — A resolved coordinate space created by the coordinate space protocol.
- [CoordinateSpaceProtocol](coordinatespaceprotocol.md) — A frame of reference within the layout system.
- [PhysicalMetric](physicalmetric.md) — Provides access to a value in points that corresponds to the specified physical measurement.
- [PhysicalMetricsConverter](physicalmetricsconverter.md) — A physical metrics converter provides conversion between point values and their extent in 3D space, in the form of physical length measurements.
