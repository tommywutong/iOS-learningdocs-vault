---
title: boundingBoxOfPath
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpath/boundingboxofpath
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpath/boundingboxofpath'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpath/boundingboxofpath.json'
content_hash: 'sha256:0d24a16f9bd16df8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGPath](../cgpath.md)

# boundingBoxOfPath

<sub>Instance Property</sub>

Returns the bounding box of a graphics path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var boundingBoxOfPath: CGRect { get }
```

## Discussion

The path bounding box is the smallest rectangle completely enclosing all points in the path but not including control points for Bézier and quadratic curves. If the path is empty, this value is [CGRectNull](../cgrectnull.md).

## See Also

### Examining a Graphics Path

- [CGPathGetBoundingBox](boundingbox.md) — Returns the bounding box containing all points in a graphics path.
- [CGPathGetCurrentPoint](currentpoint.md) — Returns the current point in a graphics path.
- [contains(_:using:transform:)](<contains(__using_transform_).md>) — Returns whether the specified point is interior to the path.
- [CGPathIsEmpty](isempty.md) — Indicates whether or not a graphics path is empty.
- [CGPathIsRect](<isrect(__).md>) — Indicates whether or not a graphics path represents a rectangle.
