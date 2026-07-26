---
title: 'CTLineGetTrailingWhitespaceWidth(_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctlinegettrailingwhitespacewidth(_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctlinegettrailingwhitespacewidth(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctlinegettrailingwhitespacewidth%28_%3A%29.json'
content_hash: 'sha256:7700377db5e256ce'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTLineGetTrailingWhitespaceWidth(_:)

<sub>Function</sub>

Returns the trailing whitespace width for a line.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTLineGetTrailingWhitespaceWidth(_ line: CTLine) -> Double
```

## Parameters

- `line` — The line whose trailing whitespace width is calculated.

## Return Value

The width of the line’s trailing whitespace. If the line is invalid, this function will always return zero.

## Discussion

Creating a line for a width can result in a line that is actually longer than the desired width due to trailing whitespace. Although this is typically not an issue due to whitespace being invisible, this function can be used to determine what amount of a line’s width is due to trailing whitespace.

## See Also

### Measuring Lines

- [CTLineGetImageBounds](<ctlinegetimagebounds(____).md>) — Calculates the image bounds for a line.
- [CTLineGetTypographicBounds](<ctlinegettypographicbounds(________).md>) — Calculates the typographic bounds of a line.
