---
title: NSLineBreakMode.byTruncatingTail
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nslinebreakmode/bytruncatingtail
source_url: 'https://developer.apple.com/documentation/uikit/nslinebreakmode/bytruncatingtail'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslinebreakmode/bytruncatingtail.json'
content_hash: 'sha256:1975c36501eee072'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLineBreakMode](../nslinebreakmode.md)

# NSLineBreakMode.byTruncatingTail

<sub>Case</sub>

The value that indicates a line displays so that the beginning fits in the container and an ellipsis glyph indicates the missing text at the end of the line.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
case byTruncatingTail
```

## Discussion

Although this mode works for multiline text, it’s more often used for single line text.

## See Also

### Constants

- [NSLineBreakByWordWrapping](bywordwrapping.md) — The value that indicates wrapping occurs at word boundaries, unless the word doesn’t fit on a single line.
- [NSLineBreakByCharWrapping](bycharwrapping.md) — The value that indicates wrapping occurs before the first character that doesn’t fit.
- [NSLineBreakByClipping](byclipping.md) — The value that indicates lines don’t extend past the edge of the text container.
- [NSLineBreakByTruncatingHead](bytruncatinghead.md) — The value that indicates that a line displays so that the end fits in the container and an ellipsis glyph indicates the missing text at the beginning of the line.
- [NSLineBreakByTruncatingMiddle](bytruncatingmiddle.md) — The value that indicates that a line displays so that the beginning and end fit in the container and an ellipsis glyph indicates the missing text in the middle.
