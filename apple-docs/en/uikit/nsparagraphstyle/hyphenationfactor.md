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
doc_path: /documentation/uikit/nsparagraphstyle/hyphenationfactor
source_url: 'https://developer.apple.com/documentation/uikit/nsparagraphstyle/hyphenationfactor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsparagraphstyle/hyphenationfactor.json'
content_hash: 'sha256:38879c1f4dd0836b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSParagraphStyle](../nsparagraphstyle.md)

# hyphenationFactor

<sub>Instance Property</sub>

The paragraph’s threshold for hyphenation.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var hyphenationFactor: Float { get }
```

## Discussion

The system attempts hyphenation when the ratio of the text width (as broken without hyphenation) to the width of the line fragment is less than the hyphenation factor. When the paragraph’s hyphenation factor is `0.0`, the system uses the layout manager’s hyphenation factor instead. The system disables hyphenation when both are `0.0`. This property detects the user-selected language by examining the first item in [preferredLanguages](../../foundation/nslocale/preferredlanguages.md).

## See Also

### Related Documentation

- [kCTLanguageAttributeName](../../coretext/kctlanguageattributename.md) — The name of the text language.

### Getting line-break information

- [lineBreakMode](linebreakmode.md) — The mode for breaking lines in the paragraph that don’t fit within a container.
- [NSLineBreakMode](../nslinebreakmode.md) — Constants that specify what happens when a line is too long for a container.
- [lineBreakStrategy](linebreakstrategy-swift.property.md) — The strategy for breaking lines while laying out paragraphs.
- [LineBreakStrategy](linebreakstrategy-swift.struct.md) — Constants that specify how the text system breaks lines while laying out paragraphs.
- [usesDefaultHyphenation](usesdefaulthyphenation.md) — A Boolean value that indicates whether the paragraph style uses the system hyphenation settings.
- [tighteningFactorForTruncation](../../appkit/nsparagraphstyle/tighteningfactorfortruncation.md) — The threshold for using tightening as an alternative to truncation.
- [allowsDefaultTighteningForTruncation](allowsdefaulttighteningfortruncation.md) — A Boolean value that indicates whether the system tightens character spacing before truncating text.
