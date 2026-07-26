---
title: isEmpty
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpath/isempty
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpath/isempty'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpath/isempty.json'
content_hash: 'sha256:4bf532cae47f409e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGPath](../cgpath.md)

# isEmpty

<sub>Instance Property</sub>

Indicates whether or not a graphics path is empty.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isEmpty: Bool { get }
```

## Discussion

An empty path contains no elements.

## See Also

### Examining a Graphics Path

- [CGPathGetBoundingBox](boundingbox.md) — Returns the bounding box containing all points in a graphics path.
- [CGPathGetPathBoundingBox](boundingboxofpath.md) — Returns the bounding box of a graphics path.
- [CGPathGetCurrentPoint](currentpoint.md) — Returns the current point in a graphics path.
- [contains(_:using:transform:)](<contains(__using_transform_).md>) — Returns whether the specified point is interior to the path.
- [CGPathIsRect](<isrect(__).md>) — Indicates whether or not a graphics path represents a rectangle.
