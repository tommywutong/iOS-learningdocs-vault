---
title: 'CGSizeMake(_:_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgsizemake(_:_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgsizemake(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgsizemake%28_%3A_%3A%29.json'
content_hash: 'sha256:c79e67cd02c6a08b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGSizeMake(_:_:)

<sub>Function</sub>

Returns a size with the specified dimension values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CGSizeMake(_ width: CGFloat, _ height: CGFloat) -> CGSize
```

## Parameters

- `width` — A width value.

- `height` — A height value.

## Return Value

Returns a [CGSize](../corefoundation/cgsize.md) structure with the specified width and height.

## See Also

### Creating a Geometric Primitive from Values

- [CGPointMake](<cgpointmake(____).md>) — Returns a point with the specified coordinates.
- [CGRectMake](<cgrectmake(________).md>) — Returns a rectangle with the specified coordinate and size values.
- [CGVectorMake](<cgvectormake(____).md>) — Returns a vector with the specified dimension values.
