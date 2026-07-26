---
title: 'CGRectGetWidth(_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgrectgetwidth(_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgrectgetwidth(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgrectgetwidth%28_%3A%29.json'
content_hash: 'sha256:78c5edb2280dc0a8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGRectGetWidth(_:)

<sub>Function</sub>

Returns the width of a rectangle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CGRectGetWidth(_ rect: CGRect) -> CGFloat
```

## Parameters

- `rect` — The rectangle to examine.

## Return Value

The width of the specified rectangle.

## Discussion

Regardless of whether the width is stored in the [CGRect](../corefoundation/cgrect.md) data structure as a positive or negative number, this function returns the width as if the rectangle were standardized.  That is, the result is never a negative number.

## See Also

### Getting Height and Width

- [CGRectGetHeight](<cgrectgetheight(__).md>) — Returns the height of a rectangle.
