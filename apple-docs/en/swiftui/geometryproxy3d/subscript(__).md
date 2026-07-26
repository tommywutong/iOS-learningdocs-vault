---
title: 'subscript(_:)'
framework: SwiftUI
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/geometryproxy3d/subscript(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/geometryproxy3d/subscript(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/geometryproxy3d/subscript%28_%3A%29.json'
content_hash: 'sha256:d49cc42e416e9f5d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GeometryProxy3D](../geometryproxy3d.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Resolves the value of an anchor to the container view.

<sub>visionOS</sub>

```swift
subscript<T>(anchor: Anchor<T>) -> T { get }
```

## See Also

### Accessing geometry characteristics

- [frame(in:)](<frame(in_).md>) — The container view’s bounds rectangle converted to a defined coordinate space.
- [size](size.md) — The size of the container view.
- [safeAreaInsets](safeareainsets.md) — The safe area inset of the container view.
- [transform(in:)](<transform(in_).md>) — The container view’s 3D transform converted to a defined coordinate space.
