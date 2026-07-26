---
title: boundingBox
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpath/boundingbox
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpath/boundingbox'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpath/boundingbox.json'
content_hash: 'sha256:c92e3502b175aba3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGPath](../cgpath.md)

# boundingBox

<sub>Instance Property</sub>

Returns the bounding box containing all points in a graphics path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var boundingBox: CGRect { get }
```

## Discussion

The bounding box is the smallest rectangle completely enclosing all points in the path, including control points for Bézier and quadratic curves. If the path is empty, this value is [CGRectNull](../cgrectnull.md).

## See Also

### Examining a Graphics Path

- [CGPathGetPathBoundingBox](boundingboxofpath.md) — Returns the bounding box of a graphics path.
- [CGPathGetCurrentPoint](currentpoint.md) — Returns the current point in a graphics path.
- [contains(_:using:transform:)](<contains(__using_transform_).md>) — Returns whether the specified point is interior to the path.
- [CGPathIsEmpty](isempty.md) — Indicates whether or not a graphics path is empty.
- [CGPathIsRect](<isrect(__).md>) — Indicates whether or not a graphics path represents a rectangle.
