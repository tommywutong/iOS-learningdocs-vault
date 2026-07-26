---
title: 'setLineDash(_:count:phase:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibezierpath/setlinedash(_:count:phase:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibezierpath/setlinedash(_:count:phase:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibezierpath/setlinedash%28_%3Acount%3Aphase%3A%29.json'
content_hash: 'sha256:deac78c109135924'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBezierPath](../uibezierpath.md)

# setLineDash(_:count:phase:)

<sub>Instance Method</sub>

Sets the line-stroking pattern for the path.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func setLineDash(_ pattern: UnsafePointer<CGFloat>?, count: Int, phase: CGFloat)
```

## Parameters

- `pattern` — A C-style array of floating point values that contains the lengths (measured in points) of the line segments and gaps in the pattern. The values in the array alternate, starting with the first line segment length, followed by the first gap length, followed by the second line segment length, and so on.

- `count` — The number of values in `pattern`.

- `phase` — The offset at which to start drawing the pattern, measured in points along the dashed-line pattern. For example, a phase value of `6` for the pattern 5-2-3-2 would cause drawing to begin in the middle of the first gap.

## See Also

### Accessing drawing properties

- [lineWidth](linewidth.md) — The line width of the path.
- [lineCapStyle](linecapstyle.md) — The shape of the endpoints of a stroked path.
- [lineJoinStyle](linejoinstyle.md) — The shape of the joints between connected segments of a stroked path.
- [miterLimit](miterlimit.md) — The limiting value that helps avoid spikes at junctions between connected line segments.
- [flatness](flatness.md) — The factor that determines the rendering accuracy for curved path segments.
- [usesEvenOddFillRule](usesevenoddfillrule.md) — A Boolean value that indicates whether the even-odd winding rule is in use for drawing paths.
- [- getLineDash:count:phase:](<getlinedash(__count_phase_).md>) — Retrieves the line-stroking pattern for the path.
