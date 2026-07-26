---
title: CGPathEqualToPath
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpathequaltopath
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpathequaltopath'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpathequaltopath.json'
content_hash: 'sha256:176909064899276d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPathEqualToPath

<sub>Function</sub>

Indicates whether two graphics paths are equivalent.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern bool CGPathEqualToPath(CGPathRef path1, CGPathRef path2);
```

## Parameters

- `path1` — The first path being compared.

- `path2` — The second path being compared.

## Return Value

A Boolean value that indicates whether or not the two specified paths contain the same sequence of path elements. If the paths are not the same, returns [false](../swift/false.md).

## See Also

### Examining a Graphics Path

- [CGPathGetBoundingBox](cgpath/boundingbox.md) — Returns the bounding box containing all points in a graphics path.
- [CGPathGetPathBoundingBox](cgpath/boundingboxofpath.md) — Returns the bounding box of a graphics path.
- [CGPathGetCurrentPoint](cgpath/currentpoint.md) — Returns the current point in a graphics path.
- [CGPathContainsPoint](cgpathcontainspoint.md) — Checks whether a point is contained in a graphics path.
- [CGPathIsEmpty](cgpath/isempty.md) — Indicates whether or not a graphics path is empty.
- [CGPathIsRect](<cgpath/isrect(__).md>) — Indicates whether or not a graphics path represents a rectangle.
