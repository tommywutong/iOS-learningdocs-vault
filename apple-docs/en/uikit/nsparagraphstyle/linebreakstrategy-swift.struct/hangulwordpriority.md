---
title: hangulWordPriority
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsparagraphstyle/linebreakstrategy-swift.struct/hangulwordpriority
source_url: 'https://developer.apple.com/documentation/uikit/nsparagraphstyle/linebreakstrategy-swift.struct/hangulwordpriority'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsparagraphstyle/linebreakstrategy-swift.struct/hangulwordpriority.json'
content_hash: 'sha256:5c08e8266bfebe1d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [NSParagraphStyle](../../nsparagraphstyle.md) · [LineBreakStrategy](../linebreakstrategy-swift.struct.md)

# hangulWordPriority

<sub>Type Property</sub>

The text system prohibits breaking between Hangul characters.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
static var hangulWordPriority: NSParagraphStyle.LineBreakStrategy { get }
```

## Discussion

To avoid breaking between Hangul characters, this strategy is preferred for typesetting modern Korean documents that display UI strings.

## See Also

### Getting the line-break styles

- [NSLineBreakStrategyPushOut](pushout.md) — The text system pushes out individual lines to avoid an orphan word on the last line of the paragraph.
- [NSLineBreakStrategyStandard](standard.md) — The text system uses the same configuration of line-break strategies that it uses for standard UI labels.
