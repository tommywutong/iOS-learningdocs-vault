---
title: miterLimit
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibezierpath/miterlimit
source_url: 'https://developer.apple.com/documentation/uikit/uibezierpath/miterlimit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibezierpath/miterlimit.json'
content_hash: 'sha256:817b1746c1c1777d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBezierPath](../uibezierpath.md)

# miterLimit

<sub>Instance Property</sub>

The limiting value that helps avoid spikes at junctions between connected line segments.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var miterLimit: CGFloat { get set }
```

## Discussion

The miter limit helps you avoid spikes in paths that use the [CGLineJoin.miter](../../coregraphics/cglinejoin/miter.md) join style. If the ratio of the miter length—that is, the diagonal length of the miter join—to the line thickness exceeds the miter limit, the joint is converted to a bevel join. The default miter limit is 10, which results in the conversion of miters whose angle at the joint is less than 11 degrees.

## See Also

### Accessing drawing properties

- [lineWidth](linewidth.md) — The line width of the path.
- [lineCapStyle](linecapstyle.md) — The shape of the endpoints of a stroked path.
- [lineJoinStyle](linejoinstyle.md) — The shape of the joints between connected segments of a stroked path.
- [flatness](flatness.md) — The factor that determines the rendering accuracy for curved path segments.
- [usesEvenOddFillRule](usesevenoddfillrule.md) — A Boolean value that indicates whether the even-odd winding rule is in use for drawing paths.
- [- setLineDash:count:phase:](<setlinedash(__count_phase_).md>) — Sets the line-stroking pattern for the path.
- [- getLineDash:count:phase:](<getlinedash(__count_phase_).md>) — Retrieves the line-stroking pattern for the path.
