---
title: lineBreakStrategy
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsmutableparagraphstyle/linebreakstrategy
source_url: 'https://developer.apple.com/documentation/uikit/nsmutableparagraphstyle/linebreakstrategy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsmutableparagraphstyle/linebreakstrategy.json'
content_hash: 'sha256:57623418efefde2b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSMutableParagraphStyle](../nsmutableparagraphstyle.md)

# lineBreakStrategy

<sub>Instance Property</sub>

The strategies that the text system may use to break lines while laying out the paragraph.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var lineBreakStrategy: NSParagraphStyle.LineBreakStrategy { get set }
```

## Discussion

Line-break strategies are collections of options the system uses to determine where to break lines in a paragraph. This is different from [lineBreakMode](../nsparagraphstyle/linebreakmode.md), which controls how to lay out lines of text that don’t fit in a container. The system ignores this property if the paragraph style’s [lineBreakMode](../nsparagraphstyle/linebreakmode.md) property specifies a mode that doesn’t support multiple lines, such as [NSLineBreakByClipping](../nslinebreakmode/byclipping.md).

The default value is [NSLineBreakStrategyNone](../nslinebreakstrategy/nslinebreakstrategynone.md).

## See Also

### Setting line-break information

- [lineBreakMode](linebreakmode.md) — The mode for breaking lines in the paragraph.
- [hyphenationFactor](hyphenationfactor.md) — The paragraph’s threshold for hyphenation.
- [usesDefaultHyphenation](usesdefaulthyphenation.md) — A Boolean value that indicates whether the paragraph style uses the system hyphenation settings.
- [tighteningFactorForTruncation](../../appkit/nsmutableparagraphstyle/tighteningfactorfortruncation.md) — The threshold for using tightening as an alternative to truncation.
- [allowsDefaultTighteningForTruncation](allowsdefaulttighteningfortruncation.md) — A Boolean value that indicates whether the system tightens intercharacter spacing before truncating text.
