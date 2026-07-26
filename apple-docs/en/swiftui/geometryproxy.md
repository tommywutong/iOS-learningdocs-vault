---
title: GeometryProxy
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/geometryproxy
source_url: 'https://developer.apple.com/documentation/swiftui/geometryproxy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/geometryproxy.json'
content_hash: 'sha256:023abf64a95ffd9b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# GeometryProxy

<sub>Structure</sub>

A proxy for access to the size and coordinate space (for anchor resolution) of the container view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct GeometryProxy
```

## Topics

### Accessing geometry characteristics

- [bounds(of:)](<geometryproxy/bounds(of_).md>) — Returns the given coordinate space’s bounds rectangle, converted to the local coordinate space.
- [concentricCornerRadii](geometryproxy/concentriccornerradii.md) — The concentric corner radii for this view’s bounds relative to the container shape. _(beta)_
- [concentricCornerRadii(in:)](<geometryproxy/concentriccornerradii(in_).md>) — Returns the concentric corner radii for the specified frame relative to the container shape. _(beta)_
- [containerCornerInsets](geometryproxy/containercornerinsets.md) — Returns the corner insets of the container view. Use this value to adjust the geometry of a view based on the overlapping corner insets of the container view. Corner insets may include pieces of system UI as well as the corner radii for windows and presentations.
- [frame(in:)](<geometryproxy/frame(in_).md>) — Returns the container view’s bounds rectangle, converted to a defined coordinate space.
- [size](geometryproxy/size.md) — The size of the container view.
- [safeAreaInsets](geometryproxy/safeareainsets.md) — The safe area inset of the container view.
- [subscript(_:)](<geometryproxy/subscript(__).md>) — Resolves the value of an anchor to the container view.
- [transform(in:)](<geometryproxy/transform(in_).md>) — The container view’s 3D transform converted to a defined coordinate space.

## See Also

### Measuring a view

- [GeometryReader](geometryreader.md) — A container view that defines its content as a function of its own size and coordinate space.
- [GeometryReader3D](geometryreader3d.md) — A container view that defines its content as a function of its own size and coordinate space.
- [GeometryProxy3D](geometryproxy3d.md) — A proxy for access to the size and coordinate space of the container view.
- [coordinateSpace(_:)](<view/coordinatespace(__).md>) — Assigns a name to the view’s coordinate space, so other code can operate on dimensions like points and sizes relative to the named space.
- [CoordinateSpace](coordinatespace.md) — A resolved coordinate space created by the coordinate space protocol.
- [CoordinateSpaceProtocol](coordinatespaceprotocol.md) — A frame of reference within the layout system.
- [PhysicalMetric](physicalmetric.md) — Provides access to a value in points that corresponds to the specified physical measurement.
- [PhysicalMetricsConverter](physicalmetricsconverter.md) — A physical metrics converter provides conversion between point values and their extent in 3D space, in the form of physical length measurements.
