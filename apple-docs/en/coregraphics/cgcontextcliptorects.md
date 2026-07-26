---
title: CGContextClipToRects
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgcontextcliptorects
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontextcliptorects'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontextcliptorects.json'
content_hash: 'sha256:958a1c01a1b747af'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGContextClipToRects

<sub>Function</sub>

Sets the clipping path to the intersection of the current clipping path with the region defined by an array of rectangles.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void CGContextClipToRects(CGContextRef c, const CGRect *rects, size_t count);
```

## Parameters

- `c` — The graphics context for which to set the clipping path.

- `rects` — An array of rectangles. The locations and dimensions of the rectangles are specified in the user space coordinate system.

- `count` — The total number of array entries in the `rects` parameter.

## Discussion

This function sets the clipping path to the intersection of the current clipping path and the region within the specified rectangles.

After determining the new clipping path, the function resets the context’s current path to an empty path.

## See Also

### Working with the Current Clipping Path

- [CGContextClipToRect](<cgcontext/clip(to_)-7cbwq.md>) — Sets the clipping path to the intersection of the current clipping path with the area defined by the specified rectangle.
- [CGContextClipToMask](<cgcontext/clip(to_mask_).md>) — Maps a mask into the specified rectangle and intersects it with the current clipping area of the graphics context.
- [CGContextGetClipBoundingBox](cgcontext/boundingboxofclippath.md) — Returns the bounding box of a clipping path.
- [CGContextClip](cgcontextclip.md) — Modifies the current clipping path, using the nonzero winding number rule.
- [CGContextEOClip](cgcontexteoclip.md) — Modifies the current clipping path, using the even-odd rule.
