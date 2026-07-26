---
title: 'getLineDash(_:count:phase:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibezierpath/getlinedash(_:count:phase:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibezierpath/getlinedash(_:count:phase:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibezierpath/getlinedash%28_%3Acount%3Aphase%3A%29.json'
content_hash: 'sha256:e4e54390b1ce4939'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBezierPath](../uibezierpath.md)

# getLineDash(_:count:phase:)

<sub>Instance Method</sub>

Retrieves the line-stroking pattern for the path.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func getLineDash(_ pattern: UnsafeMutablePointer<CGFloat>?, count: UnsafeMutablePointer<Int>?, phase: UnsafeMutablePointer<CGFloat>?)
```

## Parameters

- `pattern` — On input, a C-style array of floating point values, or `nil` if you do not want the pattern values. On output, this array contains the lengths (measured in points) of the line segments and gaps in the pattern. The values in the array alternate, starting with the first line segment length, followed by the first gap length, followed by the second line segment length, and so on.

- `count` — On input, a pointer to an integer or `nil` if you do not want the number of pattern entries. On output, the number of entries written to `pattern`.

- `phase` — On input, a pointer to a floating point value or `nil` if you do not want the phase. On output, this value contains the offset at which to start drawing the pattern, measured in points along the dashed-line pattern. For example, a phase of 6 in the pattern 5-2-3-2 would cause drawing to begin in the middle of the first gap.

## Discussion

The array in the `pattern` parameter must be large enough to hold all of the returned values in the pattern. If you are not sure how many values there might be, you can call this method twice. The first time you call it, do not pass a value for `pattern` but use the returned value in the `count` parameter to allocate an array of floating-point numbers that you can then pass in the second time.

## See Also

### Accessing drawing properties

- [lineWidth](linewidth.md) — The line width of the path.
- [lineCapStyle](linecapstyle.md) — The shape of the endpoints of a stroked path.
- [lineJoinStyle](linejoinstyle.md) — The shape of the joints between connected segments of a stroked path.
- [miterLimit](miterlimit.md) — The limiting value that helps avoid spikes at junctions between connected line segments.
- [flatness](flatness.md) — The factor that determines the rendering accuracy for curved path segments.
- [usesEvenOddFillRule](usesevenoddfillrule.md) — A Boolean value that indicates whether the even-odd winding rule is in use for drawing paths.
- [- setLineDash:count:phase:](<setlinedash(__count_phase_).md>) — Sets the line-stroking pattern for the path.
