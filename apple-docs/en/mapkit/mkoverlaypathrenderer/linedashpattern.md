---
title: lineDashPattern
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkoverlaypathrenderer/linedashpattern
source_url: 'https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer/linedashpattern'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkoverlaypathrenderer/linedashpattern.json'
content_hash: 'sha256:1bc6ace85f32ad0a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKOverlayPathRenderer](../mkoverlaypathrenderer.md)

# lineDashPattern

<sub>Instance Property</sub>

An array of numbers specifying the dash pattern to use for the path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var lineDashPattern: [NSNumber]? { get set }
```

## Discussion

The array contains one or more [NSNumber](../../foundation/nsnumber.md) objects that indicate the lengths (in points) of the line segments and gaps in the pattern. The values in the array alternate, starting with the first line segment length, followed by the first gap length, followed by the second line segment length, and so on.

This property is `nil` by default, which indicates no line dash pattern.

## See Also

### Accessing the drawing attributes

- [fillColor](fillcolor.md) — The fill color to use for the path.
- [strokeColor](strokecolor.md) — The stroke color to use for the path.
- [lineWidth](linewidth.md) — The stroke width to use for the path.
- [lineJoin](linejoin.md) — The line join style to apply to the corners of the path.
- [lineCap](linecap.md) — The line cap style to apply to the open ends of the path.
- [miterLimit](miterlimit.md) — The limiting value that helps avoid spikes at junctions between connected line segments.
- [lineDashPhase](linedashphase.md) — The offset (in points) at which to start drawing the dash pattern.
