---
title: boundingBoxOfPath
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgcontext/boundingboxofpath
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/boundingboxofpath'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/boundingboxofpath.json'
content_hash: 'sha256:54687ab92173f34c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# boundingBoxOfPath

<sub>Instance Property</sub>

Returns the smallest rectangle that contains the current path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var boundingBoxOfPath: CGRect { get }
```

## Discussion

The bounding box is the smallest rectangle completely enclosing all points in a path, including control points for Bézier cubic and quadratic curves.

## See Also

### Examining the Current Graphics Path

- [CGContextGetPathCurrentPoint](currentpointofpath.md) — Returns the current point in a non-empty path.
- [CGContextIsPathEmpty](ispathempty.md) — Indicates whether the current path contains any subpaths.
- [CGContextPathContainsPoint](<pathcontains(__mode_).md>) — Checks to see whether the specified point is contained in the current path.
