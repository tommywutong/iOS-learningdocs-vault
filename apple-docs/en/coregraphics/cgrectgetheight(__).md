---
title: 'CGRectGetHeight(_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgrectgetheight(_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgrectgetheight(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgrectgetheight%28_%3A%29.json'
content_hash: 'sha256:144811408648dc1e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGRectGetHeight(_:)

<sub>Function</sub>

Returns the height of a rectangle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CGRectGetHeight(_ rect: CGRect) -> CGFloat
```

## Parameters

- `rect` — The rectangle to examine.

## Return Value

The height of the specified rectangle.

## Discussion

Regardless of whether the height is stored in the [CGRect](../corefoundation/cgrect.md) data structure as a positive or negative number, this function returns the height as if the rectangle were standardized. That is, the result is never a negative number.

## See Also

### Getting Height and Width

- [CGRectGetWidth](<cgrectgetwidth(__).md>) — Returns the width of a rectangle.
