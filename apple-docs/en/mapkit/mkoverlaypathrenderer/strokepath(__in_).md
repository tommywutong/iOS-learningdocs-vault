---
title: 'strokePath(_:in:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkoverlaypathrenderer/strokepath(_:in:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer/strokepath(_:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkoverlaypathrenderer/strokepath%28_%3Ain%3A%29.json'
content_hash: 'sha256:7a0fbbc85692e472'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKOverlayPathRenderer](../mkoverlaypathrenderer.md)

# strokePath(_:in:)

<sub>Instance Method</sub>

Draws a line along the specified path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func strokePath(_ path: CGPath, in context: CGContext)
```

## Parameters

- `path` — The path to draw.

- `context` — The graphics context in which to draw the path.

## Discussion

You must set the current stroke color before calling this method. Typically you do this by calling the [- applyStrokePropertiesToContext:atZoomScale:](<applystrokeproperties(to_atzoomscale_).md>) method prior to drawing. If the [strokeColor](strokecolor.md) property is currently `nil`, this method does nothing.

## See Also

### Drawing the path

- [- applyStrokePropertiesToContext:atZoomScale:](<applystrokeproperties(to_atzoomscale_).md>) — Applies the renderer’s stroke-related drawing properties to the specified graphics context.
- [- applyFillPropertiesToContext:atZoomScale:](<applyfillproperties(to_atzoomscale_).md>) — Applies the receiver’s fill-related drawing properties to the specified graphics context.
- [- fillPath:inContext:](<fillpath(__in_).md>) — Fills the area that the specified path encloses.
- [shouldRasterize](shouldrasterize.md) — A Boolean value that determines whether the overlay path renderer renders the overlay as a bitmap before compositing.
