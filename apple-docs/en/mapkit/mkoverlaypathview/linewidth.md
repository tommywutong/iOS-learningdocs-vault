---
title: lineWidth
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（7.0 起废弃）, iPadOS 4.0+（7.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/mapkit/mkoverlaypathview/linewidth
source_url: 'https://developer.apple.com/documentation/mapkit/mkoverlaypathview/linewidth'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkoverlaypathview/linewidth.json'
content_hash: 'sha256:79718c3c2b0865ab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKOverlayPathView](../mkoverlaypathview.md)

# lineWidth

<sub>Instance Property</sub>

The stroke width to use for the path.

> [!warning] Deprecated
> Use an [MKOverlayPathRenderer](../mkoverlaypathrenderer.md) object instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property CGFloat lineWidth;
```

## Discussion

The default value of this property is 0.

## See Also

### Accessing the drawing attributes

- [fillColor](fillcolor.md) — The fill color to use for the path. _(deprecated)_
- [strokeColor](strokecolor.md) — The stroke color to use for the path. _(deprecated)_
- [lineJoin](linejoin.md) — The line join style to apply to corners of the path. _(deprecated)_
- [lineCap](linecap.md) — The line cap style to apply to the open ends of the path. _(deprecated)_
- [miterLimit](miterlimit.md) — The limiting value that helps avoid spikes at junctions between connected line segments. _(deprecated)_
- [lineDashPhase](linedashphase.md) — The offset (in points) at which to start drawing the dash pattern. _(deprecated)_
- [lineDashPattern](linedashpattern.md) — An array of numbers indicating the dash pattern for paths. _(deprecated)_
