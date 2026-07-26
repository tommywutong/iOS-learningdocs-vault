---
title: 'init(rect:transform:)'
framework: Core Graphics
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgpath/init(rect:transform:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpath/init(rect:transform:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpath/init%28rect%3Atransform%3A%29.json'
content_hash: 'sha256:0119fe0829102965'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGPath](../cgpath.md)

# init(rect:transform:)

<sub>Initializer</sub>

Create an immutable path of a rectangle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(rect: CGRect, transform: UnsafePointer<CGAffineTransform>?)
```

## Parameters

- `rect` — The rectangle to add.

- `transform` — A pointer to an affine transformation matrix, or `NULL` if no transformation is needed. If specified, Core Graphics applies the transformation to the rectangle before it is added to the path.

## Return Value

A new, immutable path. You are responsible for releasing this object.

## Discussion

This is a convenience function that creates a path of an rectangle. Using this convenience function is more efficient than creating a mutable path and adding an rectangle to it.

Calling this function is equivalent to using [CGRectGetMinX](<../cgrectgetminx(__).md>) and related functions to find the corners of the rectangle, then using the [CGPathMoveToPoint](../cgpathmovetopoint.md), [CGPathAddLineToPoint](../cgpathaddlinetopoint.md), and [CGPathCloseSubpath](<../cgmutablepath/closesubpath().md>) functions to draw the rectangle.

## See Also

### Creating Graphics Paths

- [CGPathCreateWithEllipseInRect](<init(ellipsein_transform_).md>) — Create an immutable path of an ellipse.
- [CGPathCreateWithRoundedRect](<init(roundedrect_cornerwidth_cornerheight_transform_).md>) — Create an immutable path of a rounded rectangle.
