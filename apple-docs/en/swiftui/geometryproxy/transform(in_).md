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
doc_path: '/documentation/swiftui/geometryproxy/transform(in:)'
source_url: 'https://developer.apple.com/documentation/swiftui/geometryproxy/transform(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/geometryproxy/transform%28in%3A%29.json'
content_hash: 'sha256:bb4c8af5caa6de13'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GeometryProxy](../geometryproxy.md)

# transform(in:)

<sub>Instance Method</sub>

The container view’s 3D transform converted to a defined coordinate space.

<sub>visionOS</sub>

```swift
func transform(in coordinateSpace: some CoordinateSpaceProtocol) -> AffineTransform3D?
```

## Discussion

If the view doesn’t have a well defined transform, such as if it is affected by a projection transform, this function may return `nil`.

## See Also

### Accessing geometry characteristics

- [bounds(of:)](<bounds(of_).md>) — Returns the given coordinate space’s bounds rectangle, converted to the local coordinate space.
- [concentricCornerRadii](concentriccornerradii.md) — The concentric corner radii for this view’s bounds relative to the container shape. _(beta)_
- [concentricCornerRadii(in:)](<concentriccornerradii(in_).md>) — Returns the concentric corner radii for the specified frame relative to the container shape. _(beta)_
- [containerCornerInsets](containercornerinsets.md) — Returns the corner insets of the container view. Use this value to adjust the geometry of a view based on the overlapping corner insets of the container view. Corner insets may include pieces of system UI as well as the corner radii for windows and presentations.
- [frame(in:)](<frame(in_).md>) — Returns the container view’s bounds rectangle, converted to a defined coordinate space.
- [size](size.md) — The size of the container view.
- [safeAreaInsets](safeareainsets.md) — The safe area inset of the container view.
- [subscript(_:)](<subscript(__).md>) — Resolves the value of an anchor to the container view.
