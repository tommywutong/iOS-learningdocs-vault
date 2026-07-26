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
doc_path: /documentation/uikit/nsparagraphstyle/usesdefaulthyphenation
source_url: 'https://developer.apple.com/documentation/uikit/nsparagraphstyle/usesdefaulthyphenation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsparagraphstyle/usesdefaulthyphenation.json'
content_hash: 'sha256:cb62b87c55a97409'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSParagraphStyle](../nsparagraphstyle.md)

# usesDefaultHyphenation

<sub>Instance Property</sub>

A Boolean value that indicates whether the paragraph style uses the system hyphenation settings.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var usesDefaultHyphenation: Bool { get }
```

## See Also

### Getting line-break information

- [lineBreakMode](linebreakmode.md) — The mode for breaking lines in the paragraph that don’t fit within a container.
- [NSLineBreakMode](../nslinebreakmode.md) — Constants that specify what happens when a line is too long for a container.
- [lineBreakStrategy](linebreakstrategy-swift.property.md) — The strategy for breaking lines while laying out paragraphs.
- [LineBreakStrategy](linebreakstrategy-swift.struct.md) — Constants that specify how the text system breaks lines while laying out paragraphs.
- [hyphenationFactor](hyphenationfactor.md) — The paragraph’s threshold for hyphenation.
- [tighteningFactorForTruncation](../../appkit/nsparagraphstyle/tighteningfactorfortruncation.md) — The threshold for using tightening as an alternative to truncation.
- [allowsDefaultTighteningForTruncation](allowsdefaulttighteningfortruncation.md) — A Boolean value that indicates whether the system tightens character spacing before truncating text.
