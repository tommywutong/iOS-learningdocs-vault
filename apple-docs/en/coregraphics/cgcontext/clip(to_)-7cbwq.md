---
title: 'clip(to:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgcontext/clip(to:)-7cbwq'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/clip(to:)-7cbwq'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/clip%28to%3A%29-7cbwq.json'
content_hash: 'sha256:f32a3e0e295aba4e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# clip(to:)

<sub>Instance Method</sub>

Sets the clipping path to the intersection of the current clipping path with the area defined by the specified rectangle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func clip(to rect: CGRect)
```

## Parameters

- `rect` — The location and dimensions of the rectangle, in user space, to be used in determining the new clipping path.

## Discussion

This function sets the specified graphics context’s clipping region to the area which intersects both the current clipping path and the specified rectangle.

After determining the new clipping path, the function resets the context’s current path to an empty path.

## See Also

### Working with the Current Clipping Path

- [clip(using:)](<clip(using_).md>) — Modifies the current clipping path.
- [clip(to:)](<clip(to_)-2eg0.md>) — Sets the clipping path to the intersection of the current clipping path with the region defined by an array of rectangles.
- [CGContextClipToMask](<clip(to_mask_).md>) — Maps a mask into the specified rectangle and intersects it with the current clipping area of the graphics context.
- [CGContextGetClipBoundingBox](boundingboxofclippath.md) — Returns the bounding box of a clipping path.
