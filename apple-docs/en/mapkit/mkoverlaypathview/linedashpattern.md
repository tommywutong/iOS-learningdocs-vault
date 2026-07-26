---
title: lineDashPattern
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（7.0 起废弃）, iPadOS 4.0+（7.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/mapkit/mkoverlaypathview/linedashpattern
source_url: 'https://developer.apple.com/documentation/mapkit/mkoverlaypathview/linedashpattern'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkoverlaypathview/linedashpattern.json'
content_hash: 'sha256:4739c9a9bda1776f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKOverlayPathView](../mkoverlaypathview.md)

# lineDashPattern

<sub>Instance Property</sub>

An array of numbers indicating the dash pattern for paths.

> [!warning] Deprecated
> Use an [MKOverlayPathRenderer](../mkoverlaypathrenderer.md) object instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (copy) NSArray * lineDashPattern;
```

## Discussion

The array contains one or more [NSNumber](../../foundation/nsnumber.md) objects that indicate the lengths (measured in points) of the line segments and gaps in the pattern. The values in the array alternate, starting with the first line segment length, followed by the first gap length, followed by the second line segment length, and so on.

This property is set to `nil` by default, which indicates no line dash pattern.

## See Also

### Accessing the drawing attributes

- [fillColor](fillcolor.md) — The fill color to use for the path. _(deprecated)_
- [strokeColor](strokecolor.md) — The stroke color to use for the path. _(deprecated)_
- [lineWidth](linewidth.md) — The stroke width to use for the path. _(deprecated)_
- [lineJoin](linejoin.md) — The line join style to apply to corners of the path. _(deprecated)_
- [lineCap](linecap.md) — The line cap style to apply to the open ends of the path. _(deprecated)_
- [miterLimit](miterlimit.md) — The limiting value that helps avoid spikes at junctions between connected line segments. _(deprecated)_
- [lineDashPhase](linedashphase.md) — The offset (in points) at which to start drawing the dash pattern. _(deprecated)_
