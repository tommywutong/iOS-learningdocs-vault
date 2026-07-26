---
title: CGPathContainsPoint
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpathcontainspoint
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpathcontainspoint'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpathcontainspoint.json'
content_hash: 'sha256:42655e3ab65e336c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPathContainsPoint

<sub>Function</sub>

Checks whether a point is contained in a graphics path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern bool CGPathContainsPoint(CGPathRef path, const CGAffineTransform *m, CGPoint point, bool eoFill);
```

## Parameters

- `path` — The path to evaluate the point against.

- `m` — An affine transform. If `m` is not `NULL` then the point is transformed by this affine transform prior to determining whether the path contains the point.

- `point` — The point to check.

- `eoFill` — A Boolean value that, if [true](../swift/true.md), specifies to use the even-odd fill rule to evaluate the painted region of the path. If [false](../swift/false.md), the winding fill rule is used.

## Return Value

Returns [true](../swift/true.md) if the point is contained in the path; [false](../swift/false.md) otherwise.

## Discussion

A point is contained in a path if it would be inside the painted region when the path is filled.

## See Also

### Examining a Graphics Path

- [CGPathEqualToPath](cgpathequaltopath.md) — Indicates whether two graphics paths are equivalent.
- [CGPathGetBoundingBox](cgpath/boundingbox.md) — Returns the bounding box containing all points in a graphics path.
- [CGPathGetPathBoundingBox](cgpath/boundingboxofpath.md) — Returns the bounding box of a graphics path.
- [CGPathGetCurrentPoint](cgpath/currentpoint.md) — Returns the current point in a graphics path.
- [CGPathIsEmpty](cgpath/isempty.md) — Indicates whether or not a graphics path is empty.
- [CGPathIsRect](<cgpath/isrect(__).md>) — Indicates whether or not a graphics path represents a rectangle.
