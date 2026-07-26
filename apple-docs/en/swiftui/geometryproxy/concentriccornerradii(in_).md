---
title: 'concentricCornerRadii(in:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftui/geometryproxy/concentriccornerradii(in:)'
source_url: 'https://developer.apple.com/documentation/swiftui/geometryproxy/concentriccornerradii(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/geometryproxy/concentriccornerradii%28in%3A%29.json'
content_hash: 'sha256:35645d2530bfdbde'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GeometryProxy](../geometryproxy.md)

# concentricCornerRadii(in:)

<sub>Instance Method</sub>

Returns the concentric corner radii for the specified frame relative to the container shape.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func concentricCornerRadii(in frame: CGRect) -> RectangleCornerRadii?
```

## Parameters

- `frame` — The frame in the view’s local coordinate space for which to calculate the concentric corner radii.

## Return Value

The resolved corner radii, or `nil` if no container shape is set or the shape does not provide sufficient corner info.

## Discussion

Concentric corners share the same center point as the container’s corners. The radius for each corner is calculated as the container’s corner radius minus the distance from the frame’s corner to the container’s corner.

Unlike [ConcentricRectangle](../concentricrectangle.md), which calculates and draws the shape, this function only returns the calculated radii. Use this when you need corner radii for a subregion of the view, or when you want to use the values for custom drawing, animations, or other purposes:

```swift
GeometryReader { geometry in
    Canvas { context, size in
        let rect = CGRect(x: 10, y: 10, width: 80, height: 80)
        if let radii = geometry.concentricCornerRadii(in: rect) {
            let path = Path(roundedRect: rect, cornerRadii: radii)
            context.fill(path, with: .color(.blue))
        }
    }
}
.containerShape(.rect(cornerRadius: 48))
```

> [!info] See Also
> [ConcentricRectangle](../concentricrectangle.md)

## See Also

### Accessing geometry characteristics

- [bounds(of:)](<bounds(of_).md>) — Returns the given coordinate space’s bounds rectangle, converted to the local coordinate space.
- [concentricCornerRadii](concentriccornerradii.md) — The concentric corner radii for this view’s bounds relative to the container shape. _(beta)_
- [containerCornerInsets](containercornerinsets.md) — Returns the corner insets of the container view. Use this value to adjust the geometry of a view based on the overlapping corner insets of the container view. Corner insets may include pieces of system UI as well as the corner radii for windows and presentations.
- [frame(in:)](<frame(in_).md>) — Returns the container view’s bounds rectangle, converted to a defined coordinate space.
- [size](size.md) — The size of the container view.
- [safeAreaInsets](safeareainsets.md) — The safe area inset of the container view.
- [subscript(_:)](<subscript(__).md>) — Resolves the value of an anchor to the container view.
- [transform(in:)](<transform(in_).md>) — The container view’s 3D transform converted to a defined coordinate space.
