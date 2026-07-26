---
title: shouldRasterize
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkoverlaypathrenderer/shouldrasterize
source_url: 'https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer/shouldrasterize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkoverlaypathrenderer/shouldrasterize.json'
content_hash: 'sha256:fd0317898c37ca92'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKOverlayPathRenderer](../mkoverlaypathrenderer.md)

# shouldRasterize

<sub>Instance Property</sub>

A Boolean value that determines whether the overlay path renderer renders the overlay as a bitmap before compositing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var shouldRasterize: Bool { get set }
```

## Discussion

The default value is `false`.

Whenever possible, MapKit vectorizes overlay shapes by default so that they scale along with the map and remain sharp. In some cases, you may want to force the rasterization of an overlay and not vectorize it. Set this variable to `true` to force the overlay path renderer to render the overlay as a bitmap.

## See Also

### Drawing the path

- [- applyStrokePropertiesToContext:atZoomScale:](<applystrokeproperties(to_atzoomscale_).md>) — Applies the renderer’s stroke-related drawing properties to the specified graphics context.
- [- applyFillPropertiesToContext:atZoomScale:](<applyfillproperties(to_atzoomscale_).md>) — Applies the receiver’s fill-related drawing properties to the specified graphics context.
- [- strokePath:inContext:](<strokepath(__in_).md>) — Draws a line along the specified path.
- [- fillPath:inContext:](<fillpath(__in_).md>) — Fills the area that the specified path encloses.
