---
title: lineWidth
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibezierpath/linewidth
source_url: 'https://developer.apple.com/documentation/uikit/uibezierpath/linewidth'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibezierpath/linewidth.json'
content_hash: 'sha256:b0320c0a3d34b9e5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBezierPath](../uibezierpath.md)

# lineWidth

<sub>Instance Property</sub>

The line width of the path.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var lineWidth: CGFloat { get set }
```

## Discussion

The line width defines the thickness of the receiver’s stroked path. A width of 0 is interpreted as the thinnest line that can be rendered on a particular device. The actual rendered line width may vary from the specified width by as much as 2 device pixels, depending on the position of the line with respect to the pixel grid and the current anti-aliasing settings. The width of the line may also be affected by scaling factors specified in the current transformation matrix of the active graphics context.

The default line width is 1.0.

## See Also

### Accessing drawing properties

- [lineCapStyle](linecapstyle.md) — The shape of the endpoints of a stroked path.
- [lineJoinStyle](linejoinstyle.md) — The shape of the joints between connected segments of a stroked path.
- [miterLimit](miterlimit.md) — The limiting value that helps avoid spikes at junctions between connected line segments.
- [flatness](flatness.md) — The factor that determines the rendering accuracy for curved path segments.
- [usesEvenOddFillRule](usesevenoddfillrule.md) — A Boolean value that indicates whether the even-odd winding rule is in use for drawing paths.
- [- setLineDash:count:phase:](<setlinedash(__count_phase_).md>) — Sets the line-stroking pattern for the path.
- [- getLineDash:count:phase:](<getlinedash(__count_phase_).md>) — Retrieves the line-stroking pattern for the path.
