---
title: 'coordinateSpace3D(for:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/geometryproxy3d/coordinatespace3d(for:)'
source_url: 'https://developer.apple.com/documentation/swiftui/geometryproxy3d/coordinatespace3d(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/geometryproxy3d/coordinatespace3d%28for%3A%29.json'
content_hash: 'sha256:8e5cb3be495b5a20'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GeometryProxy3D](../geometryproxy3d.md)

# coordinateSpace3D(for:)

<sub>Instance Method</sub>

Returns a value that can be used for `CoordinateSpace3D` based coordinate conversions.

<sub>visionOS</sub>

```swift
func coordinateSpace3D(for space: any CoordinateSpaceProtocol = LocalCoordinateSpace()) -> GeometryProxyCoordinateSpace3D
```

## Parameters

- `space` — The SwiftUI coordinate space to represent.
