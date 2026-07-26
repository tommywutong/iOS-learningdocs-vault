---
title: 'strokePath:inContext:'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+（7.0 起废弃）, iPadOS 4.0+（7.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/mapkit/mkoverlaypathview/strokepath:incontext:'
source_url: 'https://developer.apple.com/documentation/mapkit/mkoverlaypathview/strokepath:incontext:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkoverlaypathview/strokepath%3Aincontext%3A.json'
content_hash: 'sha256:753480b8942e1cd9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKOverlayPathView](../mkoverlaypathview.md)

# strokePath:inContext:

<sub>Instance Method</sub>

Draws a line along the specified path.

> [!warning] Deprecated
> Use an [MKOverlayPathRenderer](../mkoverlaypathrenderer.md) object instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (void) strokePath:(CGPathRef) path inContext:(CGContextRef) context;
```

## Parameters

- `path` — The path to draw.

- `context` — The graphics context in which to draw the path.

## Discussion

You must set the current stroke color before calling this method. Typically you do this by calling the [applyStrokePropertiesToContext:atZoomScale:](applystrokepropertiestocontext_atzoomscale_.md) method prior to drawing. If the [strokeColor](strokecolor.md) property is currently `nil`, this method does nothing.

## See Also

### Drawing the Path

- [applyStrokePropertiesToContext:atZoomScale:](applystrokepropertiestocontext_atzoomscale_.md) — Applies the receiver’s current stroke-related drawing properties to the specified graphics context. _(deprecated)_
- [applyFillPropertiesToContext:atZoomScale:](applyfillpropertiestocontext_atzoomscale_.md) — Applies the receiver’s current fill-related drawing properties to the specified graphics context _(deprecated)_
- [fillPath:inContext:](fillpath_incontext_.md) — Fills the area enclosed by the specified path. _(deprecated)_
