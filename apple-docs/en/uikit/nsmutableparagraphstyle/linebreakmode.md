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
doc_path: /documentation/uikit/nsmutableparagraphstyle/linebreakmode
source_url: 'https://developer.apple.com/documentation/uikit/nsmutableparagraphstyle/linebreakmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsmutableparagraphstyle/linebreakmode.json'
content_hash: 'sha256:c5bd5df364629e7d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSMutableParagraphStyle](../nsmutableparagraphstyle.md)

# lineBreakMode

<sub>Instance Property</sub>

The mode for breaking lines in the paragraph.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var lineBreakMode: NSLineBreakMode { get set }
```

## Discussion

This property controls how the text system lays out lines that don’t fit in its container, such as by truncating with an ellipsis (…) or clipping the text. This is different from [LineBreakStrategy](../nsparagraphstyle/linebreakstrategy-swift.struct.md), which controls where the system places line breaks in a paragraph.

## See Also

### Setting line-break information

- [lineBreakStrategy](linebreakstrategy.md) — The strategies that the text system may use to break lines while laying out the paragraph.
- [hyphenationFactor](hyphenationfactor.md) — The paragraph’s threshold for hyphenation.
- [usesDefaultHyphenation](usesdefaulthyphenation.md) — A Boolean value that indicates whether the paragraph style uses the system hyphenation settings.
- [tighteningFactorForTruncation](../../appkit/nsmutableparagraphstyle/tighteningfactorfortruncation.md) — The threshold for using tightening as an alternative to truncation.
- [allowsDefaultTighteningForTruncation](allowsdefaulttighteningfortruncation.md) — A Boolean value that indicates whether the system tightens intercharacter spacing before truncating text.
