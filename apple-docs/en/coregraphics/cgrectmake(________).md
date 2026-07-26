---
title: 'CGRectMake(_:_:_:_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgrectmake(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgrectmake(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgrectmake%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:21eee8c5523c5075'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGRectMake(_:_:_:_:)

<sub>Function</sub>

Returns a rectangle with the specified coordinate and size values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CGRectMake(_ x: CGFloat, _ y: CGFloat, _ width: CGFloat, _ height: CGFloat) -> CGRect
```

## Parameters

- `x` — The x-coordinate of the rectangle’s origin point.

- `y` — The y-coordinate of the rectangle’s origin point.

- `width` — The width of the rectangle.

- `height` — The height of the rectangle.

## Return Value

A rectangle with the specified location and dimensions.

## See Also

### Creating a Geometric Primitive from Values

- [CGPointMake](<cgpointmake(____).md>) — Returns a point with the specified coordinates.
- [CGSizeMake](<cgsizemake(____).md>) — Returns a size with the specified dimension values.
- [CGVectorMake](<cgvectormake(____).md>) — Returns a vector with the specified dimension values.
