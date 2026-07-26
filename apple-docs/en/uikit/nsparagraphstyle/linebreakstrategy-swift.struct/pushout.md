---
title: pushOut
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsparagraphstyle/linebreakstrategy-swift.struct/pushout
source_url: 'https://developer.apple.com/documentation/uikit/nsparagraphstyle/linebreakstrategy-swift.struct/pushout'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsparagraphstyle/linebreakstrategy-swift.struct/pushout.json'
content_hash: 'sha256:35f5ad3d89109782'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [NSParagraphStyle](../../nsparagraphstyle.md) · [LineBreakStrategy](../linebreakstrategy-swift.struct.md)

# pushOut

<sub>Type Property</sub>

The text system pushes out individual lines to avoid an orphan word on the last line of the paragraph.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
static var pushOut: NSParagraphStyle.LineBreakStrategy { get }
```

## Discussion

To avoid an orphan word on the last line of a paragraph before a page break, the text system may extend individual lines by one or more words. Typically, the text system only pushes out the last line by one word.

## See Also

### Getting the line-break styles

- [NSLineBreakStrategyHangulWordPriority](hangulwordpriority.md) — The text system prohibits breaking between Hangul characters.
- [NSLineBreakStrategyStandard](standard.md) — The text system uses the same configuration of line-break strategies that it uses for standard UI labels.
