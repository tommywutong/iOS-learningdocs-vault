---
title: 'CTLineGetBoundsWithOptions(_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctlinegetboundswithoptions(_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctlinegetboundswithoptions(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctlinegetboundswithoptions%28_%3A_%3A%29.json'
content_hash: 'sha256:f6f35f10af487920'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTLineGetBoundsWithOptions(_:_:)

<sub>Function</sub>

Calculates the bounds for a line.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTLineGetBoundsWithOptions(_ line: CTLine, _ options: CTLineBoundsOptions) -> CGRect
```

## Parameters

- `line` — The line for which you calculate the bounds.

- `options` — Desired options or `0` if none.

## Return Value

The bounds of the line as specified by the type and options, such that the coordinate origin is coincident with the line origin and the rect origin is at the bottom left. If the line is invalid, this function will return [CGRectNull](../coregraphics/cgrectnull.md).

## See Also

### Related Documentation

- [CTLineBoundsOptions](ctlineboundsoptions.md) — Options for getting the bounds of a line of text.

### Measuring the Glyph Run

- [CTRunGetTypographicBounds](<ctrungettypographicbounds(__________).md>) — Gets the typographic bounds of the run.
- [CTRunGetImageBounds](<ctrungetimagebounds(______).md>) — Calculates the image bounds for a glyph range.
- [CTRunGetBaseAdvancesAndOrigins](<ctrungetbaseadvancesandorigins(________).md>) — Copies a range of base advances and origins into user-provided buffers.
