---
title: 'CTRunGetImageBounds(_:_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctrungetimagebounds(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctrungetimagebounds(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctrungetimagebounds%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:2f304bcc2d046f84'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTRunGetImageBounds(_:_:_:)

<sub>Function</sub>

Calculates the image bounds for a glyph range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTRunGetImageBounds(_ run: CTRun, _ context: CGContext?, _ range: CFRange) -> CGRect
```

## Parameters

- `run` — The run for which to calculate the image bounds.

- `context` — The context for the image bounds being calculated. This is required because the context could have settings in it that would cause changes in the image bounds.

- `range` — The portion of the run to measure. If the length of the range is set to `0`, then the measure operation continues from the start index of the range to the end of the run.

## Return Value

A rectangle that tightly encloses the paths of the run’s glyphs, or, if `run`, `context`, or `range` is invalid, [CGRectNull](../coregraphics/cgrectnull.md).

## See Also

### Measuring the Glyph Run

- [CTLineGetBoundsWithOptions](<ctlinegetboundswithoptions(____).md>) — Calculates the bounds for a line.
- [CTRunGetTypographicBounds](<ctrungettypographicbounds(__________).md>) — Gets the typographic bounds of the run.
- [CTRunGetBaseAdvancesAndOrigins](<ctrungetbaseadvancesandorigins(________).md>) — Copies a range of base advances and origins into user-provided buffers.
