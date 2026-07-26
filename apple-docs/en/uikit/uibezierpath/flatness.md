---
title: flatness
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibezierpath/flatness
source_url: 'https://developer.apple.com/documentation/uikit/uibezierpath/flatness'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibezierpath/flatness.json'
content_hash: 'sha256:896f8d2839d75606'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBezierPath](../uibezierpath.md)

# flatness

<sub>Instance Property</sub>

The factor that determines the rendering accuracy for curved path segments.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var flatness: CGFloat { get set }
```

## Discussion

The flatness value measures the largest permissible distance (measured in pixels) between a point on the true curve and a point on the rendered curve. Smaller values result in smoother curves but require more computation time. Larger values result in more jagged curves but are rendered much faster. The default flatness value is `0.6`.

In most cases, you should not change the flatness value. However, you might increase the flatness value temporarily to minimize the amount of time it takes to draw a shape temporarily (such as during scrolling).

## See Also

### Accessing drawing properties

- [lineWidth](linewidth.md) — The line width of the path.
- [lineCapStyle](linecapstyle.md) — The shape of the endpoints of a stroked path.
- [lineJoinStyle](linejoinstyle.md) — The shape of the joints between connected segments of a stroked path.
- [miterLimit](miterlimit.md) — The limiting value that helps avoid spikes at junctions between connected line segments.
- [usesEvenOddFillRule](usesevenoddfillrule.md) — A Boolean value that indicates whether the even-odd winding rule is in use for drawing paths.
- [- setLineDash:count:phase:](<setlinedash(__count_phase_).md>) — Sets the line-stroking pattern for the path.
- [- getLineDash:count:phase:](<getlinedash(__count_phase_).md>) — Retrieves the line-stroking pattern for the path.
