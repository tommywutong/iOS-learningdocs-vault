---
title: 'applyFillPropertiesToContext:atZoomScale:'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+（7.0 起废弃）, iPadOS 4.0+（7.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/mapkit/mkoverlaypathview/applyfillpropertiestocontext:atzoomscale:'
source_url: 'https://developer.apple.com/documentation/mapkit/mkoverlaypathview/applyfillpropertiestocontext:atzoomscale:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkoverlaypathview/applyfillpropertiestocontext%3Aatzoomscale%3A.json'
content_hash: 'sha256:062b69d46e67bc95'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKOverlayPathView](../mkoverlaypathview.md)

# applyFillPropertiesToContext:atZoomScale:

<sub>Instance Method</sub>

Applies the receiver’s current fill-related drawing properties to the specified graphics context

> [!warning] Deprecated
> Use an [MKOverlayPathRenderer](../mkoverlaypathrenderer.md) object instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (void) applyFillPropertiesToContext:(CGContextRef) context atZoomScale:(MKZoomScale) zoomScale;
```

## Parameters

- `context` — The graphics context used to draw the view’s contents.

- `zoomScale` — The current zoom scale used for drawing.

## Discussion

This is a convenience method for applying all of the drawing properties used when filling a path. This method applies the current fill color to the specified graphics context.

## See Also

### Drawing the Path

- [applyStrokePropertiesToContext:atZoomScale:](applystrokepropertiestocontext_atzoomscale_.md) — Applies the receiver’s current stroke-related drawing properties to the specified graphics context. _(deprecated)_
- [strokePath:inContext:](strokepath_incontext_.md) — Draws a line along the specified path. _(deprecated)_
- [fillPath:inContext:](fillpath_incontext_.md) — Fills the area enclosed by the specified path. _(deprecated)_
