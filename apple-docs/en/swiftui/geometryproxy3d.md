---
title: GeometryProxy3D
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/geometryproxy3d
source_url: 'https://developer.apple.com/documentation/swiftui/geometryproxy3d'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/geometryproxy3d.json'
content_hash: 'sha256:b181edd92cca9ec5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# GeometryProxy3D

<sub>Structure</sub>

A proxy for access to the size and coordinate space of the container view.

<sub>visionOS</sub>

```swift
struct GeometryProxy3D
```

## Overview

You can use a proxy for anchor resolution.

## Topics

### Accessing geometry characteristics

- [frame(in:)](<geometryproxy3d/frame(in_).md>) — The container view’s bounds rectangle converted to a defined coordinate space.
- [size](geometryproxy3d/size.md) — The size of the container view.
- [safeAreaInsets](geometryproxy3d/safeareainsets.md) — The safe area inset of the container view.
- [subscript(_:)](<geometryproxy3d/subscript(__).md>) — Resolves the value of an anchor to the container view.
- [transform(in:)](<geometryproxy3d/transform(in_).md>) — The container view’s 3D transform converted to a defined coordinate space.

### Instance Methods

- [coordinateSpace3D(for:)](<geometryproxy3d/coordinatespace3d(for_).md>) — Returns a value that can be used for `CoordinateSpace3D` based coordinate conversions.

## See Also

### Measuring a view

- [GeometryReader](geometryreader.md) — A container view that defines its content as a function of its own size and coordinate space.
- [GeometryReader3D](geometryreader3d.md) — A container view that defines its content as a function of its own size and coordinate space.
- [GeometryProxy](geometryproxy.md) — A proxy for access to the size and coordinate space (for anchor resolution) of the container view.
- [coordinateSpace(_:)](<view/coordinatespace(__).md>) — Assigns a name to the view’s coordinate space, so other code can operate on dimensions like points and sizes relative to the named space.
- [CoordinateSpace](coordinatespace.md) — A resolved coordinate space created by the coordinate space protocol.
- [CoordinateSpaceProtocol](coordinatespaceprotocol.md) — A frame of reference within the layout system.
- [PhysicalMetric](physicalmetric.md) — Provides access to a value in points that corresponds to the specified physical measurement.
- [PhysicalMetricsConverter](physicalmetricsconverter.md) — A physical metrics converter provides conversion between point values and their extent in 3D space, in the form of physical length measurements.
