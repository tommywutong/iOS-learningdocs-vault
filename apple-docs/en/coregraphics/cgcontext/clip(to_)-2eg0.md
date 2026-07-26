---
title: 'clip(to:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 7.0+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgcontext/clip(to:)-2eg0'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/clip(to:)-2eg0'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/clip%28to%3A%29-2eg0.json'
content_hash: 'sha256:e832dfcd37c72865'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# clip(to:)

<sub>Instance Method</sub>

Sets the clipping path to the intersection of the current clipping path with the region defined by an array of rectangles.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func clip(to rects: [CGRect])
```

## Parameters

- `rects` — An array of rectangles, in user space coordinates.

## Discussion

This method sets the clipping path to the intersection of the current clipping path and the region within the specified rectangles.

After determining the new clipping path, the function resets the context’s current path to an empty path.

## See Also

### Working with the Current Clipping Path

- [clip(using:)](<clip(using_).md>) — Modifies the current clipping path.
- [CGContextClipToRect](<clip(to_)-7cbwq.md>) — Sets the clipping path to the intersection of the current clipping path with the area defined by the specified rectangle.
- [CGContextClipToMask](<clip(to_mask_).md>) — Maps a mask into the specified rectangle and intersects it with the current clipping area of the graphics context.
- [CGContextGetClipBoundingBox](boundingboxofclippath.md) — Returns the bounding box of a clipping path.
