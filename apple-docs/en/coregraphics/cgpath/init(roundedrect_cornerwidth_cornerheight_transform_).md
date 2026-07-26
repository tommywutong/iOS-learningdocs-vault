---
title: 'init(roundedRect:cornerWidth:cornerHeight:transform:)'
framework: Core Graphics
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgpath/init(roundedrect:cornerwidth:cornerheight:transform:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpath/init(roundedrect:cornerwidth:cornerheight:transform:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpath/init%28roundedrect%3Acornerwidth%3Acornerheight%3Atransform%3A%29.json'
content_hash: 'sha256:215106aabcfbffd8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGPath](../cgpath.md)

# init(roundedRect:cornerWidth:cornerHeight:transform:)

<sub>Initializer</sub>

Create an immutable path of a rounded rectangle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(roundedRect rect: CGRect, cornerWidth: CGFloat, cornerHeight: CGFloat, transform: UnsafePointer<CGAffineTransform>?)
```

## Parameters

- `rect` — The rectangle to add.

- `cornerWidth` — The width of the rounded corner sections.

- `cornerHeight` — The height of the rounded corner sections.

- `transform` — A pointer to an affine transformation matrix, or `NULL` if no transformation is needed. If specified, Core Graphics applies the transformation to the rectangle before it is added to the path.

## Return Value

A new, immutable path. You are responsible for releasing this object.

## Discussion

This is a convenience function that creates a path of an rounded rectangle. Using this convenience function is more efficient than creating a mutable path and adding an rectangle to it.

Each corner of the rounded rectangle is one-quarter of an ellipse with axes equal to the `cornerWidth` and `cornerHeight` parameters. The rounded rectangle forms a complete subpath and is oriented in the clockwise direction.

## See Also

### Creating Graphics Paths

- [CGPathCreateWithRect](<init(rect_transform_).md>) — Create an immutable path of a rectangle.
- [CGPathCreateWithEllipseInRect](<init(ellipsein_transform_).md>) — Create an immutable path of an ellipse.
