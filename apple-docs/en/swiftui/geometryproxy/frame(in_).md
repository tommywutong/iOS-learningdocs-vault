---
title: 'frame(in:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/geometryproxy/frame(in:)'
source_url: 'https://developer.apple.com/documentation/swiftui/geometryproxy/frame(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/geometryproxy/frame%28in%3A%29.json'
content_hash: 'sha256:ad03f0be8127ea6f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GeometryProxy](../geometryproxy.md)

# frame(in:)

<sub>Instance Method</sub>

Returns the container view’s bounds rectangle, converted to a defined coordinate space.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func frame(in coordinateSpace: some CoordinateSpaceProtocol) -> CGRect
```

## See Also

### Accessing geometry characteristics

- [bounds(of:)](<bounds(of_).md>) — Returns the given coordinate space’s bounds rectangle, converted to the local coordinate space.
- [concentricCornerRadii](concentriccornerradii.md) — The concentric corner radii for this view’s bounds relative to the container shape. _(beta)_
- [concentricCornerRadii(in:)](<concentriccornerradii(in_).md>) — Returns the concentric corner radii for the specified frame relative to the container shape. _(beta)_
- [containerCornerInsets](containercornerinsets.md) — Returns the corner insets of the container view. Use this value to adjust the geometry of a view based on the overlapping corner insets of the container view. Corner insets may include pieces of system UI as well as the corner radii for windows and presentations.
- [size](size.md) — The size of the container view.
- [safeAreaInsets](safeareainsets.md) — The safe area inset of the container view.
- [subscript(_:)](<subscript(__).md>) — Resolves the value of an anchor to the container view.
- [transform(in:)](<transform(in_).md>) — The container view’s 3D transform converted to a defined coordinate space.
