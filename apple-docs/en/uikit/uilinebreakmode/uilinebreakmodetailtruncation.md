---
title: UILineBreakModeTailTruncation
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Enumeration Case
platforms: [iOS 2.0+（6.0 起废弃）, iPadOS 2.0+（6.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uilinebreakmode/uilinebreakmodetailtruncation
source_url: 'https://developer.apple.com/documentation/uikit/uilinebreakmode/uilinebreakmodetailtruncation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilinebreakmode/uilinebreakmodetailtruncation.json'
content_hash: 'sha256:49a4d5d796cdfce2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILineBreakMode](../uilinebreakmode.md)

# UILineBreakModeTailTruncation

<sub>Enumeration Case</sub>

Truncate text (as necessary) from the end of the line.

> [!warning] Deprecated
> Use [NSLineBreakByTruncatingTail](../nslinebreakmode/bytruncatingtail.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
UILineBreakModeTailTruncation
```

## Discussion

For multiple lines of text, only text on the last line truncates.

## See Also

### Deprecated constants

- [UILineBreakModeWordWrap](uilinebreakmodewordwrap.md) — Wrap or clip the string only at word boundaries. _(deprecated)_
- [UILineBreakModeCharacterWrap](uilinebreakmodecharacterwrap.md) — Wrap or clip the string at the closest character boundary. _(deprecated)_
- [UILineBreakModeClip](uilinebreakmodeclip.md) — Clip the text when reaching the end of the drawing rectangle. _(deprecated)_
- [UILineBreakModeHeadTruncation](uilinebreakmodeheadtruncation.md) — Truncate text (as necessary) from the beginning of the line. _(deprecated)_
- [UILineBreakModeMiddleTruncation](uilinebreakmodemiddletruncation.md) — Truncate text (as necessary) from the middle of the line. _(deprecated)_
