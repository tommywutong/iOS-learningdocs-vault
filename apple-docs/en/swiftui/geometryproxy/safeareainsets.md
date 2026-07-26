---
title: safeAreaInsets
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/geometryproxy/safeareainsets
source_url: 'https://developer.apple.com/documentation/swiftui/geometryproxy/safeareainsets'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/geometryproxy/safeareainsets.json'
content_hash: 'sha256:d2d4508b5e4a82e7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GeometryProxy](../geometryproxy.md)

# safeAreaInsets

<sub>Instance Property</sub>

The safe area inset of the container view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var safeAreaInsets: EdgeInsets { get }
```

## See Also

### Accessing geometry characteristics

- [bounds(of:)](<bounds(of_).md>) — Returns the given coordinate space’s bounds rectangle, converted to the local coordinate space.
- [concentricCornerRadii](concentriccornerradii.md) — The concentric corner radii for this view’s bounds relative to the container shape. _(beta)_
- [concentricCornerRadii(in:)](<concentriccornerradii(in_).md>) — Returns the concentric corner radii for the specified frame relative to the container shape. _(beta)_
- [containerCornerInsets](containercornerinsets.md) — Returns the corner insets of the container view. Use this value to adjust the geometry of a view based on the overlapping corner insets of the container view. Corner insets may include pieces of system UI as well as the corner radii for windows and presentations.
- [frame(in:)](<frame(in_).md>) — Returns the container view’s bounds rectangle, converted to a defined coordinate space.
- [size](size.md) — The size of the container view.
- [subscript(_:)](<subscript(__).md>) — Resolves the value of an anchor to the container view.
- [transform(in:)](<transform(in_).md>) — The container view’s 3D transform converted to a defined coordinate space.
