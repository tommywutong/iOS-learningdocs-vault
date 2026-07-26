---
title: 'fillPath:inContext:'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+（7.0 起废弃）, iPadOS 4.0+（7.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/mapkit/mkoverlaypathview/fillpath:incontext:'
source_url: 'https://developer.apple.com/documentation/mapkit/mkoverlaypathview/fillpath:incontext:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkoverlaypathview/fillpath%3Aincontext%3A.json'
content_hash: 'sha256:2aea572c113f4d3f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKOverlayPathView](../mkoverlaypathview.md)

# fillPath:inContext:

<sub>Instance Method</sub>

Fills the area enclosed by the specified path.

> [!warning] Deprecated
> Use an [MKOverlayPathRenderer](../mkoverlaypathrenderer.md) object instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (void) fillPath:(CGPathRef) path inContext:(CGContextRef) context;
```

## Parameters

- `path` — The path to fill.

- `context` — The graphics context in which to draw the path.

## Discussion

You must set the current fill color before calling this method. Typically you do this by calling the [applyFillPropertiesToContext:atZoomScale:](applyfillpropertiestocontext_atzoomscale_.md) method prior to drawing. If the [fillColor](fillcolor.md) property is currently `nil`, this method does nothing.

## See Also

### Drawing the Path

- [applyStrokePropertiesToContext:atZoomScale:](applystrokepropertiestocontext_atzoomscale_.md) — Applies the receiver’s current stroke-related drawing properties to the specified graphics context. _(deprecated)_
- [applyFillPropertiesToContext:atZoomScale:](applyfillpropertiestocontext_atzoomscale_.md) — Applies the receiver’s current fill-related drawing properties to the specified graphics context _(deprecated)_
- [strokePath:inContext:](strokepath_incontext_.md) — Draws a line along the specified path. _(deprecated)_
