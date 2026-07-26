---
title: UILineBreakModeClip
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Enumeration Case
platforms: [iOS 2.0+（6.0 起废弃）, iPadOS 2.0+（6.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uilinebreakmode/uilinebreakmodeclip
source_url: 'https://developer.apple.com/documentation/uikit/uilinebreakmode/uilinebreakmodeclip'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilinebreakmode/uilinebreakmodeclip.json'
content_hash: 'sha256:9069171b0f4a26ed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILineBreakMode](../uilinebreakmode.md)

# UILineBreakModeClip

<sub>Enumeration Case</sub>

Clip the text when reaching the end of the drawing rectangle.

> [!warning] Deprecated
> Use [NSLineBreakByClipping](../nslinebreakmode/byclipping.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
UILineBreakModeClip
```

## Discussion

This option could result in a partially rendered character at the end of a string.

## See Also

### Deprecated constants

- [UILineBreakModeWordWrap](uilinebreakmodewordwrap.md) — Wrap or clip the string only at word boundaries. _(deprecated)_
- [UILineBreakModeCharacterWrap](uilinebreakmodecharacterwrap.md) — Wrap or clip the string at the closest character boundary. _(deprecated)_
- [UILineBreakModeHeadTruncation](uilinebreakmodeheadtruncation.md) — Truncate text (as necessary) from the beginning of the line. _(deprecated)_
- [UILineBreakModeTailTruncation](uilinebreakmodetailtruncation.md) — Truncate text (as necessary) from the end of the line. _(deprecated)_
- [UILineBreakModeMiddleTruncation](uilinebreakmodemiddletruncation.md) — Truncate text (as necessary) from the middle of the line. _(deprecated)_
