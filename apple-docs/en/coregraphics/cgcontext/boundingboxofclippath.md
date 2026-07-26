---
title: boundingBoxOfClipPath
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.3+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgcontext/boundingboxofclippath
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/boundingboxofclippath'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/boundingboxofclippath.json'
content_hash: 'sha256:35dafb564d44359e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# boundingBoxOfClipPath

<sub>Instance Property</sub>

Returns the bounding box of a clipping path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var boundingBoxOfClipPath: CGRect { get }
```

## Discussion

The bounding box is the smallest rectangle completely enclosing all points in the clipping path, including control points for any Bezier curves in the path.

## See Also

### Working with the Current Clipping Path

- [clip(using:)](<clip(using_).md>) — Modifies the current clipping path.
- [CGContextClipToRect](<clip(to_)-7cbwq.md>) — Sets the clipping path to the intersection of the current clipping path with the area defined by the specified rectangle.
- [clip(to:)](<clip(to_)-2eg0.md>) — Sets the clipping path to the intersection of the current clipping path with the region defined by an array of rectangles.
- [CGContextClipToMask](<clip(to_mask_).md>) — Maps a mask into the specified rectangle and intersects it with the current clipping area of the graphics context.
