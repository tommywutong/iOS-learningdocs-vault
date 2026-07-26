---
title: hyphenationFactor
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsmutableparagraphstyle/hyphenationfactor
source_url: 'https://developer.apple.com/documentation/uikit/nsmutableparagraphstyle/hyphenationfactor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsmutableparagraphstyle/hyphenationfactor.json'
content_hash: 'sha256:d2ec8fd243b862f0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSMutableParagraphStyle](../nsmutableparagraphstyle.md)

# hyphenationFactor

<sub>Instance Property</sub>

The paragraph’s threshold for hyphenation.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var hyphenationFactor: Float { get set }
```

## Discussion

Valid values lie between `0.0` and `1.0` inclusive. The default value is `0.0`. Hyphenation is attempted when the ratio of the text width (as broken without hyphenation) to the width of the line fragment is less than the hyphenation factor. When the paragraph’s hyphenation factor is `0.0`, the layout manager’s hyphenation factor is used instead. When both are `0.0`, hyphenation is disabled. This property detects the user-selected language by examining the first item in `preferredLanguages`.

## See Also

### Related Documentation

- [kCTLanguageAttributeName](../../coretext/kctlanguageattributename.md) — The name of the text language.

### Setting line-break information

- [lineBreakMode](linebreakmode.md) — The mode for breaking lines in the paragraph.
- [lineBreakStrategy](linebreakstrategy.md) — The strategies that the text system may use to break lines while laying out the paragraph.
- [usesDefaultHyphenation](usesdefaulthyphenation.md) — A Boolean value that indicates whether the paragraph style uses the system hyphenation settings.
- [tighteningFactorForTruncation](../../appkit/nsmutableparagraphstyle/tighteningfactorfortruncation.md) — The threshold for using tightening as an alternative to truncation.
- [allowsDefaultTighteningForTruncation](allowsdefaulttighteningfortruncation.md) — A Boolean value that indicates whether the system tightens intercharacter spacing before truncating text.
