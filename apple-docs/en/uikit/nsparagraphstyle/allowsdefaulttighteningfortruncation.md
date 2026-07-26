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
doc_path: /documentation/uikit/nsparagraphstyle/allowsdefaulttighteningfortruncation
source_url: 'https://developer.apple.com/documentation/uikit/nsparagraphstyle/allowsdefaulttighteningfortruncation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsparagraphstyle/allowsdefaulttighteningfortruncation.json'
content_hash: 'sha256:affca0128abc6928'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSParagraphStyle](../nsparagraphstyle.md)

# allowsDefaultTighteningForTruncation

<sub>Instance Property</sub>

A Boolean value that indicates whether the system tightens character spacing before truncating text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var allowsDefaultTighteningForTruncation: Bool { get }
```

## Discussion

When this property is [true](../../swift/true.md), the system tries to reduce the space between characters before truncating characters. The system performs this tightening in cases where the text wouldn’t otherwise fit in the available space. The maximum amount of tightening performed by the system is dependent on the font, line width, and other factors.

The default value of this property is [false](../../swift/false.md).

## See Also

### Getting line-break information

- [lineBreakMode](linebreakmode.md) — The mode for breaking lines in the paragraph that don’t fit within a container.
- [NSLineBreakMode](../nslinebreakmode.md) — Constants that specify what happens when a line is too long for a container.
- [lineBreakStrategy](linebreakstrategy-swift.property.md) — The strategy for breaking lines while laying out paragraphs.
- [LineBreakStrategy](linebreakstrategy-swift.struct.md) — Constants that specify how the text system breaks lines while laying out paragraphs.
- [hyphenationFactor](hyphenationfactor.md) — The paragraph’s threshold for hyphenation.
- [usesDefaultHyphenation](usesdefaulthyphenation.md) — A Boolean value that indicates whether the paragraph style uses the system hyphenation settings.
- [tighteningFactorForTruncation](../../appkit/nsparagraphstyle/tighteningfactorfortruncation.md) — The threshold for using tightening as an alternative to truncation.
