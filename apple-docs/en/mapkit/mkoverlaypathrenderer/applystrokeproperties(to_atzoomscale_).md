---
title: 'applyStrokeProperties(to:atZoomScale:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkoverlaypathrenderer/applystrokeproperties(to:atzoomscale:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer/applystrokeproperties(to:atzoomscale:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkoverlaypathrenderer/applystrokeproperties%28to%3Aatzoomscale%3A%29.json'
content_hash: 'sha256:8265cf1c97b19e0d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKOverlayPathRenderer](../mkoverlaypathrenderer.md)

# applyStrokeProperties(to:atZoomScale:)

<sub>Instance Method</sub>

Applies the renderer’s stroke-related drawing properties to the specified graphics context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func applyStrokeProperties(to context: CGContext, atZoomScale zoomScale: MKZoomScale)
```

## Parameters

- `context` — The graphics context for drawing the view’s contents.

- `zoomScale` — The zoom scale for drawing.

## Discussion

This is a convenience method for applying all of the drawing properties MapKit uses when stroking a path. This method applies the stroke color, line width, line join, line cap, miter limit, line dash phase, and line dash attributes to the specified graphics context. This method applies the scale factor in the `zoomScale` parameter to the line width and line dash pattern automatically so that lines scale appropriately.

This method doesn’t save the current graphics state before applying the new attributes. If you want to preserve the existing state, save it and restore it later when you finish drawing.

## See Also

### Drawing the path

- [- applyFillPropertiesToContext:atZoomScale:](<applyfillproperties(to_atzoomscale_).md>) — Applies the receiver’s fill-related drawing properties to the specified graphics context.
- [- strokePath:inContext:](<strokepath(__in_).md>) — Draws a line along the specified path.
- [- fillPath:inContext:](<fillpath(__in_).md>) — Fills the area that the specified path encloses.
- [shouldRasterize](shouldrasterize.md) — A Boolean value that determines whether the overlay path renderer renders the overlay as a bitmap before compositing.
