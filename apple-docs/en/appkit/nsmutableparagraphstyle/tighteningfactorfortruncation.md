---
title: tighteningFactorForTruncation
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nsmutableparagraphstyle/tighteningfactorfortruncation
source_url: 'https://developer.apple.com/documentation/appkit/nsmutableparagraphstyle/tighteningfactorfortruncation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nsmutableparagraphstyle/tighteningfactorfortruncation.json'
content_hash: 'sha256:fb56a8ca6efd1523'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSMutableParagraphStyle](../nsmutableparagraphstyle.md)

# tighteningFactorForTruncation

<sub>Instance Property</sub>

The threshold for using tightening as an alternative to truncation.

<sub>macOS</sub>

```swift
var tighteningFactorForTruncation: Float { get set }
```

## Discussion

When the line break mode specifies truncation, the text system attempts to tighten inter character spacing as an alternative to truncation, provided that the ratio of the text width to the line fragment width does not exceed 1.0 + the value of [tighteningFactorForTruncation](../nsparagraphstyle/tighteningfactorfortruncation.md). Otherwise the text is truncated at a location determined by the line break mode. The default value is 0.05. This value can be a positive or negative value. Values less than or equal to 0.0 result in not tightening.

## See Also

### Setting line-break information

- [lineBreakMode](linebreakmode.md) — The mode for breaking lines in the paragraph.
- [lineBreakStrategy](linebreakstrategy.md) — The strategies that the text system may use to break lines while laying out the paragraph.
- [hyphenationFactor](hyphenationfactor.md) — The paragraph’s threshold for hyphenation.
- [usesDefaultHyphenation](usesdefaulthyphenation.md)
- [allowsDefaultTighteningForTruncation](allowsdefaulttighteningfortruncation.md) — A Boolean value that indicates whether the system tightens intercharacter spacing before truncating text.
