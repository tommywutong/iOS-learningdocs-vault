---
title: 'CGRectGetMidX(_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgrectgetmidx(_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgrectgetmidx(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgrectgetmidx%28_%3A%29.json'
content_hash: 'sha256:d0765f2a5b861be1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGRectGetMidX(_:)

<sub>Function</sub>

Returns the x- coordinate that establishes the center of a rectangle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CGRectGetMidX(_ rect: CGRect) -> CGFloat
```

## Parameters

- `rect` — The rectangle to examine.

## Return Value

The x-coordinate of the center of the specified rectangle.

## See Also

### Getting Min, Mid, and Max Values

- [CGRectGetMinX](<cgrectgetminx(__).md>) — Returns the smallest value for the x-coordinate of the rectangle.
- [CGRectGetMinY](<cgrectgetminy(__).md>) — Returns the smallest value for the y-coordinate of the rectangle.
- [CGRectGetMidY](<cgrectgetmidy(__).md>) — Returns the y-coordinate that establishes the center of the rectangle.
- [CGRectGetMaxX](<cgrectgetmaxx(__).md>) — Returns the largest value of the x-coordinate for the rectangle.
- [CGRectGetMaxY](<cgrectgetmaxy(__).md>) — Returns the largest value for the y-coordinate of the rectangle.
