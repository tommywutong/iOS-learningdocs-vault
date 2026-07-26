---
title: lineBreakMode
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsparagraphstyle/linebreakmode
source_url: 'https://developer.apple.com/documentation/uikit/nsparagraphstyle/linebreakmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsparagraphstyle/linebreakmode.json'
content_hash: 'sha256:8af2be54248af816'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSParagraphStyle](../nsparagraphstyle.md)

# lineBreakMode

<sub>Instance Property</sub>

The mode for breaking lines in the paragraph that don’t fit within a container.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var lineBreakMode: NSLineBreakMode { get }
```

## Discussion

This property controls how the text system lays out lines that don’t fit in its container, such as by truncating with an ellipsis (…) or clipping the text. This is different from [LineBreakStrategy](linebreakstrategy-swift.struct.md), which controls where the system places line breaks in a paragraph.

## See Also

### Getting line-break information

- [NSLineBreakMode](../nslinebreakmode.md) — Constants that specify what happens when a line is too long for a container.
- [lineBreakStrategy](linebreakstrategy-swift.property.md) — The strategy for breaking lines while laying out paragraphs.
- [LineBreakStrategy](linebreakstrategy-swift.struct.md) — Constants that specify how the text system breaks lines while laying out paragraphs.
- [hyphenationFactor](hyphenationfactor.md) — The paragraph’s threshold for hyphenation.
- [usesDefaultHyphenation](usesdefaulthyphenation.md) — A Boolean value that indicates whether the paragraph style uses the system hyphenation settings.
- [tighteningFactorForTruncation](../../appkit/nsparagraphstyle/tighteningfactorfortruncation.md) — The threshold for using tightening as an alternative to truncation.
- [allowsDefaultTighteningForTruncation](allowsdefaulttighteningfortruncation.md) — A Boolean value that indicates whether the system tightens character spacing before truncating text.
