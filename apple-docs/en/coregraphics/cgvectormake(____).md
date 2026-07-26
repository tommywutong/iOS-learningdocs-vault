---
title: 'CGVectorMake(_:_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgvectormake(_:_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgvectormake(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgvectormake%28_%3A_%3A%29.json'
content_hash: 'sha256:9a6104f99976c807'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGVectorMake(_:_:)

<sub>Function</sub>

Returns a vector with the specified dimension values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CGVectorMake(_ dx: CGFloat, _ dy: CGFloat) -> CGVector
```

## Parameters

- `dx` — The x-coordinate of the vector to construct.

- `dy` — The y-coordinate of the vector to construct.

## Return Value

Returns a [CGVector](../corefoundation/cgvector.md) structure with the specified coordinates.

## See Also

### Creating a Geometric Primitive from Values

- [CGPointMake](<cgpointmake(____).md>) — Returns a point with the specified coordinates.
- [CGRectMake](<cgrectmake(________).md>) — Returns a rectangle with the specified coordinate and size values.
- [CGSizeMake](<cgsizemake(____).md>) — Returns a size with the specified dimension values.
