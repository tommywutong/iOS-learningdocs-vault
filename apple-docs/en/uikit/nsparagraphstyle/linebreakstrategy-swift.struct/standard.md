---
title: standard
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsparagraphstyle/linebreakstrategy-swift.struct/standard
source_url: 'https://developer.apple.com/documentation/uikit/nsparagraphstyle/linebreakstrategy-swift.struct/standard'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsparagraphstyle/linebreakstrategy-swift.struct/standard.json'
content_hash: 'sha256:9987c1817259b42c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [NSParagraphStyle](../../nsparagraphstyle.md) · [LineBreakStrategy](../linebreakstrategy-swift.struct.md)

# standard

<sub>Type Property</sub>

The text system uses the same configuration of line-break strategies that it uses for standard UI labels.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
static var standard: NSParagraphStyle.LineBreakStrategy { get }
```

## Discussion

This strategy optimizes for displaying shorter strings that are common in UI labels. This strategy may be unsuitable for large amounts of text.

## See Also

### Getting the line-break styles

- [NSLineBreakStrategyPushOut](pushout.md) — The text system pushes out individual lines to avoid an orphan word on the last line of the paragraph.
- [NSLineBreakStrategyHangulWordPriority](hangulwordpriority.md) — The text system prohibits breaking between Hangul characters.
