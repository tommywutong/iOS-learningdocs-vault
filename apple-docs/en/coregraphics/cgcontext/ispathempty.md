---
title: isPathEmpty
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgcontext/ispathempty
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/ispathempty'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/ispathempty.json'
content_hash: 'sha256:1bef529341f5be09'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# isPathEmpty

<sub>Instance Property</sub>

Indicates whether the current path contains any subpaths.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isPathEmpty: Bool { get }
```

## See Also

### Examining the Current Graphics Path

- [CGContextGetPathBoundingBox](boundingboxofpath.md) — Returns the smallest rectangle that contains the current path.
- [CGContextGetPathCurrentPoint](currentpointofpath.md) — Returns the current point in a non-empty path.
- [CGContextPathContainsPoint](<pathcontains(__mode_).md>) — Checks to see whether the specified point is contained in the current path.
