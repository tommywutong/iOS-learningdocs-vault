---
title: 'CTRunGetTypographicBounds(_:_:_:_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctrungettypographicbounds(_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctrungettypographicbounds(_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctrungettypographicbounds%28_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:fe74338f5ffe519e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTRunGetTypographicBounds(_:_:_:_:_:)

<sub>Function</sub>

Gets the typographic bounds of the run.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTRunGetTypographicBounds(_ run: CTRun, _ range: CFRange, _ ascent: UnsafeMutablePointer<CGFloat>?, _ descent: UnsafeMutablePointer<CGFloat>?, _ leading: UnsafeMutablePointer<CGFloat>?) -> Double
```

## Parameters

- `run` — The run for which to calculate the typographic bounds.

- `range` — The portion of the run to measure. If the length of the range is set to `0`, then the measure operation continues from the range’s start index to the end of the run.

- `ascent` — On output, the ascent of the run. This can be set to `NULL` if not needed.

- `descent` — On output, the descent of the run. This can be set to `NULL` if not needed.

- `leading` — On output, the leading of the run. This can be set to `NULL` if not needed.

## Return Value

The typographic width of the run, or if `run` or `range` is invalid, `0`.

## See Also

### Measuring the Glyph Run

- [CTLineGetBoundsWithOptions](<ctlinegetboundswithoptions(____).md>) — Calculates the bounds for a line.
- [CTRunGetImageBounds](<ctrungetimagebounds(______).md>) — Calculates the image bounds for a glyph range.
- [CTRunGetBaseAdvancesAndOrigins](<ctrungetbaseadvancesandorigins(________).md>) — Copies a range of base advances and origins into user-provided buffers.
