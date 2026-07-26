---
title: currentPoint
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpath/currentpoint
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpath/currentpoint'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpath/currentpoint.json'
content_hash: 'sha256:1e0975926bad4407'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGPath](../cgpath.md)

# currentPoint

<sub>Instance Property</sub>

Returns the current point in a graphics path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var currentPoint: CGPoint { get }
```

## Discussion

If the path is empty—that is, if it has no elements—this function returns [CGPointZero](../cgpointzero.md) (see [CGGeometry](../cggeometry.md)). To determine whether a path is empty, use [CGPathIsEmpty](isempty.md).

## See Also

### Examining a Graphics Path

- [CGPathGetBoundingBox](boundingbox.md) — Returns the bounding box containing all points in a graphics path.
- [CGPathGetPathBoundingBox](boundingboxofpath.md) — Returns the bounding box of a graphics path.
- [contains(_:using:transform:)](<contains(__using_transform_).md>) — Returns whether the specified point is interior to the path.
- [CGPathIsEmpty](isempty.md) — Indicates whether or not a graphics path is empty.
- [CGPathIsRect](<isrect(__).md>) — Indicates whether or not a graphics path represents a rectangle.
