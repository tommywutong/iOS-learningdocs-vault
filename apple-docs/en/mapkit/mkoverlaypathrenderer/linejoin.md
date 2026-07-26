---
title: lineJoin
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkoverlaypathrenderer/linejoin
source_url: 'https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer/linejoin'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkoverlaypathrenderer/linejoin.json'
content_hash: 'sha256:9fdf6a003d346dac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKOverlayPathRenderer](../mkoverlaypathrenderer.md)

# lineJoin

<sub>Instance Property</sub>

The line join style to apply to the corners of the path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var lineJoin: CGLineJoin { get set }
```

## Discussion

The default line join style is [CGLineJoin.round](../../coregraphics/cglinejoin/round.md).

## See Also

### Accessing the drawing attributes

- [fillColor](fillcolor.md) — The fill color to use for the path.
- [strokeColor](strokecolor.md) — The stroke color to use for the path.
- [lineWidth](linewidth.md) — The stroke width to use for the path.
- [lineCap](linecap.md) — The line cap style to apply to the open ends of the path.
- [miterLimit](miterlimit.md) — The limiting value that helps avoid spikes at junctions between connected line segments.
- [lineDashPhase](linedashphase.md) — The offset (in points) at which to start drawing the dash pattern.
- [lineDashPattern](linedashpattern.md) — An array of numbers specifying the dash pattern to use for the path.
