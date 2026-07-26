---
title: 'CTLineGetImageBounds(_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctlinegetimagebounds(_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctlinegetimagebounds(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctlinegetimagebounds%28_%3A_%3A%29.json'
content_hash: 'sha256:a242dba199de5409'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTLineGetImageBounds(_:_:)

<sub>Function</sub>

Calculates the image bounds for a line.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTLineGetImageBounds(_ line: CTLine, _ context: CGContext?) -> CGRect
```

## Parameters

- `line` — The line whose image bounds are calculated.

- `context` — The context for which the image bounds are calculated. This is required because the context could have settings in it that would cause changes in the image bounds.

## Return Value

A rectangle that tightly encloses the paths of the line’s glyphs, or, if the line or context is invalid, [CGRectNull](../coregraphics/cgrectnull.md).

## See Also

### Measuring Lines

- [CTLineGetTypographicBounds](<ctlinegettypographicbounds(________).md>) — Calculates the typographic bounds of a line.
- [CTLineGetTrailingWhitespaceWidth](<ctlinegettrailingwhitespacewidth(__).md>) — Returns the trailing whitespace width for a line.
