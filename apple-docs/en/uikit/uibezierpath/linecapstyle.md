---
title: lineCapStyle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibezierpath/linecapstyle
source_url: 'https://developer.apple.com/documentation/uikit/uibezierpath/linecapstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibezierpath/linecapstyle.json'
content_hash: 'sha256:ff84d7db67522b71'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBezierPath](../uibezierpath.md)

# lineCapStyle

<sub>Instance Property</sub>

The shape of the endpoints of a stroked path.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var lineCapStyle: CGLineCap { get set }
```

## Discussion

The line cap style is applied to the start and end points of any open subpaths. This property does not affect closed subpaths. The default line cap style is [CGLineCap.butt](../../coregraphics/cglinecap/butt.md).

## See Also

### Accessing drawing properties

- [lineWidth](linewidth.md) — The line width of the path.
- [lineJoinStyle](linejoinstyle.md) — The shape of the joints between connected segments of a stroked path.
- [miterLimit](miterlimit.md) — The limiting value that helps avoid spikes at junctions between connected line segments.
- [flatness](flatness.md) — The factor that determines the rendering accuracy for curved path segments.
- [usesEvenOddFillRule](usesevenoddfillrule.md) — A Boolean value that indicates whether the even-odd winding rule is in use for drawing paths.
- [- setLineDash:count:phase:](<setlinedash(__count_phase_).md>) — Sets the line-stroking pattern for the path.
- [- getLineDash:count:phase:](<getlinedash(__count_phase_).md>) — Retrieves the line-stroking pattern for the path.
