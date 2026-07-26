---
title: concentricCornerRadii
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftui/geometryproxy/concentriccornerradii
source_url: 'https://developer.apple.com/documentation/swiftui/geometryproxy/concentriccornerradii'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/geometryproxy/concentriccornerradii.json'
content_hash: 'sha256:cc66952ed3d0e60a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GeometryProxy](../geometryproxy.md)

# concentricCornerRadii

<sub>Instance Property</sub>

The concentric corner radii for this view’s bounds relative to the container shape.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var concentricCornerRadii: RectangleCornerRadii? { get }
```

## Return Value

The resolved corner radii, or `nil` if no container shape is set or the shape does not provide sufficient corner info.

## Discussion

Concentric corners share the same center point as the container’s corners, creating visually harmonious nested rounded rectangles. The radius for each corner is calculated as the container’s corner radius minus the distance from this view’s corner to the container’s corner.

Unlike [ConcentricRectangle](../concentricrectangle.md), which calculates and draws the shape, this property only returns the calculated radii. This allows you to use the values for custom drawing, animations, or other purposes:

```swift
GeometryReader { geometry in
    Canvas { context, size in
        if let radii = geometry.concentricCornerRadii {
            let path = Path(
                roundedRect: CGRect(origin: .zero, size: size),
                cornerRadii: radii
            )
            context.fill(path, with: .color(.blue))
        }
    }
}
.containerShape(.rect(cornerRadius: 48))
```

Each corner’s radius depends on its position relative to the container:

- Corners aligned with the container’s corners get concentric radii
- Corners far from the container’s corners get zero radii
- The radius is clamped to the view’s maximum possible radius

> [!info] See Also
> [ConcentricRectangle](../concentricrectangle.md)

## See Also

### Accessing geometry characteristics

- [bounds(of:)](<bounds(of_).md>) — Returns the given coordinate space’s bounds rectangle, converted to the local coordinate space.
- [concentricCornerRadii(in:)](<concentriccornerradii(in_).md>) — Returns the concentric corner radii for the specified frame relative to the container shape. _(beta)_
- [containerCornerInsets](containercornerinsets.md) — Returns the corner insets of the container view. Use this value to adjust the geometry of a view based on the overlapping corner insets of the container view. Corner insets may include pieces of system UI as well as the corner radii for windows and presentations.
- [frame(in:)](<frame(in_).md>) — Returns the container view’s bounds rectangle, converted to a defined coordinate space.
- [size](size.md) — The size of the container view.
- [safeAreaInsets](safeareainsets.md) — The safe area inset of the container view.
- [subscript(_:)](<subscript(__).md>) — Resolves the value of an anchor to the container view.
- [transform(in:)](<transform(in_).md>) — The container view’s 3D transform converted to a defined coordinate space.
