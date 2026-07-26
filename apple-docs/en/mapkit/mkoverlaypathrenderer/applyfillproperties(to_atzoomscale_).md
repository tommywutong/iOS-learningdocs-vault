---
title: 'applyFillProperties(to:atZoomScale:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkoverlaypathrenderer/applyfillproperties(to:atzoomscale:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer/applyfillproperties(to:atzoomscale:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkoverlaypathrenderer/applyfillproperties%28to%3Aatzoomscale%3A%29.json'
content_hash: 'sha256:51d9af248eda582a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKOverlayPathRenderer](../mkoverlaypathrenderer.md)

# applyFillProperties(to:atZoomScale:)

<sub>Instance Method</sub>

Applies the receiver’s fill-related drawing properties to the specified graphics context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func applyFillProperties(to context: CGContext, atZoomScale zoomScale: MKZoomScale)
```

## Parameters

- `context` — The graphics context used to draw the view’s contents.

- `zoomScale` — The current zoom scale used for drawing.

## Discussion

This is a convenience method for applying all of the drawing properties used when filling a path. This method applies the current fill color to the specified graphics context.

## See Also

### Drawing the path

- [- applyStrokePropertiesToContext:atZoomScale:](<applystrokeproperties(to_atzoomscale_).md>) — Applies the renderer’s stroke-related drawing properties to the specified graphics context.
- [- strokePath:inContext:](<strokepath(__in_).md>) — Draws a line along the specified path.
- [- fillPath:inContext:](<fillpath(__in_).md>) — Fills the area that the specified path encloses.
- [shouldRasterize](shouldrasterize.md) — A Boolean value that determines whether the overlay path renderer renders the overlay as a bitmap before compositing.
