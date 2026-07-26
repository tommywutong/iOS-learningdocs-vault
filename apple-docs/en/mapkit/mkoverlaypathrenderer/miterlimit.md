---
title: miterLimit
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkoverlaypathrenderer/miterlimit
source_url: 'https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer/miterlimit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkoverlaypathrenderer/miterlimit.json'
content_hash: 'sha256:b25b77a320848262'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKOverlayPathRenderer](../mkoverlaypathrenderer.md)

# miterLimit

<sub>Instance Property</sub>

The limiting value that helps avoid spikes at junctions between connected line segments.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var miterLimit: CGFloat { get set }
```

## Discussion

The miter limit helps you avoid spikes in paths that use the [CGLineJoin.miter](../../coregraphics/cglinejoin/miter.md) join style. If the ratio of the miter length to the line thickness — the diagonal length of the miter join — exceeds the miter limit, the renderer converts the joint to a bevel join. The default miter limit is `10`, which results in the conversion of miters with an angle at the joint of less than `11` degrees.

## See Also

### Accessing the drawing attributes

- [fillColor](fillcolor.md) — The fill color to use for the path.
- [strokeColor](strokecolor.md) — The stroke color to use for the path.
- [lineWidth](linewidth.md) — The stroke width to use for the path.
- [lineJoin](linejoin.md) — The line join style to apply to the corners of the path.
- [lineCap](linecap.md) — The line cap style to apply to the open ends of the path.
- [lineDashPhase](linedashphase.md) — The offset (in points) at which to start drawing the dash pattern.
- [lineDashPattern](linedashpattern.md) — An array of numbers specifying the dash pattern to use for the path.
