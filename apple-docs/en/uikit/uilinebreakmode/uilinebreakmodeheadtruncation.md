---
title: UILineBreakModeHeadTruncation
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Enumeration Case
platforms: [iOS 2.0+（6.0 起废弃）, iPadOS 2.0+（6.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uilinebreakmode/uilinebreakmodeheadtruncation
source_url: 'https://developer.apple.com/documentation/uikit/uilinebreakmode/uilinebreakmodeheadtruncation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilinebreakmode/uilinebreakmodeheadtruncation.json'
content_hash: 'sha256:d83aea66ea641d87'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILineBreakMode](../uilinebreakmode.md)

# UILineBreakModeHeadTruncation

<sub>Enumeration Case</sub>

Truncate text (as necessary) from the beginning of the line.

> [!warning] Deprecated
> Use [NSLineBreakByTruncatingHead](../nslinebreakmode/bytruncatinghead.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
UILineBreakModeHeadTruncation
```

## Discussion

For multiple lines of text, only text on the first line truncates.

## See Also

### Deprecated constants

- [UILineBreakModeWordWrap](uilinebreakmodewordwrap.md) — Wrap or clip the string only at word boundaries. _(deprecated)_
- [UILineBreakModeCharacterWrap](uilinebreakmodecharacterwrap.md) — Wrap or clip the string at the closest character boundary. _(deprecated)_
- [UILineBreakModeClip](uilinebreakmodeclip.md) — Clip the text when reaching the end of the drawing rectangle. _(deprecated)_
- [UILineBreakModeTailTruncation](uilinebreakmodetailtruncation.md) — Truncate text (as necessary) from the end of the line. _(deprecated)_
- [UILineBreakModeMiddleTruncation](uilinebreakmodemiddletruncation.md) — Truncate text (as necessary) from the middle of the line. _(deprecated)_
