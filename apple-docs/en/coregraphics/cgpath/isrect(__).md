---
title: 'isRect(_:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgpath/isrect(_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpath/isrect(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpath/isrect%28_%3A%29.json'
content_hash: 'sha256:012e2651f8456a80'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGPath](../cgpath.md)

# isRect(_:)

<sub>Instance Method</sub>

Indicates whether or not a graphics path represents a rectangle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isRect(_ rect: UnsafeMutablePointer<CGRect>?) -> Bool
```

## Parameters

- `rect` — On input, a pointer to an uninitialized rectangle. If the specified path represents a rectangle, on return contains a copy of the rectangle.

## Return Value

A Boolean value that indicates whether the specified path represents a rectangle. If the path represents a rectangle, returns [true](../../swift/true.md).

## See Also

### Examining a Graphics Path

- [CGPathGetBoundingBox](boundingbox.md) — Returns the bounding box containing all points in a graphics path.
- [CGPathGetPathBoundingBox](boundingboxofpath.md) — Returns the bounding box of a graphics path.
- [CGPathGetCurrentPoint](currentpoint.md) — Returns the current point in a graphics path.
- [contains(_:using:transform:)](<contains(__using_transform_).md>) — Returns whether the specified point is interior to the path.
- [CGPathIsEmpty](isempty.md) — Indicates whether or not a graphics path is empty.
