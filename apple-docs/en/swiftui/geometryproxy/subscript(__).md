---
title: 'subscript(_:)'
framework: SwiftUI
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/geometryproxy/subscript(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/geometryproxy/subscript(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/geometryproxy/subscript%28_%3A%29.json'
content_hash: 'sha256:bafee6bc9b5bd4ad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GeometryProxy](../geometryproxy.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Resolves the value of an anchor to the container view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript<T>(anchor: Anchor<T>) -> T { get }
```

## See Also

### Accessing geometry characteristics

- [bounds(of:)](<bounds(of_).md>) — Returns the given coordinate space’s bounds rectangle, converted to the local coordinate space.
- [concentricCornerRadii](concentriccornerradii.md) — The concentric corner radii for this view’s bounds relative to the container shape. _(beta)_
- [concentricCornerRadii(in:)](<concentriccornerradii(in_).md>) — Returns the concentric corner radii for the specified frame relative to the container shape. _(beta)_
- [containerCornerInsets](containercornerinsets.md) — Returns the corner insets of the container view. Use this value to adjust the geometry of a view based on the overlapping corner insets of the container view. Corner insets may include pieces of system UI as well as the corner radii for windows and presentations.
- [frame(in:)](<frame(in_).md>) — Returns the container view’s bounds rectangle, converted to a defined coordinate space.
- [size](size.md) — The size of the container view.
- [safeAreaInsets](safeareainsets.md) — The safe area inset of the container view.
- [transform(in:)](<transform(in_).md>) — The container view’s 3D transform converted to a defined coordinate space.
