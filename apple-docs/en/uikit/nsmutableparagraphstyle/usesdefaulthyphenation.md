---
title: usesDefaultHyphenation
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsmutableparagraphstyle/usesdefaulthyphenation
source_url: 'https://developer.apple.com/documentation/uikit/nsmutableparagraphstyle/usesdefaulthyphenation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsmutableparagraphstyle/usesdefaulthyphenation.json'
content_hash: 'sha256:78d5cf646d7994f7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSMutableParagraphStyle](../nsmutableparagraphstyle.md)

# usesDefaultHyphenation

<sub>Instance Property</sub>

A Boolean value that indicates whether the paragraph style uses the system hyphenation settings.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var usesDefaultHyphenation: Bool { get set }
```

## Discussion

The system determines the exact hyphenation logic dynamically by examining the layout context such as language, platform, etc. When `true`, it affects the return value from [hyphenationFactor](hyphenationfactor.md) when the property is set to `0.0`.

## See Also

### Setting line-break information

- [lineBreakMode](linebreakmode.md) — The mode for breaking lines in the paragraph.
- [lineBreakStrategy](linebreakstrategy.md) — The strategies that the text system may use to break lines while laying out the paragraph.
- [hyphenationFactor](hyphenationfactor.md) — The paragraph’s threshold for hyphenation.
- [tighteningFactorForTruncation](../../appkit/nsmutableparagraphstyle/tighteningfactorfortruncation.md) — The threshold for using tightening as an alternative to truncation.
- [allowsDefaultTighteningForTruncation](allowsdefaulttighteningfortruncation.md) — A Boolean value that indicates whether the system tightens intercharacter spacing before truncating text.
