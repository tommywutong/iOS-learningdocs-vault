---
title: allowsDefaultTighteningForTruncation
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsmutableparagraphstyle/allowsdefaulttighteningfortruncation
source_url: 'https://developer.apple.com/documentation/uikit/nsmutableparagraphstyle/allowsdefaulttighteningfortruncation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsmutableparagraphstyle/allowsdefaulttighteningfortruncation.json'
content_hash: 'sha256:5a4028aa0c5075d8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSMutableParagraphStyle](../nsmutableparagraphstyle.md)

# allowsDefaultTighteningForTruncation

<sub>Instance Property</sub>

A Boolean value that indicates whether the system tightens intercharacter spacing before truncating text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var allowsDefaultTighteningForTruncation: Bool { get set }
```

## Discussion

When this property is set to [true](../../swift/true.md), the system tries to reduce the space between characters before truncating characters. The system performs this tightening in cases where the text would not otherwise fit in the available space. The maximum amount of tightening performed by the system is dependent on the font, line width, and other factors.

The default value of this property is [false](../../swift/false.md).

## See Also

### Setting line-break information

- [lineBreakMode](linebreakmode.md) — The mode for breaking lines in the paragraph.
- [lineBreakStrategy](linebreakstrategy.md) — The strategies that the text system may use to break lines while laying out the paragraph.
- [hyphenationFactor](hyphenationfactor.md) — The paragraph’s threshold for hyphenation.
- [usesDefaultHyphenation](usesdefaulthyphenation.md) — A Boolean value that indicates whether the paragraph style uses the system hyphenation settings.
- [tighteningFactorForTruncation](../../appkit/nsmutableparagraphstyle/tighteningfactorfortruncation.md) — The threshold for using tightening as an alternative to truncation.
