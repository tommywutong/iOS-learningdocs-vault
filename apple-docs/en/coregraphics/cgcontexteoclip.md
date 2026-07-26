---
title: CGContextEOClip
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgcontexteoclip
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontexteoclip'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontexteoclip.json'
content_hash: 'sha256:4de535a84e16dc52'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGContextEOClip

<sub>Function</sub>

Modifies the current clipping path, using the even-odd rule.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void CGContextEOClip(CGContextRef c);
```

## Parameters

- `c` — A graphics context containing a path. If the context does not have a current path, the function does nothing.

## Discussion

The function uses the even-odd rule to calculate the intersection of the current path with the current clipping path. The path resulting from the intersection is used as the new current clipping path for subsequent painting operations.

If the current path includes any open subpaths, the paths are treated as if they were closed by calling [CGContextClosePath](<cgcontext/closepath().md>).

Unlike the current path, the current clipping path is part of the graphics state. Therefore, to re-enlarge the paintable area by restoring the clipping path to a prior state, you must save the graphics state before you clip and restore the graphics state after you’ve completed any clipped drawing.

After determining the new clipping path, the function resets the context’s current path to an empty path.

## See Also

### Working with the Current Clipping Path

- [CGContextClipToRect](<cgcontext/clip(to_)-7cbwq.md>) — Sets the clipping path to the intersection of the current clipping path with the area defined by the specified rectangle.
- [CGContextClipToMask](<cgcontext/clip(to_mask_).md>) — Maps a mask into the specified rectangle and intersects it with the current clipping area of the graphics context.
- [CGContextGetClipBoundingBox](cgcontext/boundingboxofclippath.md) — Returns the bounding box of a clipping path.
- [CGContextClip](cgcontextclip.md) — Modifies the current clipping path, using the nonzero winding number rule.
- [CGContextClipToRects](cgcontextcliptorects.md) — Sets the clipping path to the intersection of the current clipping path with the region defined by an array of rectangles.
