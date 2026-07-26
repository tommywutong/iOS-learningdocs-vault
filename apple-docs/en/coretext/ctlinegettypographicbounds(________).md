---
title: 'CTLineGetTypographicBounds(_:_:_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctlinegettypographicbounds(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctlinegettypographicbounds(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctlinegettypographicbounds%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:277c7085ab5ee7c0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTLineGetTypographicBounds(_:_:_:_:)

<sub>Function</sub>

Calculates the typographic bounds of a line.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTLineGetTypographicBounds(_ line: CTLine, _ ascent: UnsafeMutablePointer<CGFloat>?, _ descent: UnsafeMutablePointer<CGFloat>?, _ leading: UnsafeMutablePointer<CGFloat>?) -> Double
```

## Parameters

- `line` — The line whose typographic bounds are calculated.

- `ascent` — On output, the ascent of the line. This parameter can be set to `NULL` if not needed.

- `descent` — On output, the descent of the line. This parameter can be set to `NULL` if not needed.

- `leading` — On output, the leading of the line. This parameter can be set to `NULL` if not needed.

## Return Value

The typographic width of the line. If the line is invalid, this function returns `0`.

## See Also

### Measuring Lines

- [CTLineGetImageBounds](<ctlinegetimagebounds(____).md>) — Calculates the image bounds for a line.
- [CTLineGetTrailingWhitespaceWidth](<ctlinegettrailingwhitespacewidth(__).md>) — Returns the trailing whitespace width for a line.
