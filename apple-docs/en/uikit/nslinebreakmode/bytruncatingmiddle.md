---
title: NSLineBreakMode.byTruncatingMiddle
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nslinebreakmode/bytruncatingmiddle
source_url: 'https://developer.apple.com/documentation/uikit/nslinebreakmode/bytruncatingmiddle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslinebreakmode/bytruncatingmiddle.json'
content_hash: 'sha256:866841108196c5cf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLineBreakMode](../nslinebreakmode.md)

# NSLineBreakMode.byTruncatingMiddle

<sub>Case</sub>

The value that indicates that a line displays so that the beginning and end fit in the container and an ellipsis glyph indicates the missing text in the middle.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
case byTruncatingMiddle
```

## Discussion

Use this mode for single-line layout; using it with multiline text truncates the text into a single line.

## See Also

### Constants

- [NSLineBreakByWordWrapping](bywordwrapping.md) — The value that indicates wrapping occurs at word boundaries, unless the word doesn’t fit on a single line.
- [NSLineBreakByCharWrapping](bycharwrapping.md) — The value that indicates wrapping occurs before the first character that doesn’t fit.
- [NSLineBreakByClipping](byclipping.md) — The value that indicates lines don’t extend past the edge of the text container.
- [NSLineBreakByTruncatingHead](bytruncatinghead.md) — The value that indicates that a line displays so that the end fits in the container and an ellipsis glyph indicates the missing text at the beginning of the line.
- [NSLineBreakByTruncatingTail](bytruncatingtail.md) — The value that indicates a line displays so that the beginning fits in the container and an ellipsis glyph indicates the missing text at the end of the line.
