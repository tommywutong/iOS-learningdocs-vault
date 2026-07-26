---
title: 'transform(in:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/geometryproxy3d/transform(in:)'
source_url: 'https://developer.apple.com/documentation/swiftui/geometryproxy3d/transform(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/geometryproxy3d/transform%28in%3A%29.json'
content_hash: 'sha256:5c64953e59137f52'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GeometryProxy3D](../geometryproxy3d.md)

# transform(in:)

<sub>Instance Method</sub>

The container view’s 3D transform converted to a defined coordinate space.

<sub>visionOS</sub>

```swift
func transform(in coordinateSpace: some CoordinateSpaceProtocol) -> AffineTransform3D?
```

## Discussion

If the view doesn’t have a well-defined transform, such as if it’s affected by a projection transform, this function may return `nil`.

## See Also

### Accessing geometry characteristics

- [frame(in:)](<frame(in_).md>) — The container view’s bounds rectangle converted to a defined coordinate space.
- [size](size.md) — The size of the container view.
- [safeAreaInsets](safeareainsets.md) — The safe area inset of the container view.
- [subscript(_:)](<subscript(__).md>) — Resolves the value of an anchor to the container view.
