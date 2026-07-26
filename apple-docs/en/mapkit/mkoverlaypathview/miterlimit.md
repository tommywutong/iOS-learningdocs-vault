---
title: miterLimit
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（7.0 起废弃）, iPadOS 4.0+（7.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/mapkit/mkoverlaypathview/miterlimit
source_url: 'https://developer.apple.com/documentation/mapkit/mkoverlaypathview/miterlimit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkoverlaypathview/miterlimit.json'
content_hash: 'sha256:23bd0cf5ef03289c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKOverlayPathView](../mkoverlaypathview.md)

# miterLimit

<sub>Instance Property</sub>

The limiting value that helps avoid spikes at junctions between connected line segments.

> [!warning] Deprecated
> Use an [MKOverlayPathRenderer](../mkoverlaypathrenderer.md) object instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property CGFloat miterLimit;
```

## Discussion

The miter limit helps you avoid spikes in paths that use the [CGLineJoin.miter](../../coregraphics/cglinejoin/miter.md) join style. If the ratio of the miter length—that is, the diagonal length of the miter join—to the line thickness exceeds the miter limit, the joint is converted to a bevel join. The default miter limit is 10, which results in the conversion of miters whose angle at the joint is less than 11 degrees.

## See Also

### Accessing the drawing attributes

- [fillColor](fillcolor.md) — The fill color to use for the path. _(deprecated)_
- [strokeColor](strokecolor.md) — The stroke color to use for the path. _(deprecated)_
- [lineWidth](linewidth.md) — The stroke width to use for the path. _(deprecated)_
- [lineJoin](linejoin.md) — The line join style to apply to corners of the path. _(deprecated)_
- [lineCap](linecap.md) — The line cap style to apply to the open ends of the path. _(deprecated)_
- [lineDashPhase](linedashphase.md) — The offset (in points) at which to start drawing the dash pattern. _(deprecated)_
- [lineDashPattern](linedashpattern.md) — An array of numbers indicating the dash pattern for paths. _(deprecated)_
