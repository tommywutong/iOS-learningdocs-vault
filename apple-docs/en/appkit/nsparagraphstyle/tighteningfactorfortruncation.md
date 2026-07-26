---
title: tighteningFactorForTruncation
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nsparagraphstyle/tighteningfactorfortruncation
source_url: 'https://developer.apple.com/documentation/appkit/nsparagraphstyle/tighteningfactorfortruncation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nsparagraphstyle/tighteningfactorfortruncation.json'
content_hash: 'sha256:a29f79d9758e50d1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSParagraphStyle](../nsparagraphstyle.md)

# tighteningFactorForTruncation

<sub>Instance Property</sub>

The threshold for using tightening as an alternative to truncation.

<sub>macOS</sub>

```swift
var tighteningFactorForTruncation: Float { get }
```

## Discussion

When the line break mode specifies truncation, the text system attempts to tighten character spacing as an alternative to truncation. Provided that the ratio of the text width to the line fragment width doesn’t exceed `1.0` + the system sets the tightening factor to this property. Otherwise, the system truncates the text at a location determined by the line break mode.

## See Also

### Getting line-break information

- [lineBreakMode](linebreakmode.md) — The mode for breaking lines in the paragraph that don’t fit within a container.
- [NSLineBreakMode](../nslinebreakmode.md) — Constants that specify what happens when a line is too long for a container.
- [lineBreakStrategy](linebreakstrategy-swift.property.md) — The strategy for breaking lines while laying out paragraphs.
- [LineBreakStrategy](linebreakstrategy-swift.struct.md) — Constants that specify how the text system breaks lines while laying out paragraphs.
- [hyphenationFactor](hyphenationfactor.md) — The paragraph’s threshold for hyphenation.
- [usesDefaultHyphenation](usesdefaulthyphenation.md) — A Boolean value that indicates whether the paragraph style uses the system hyphenation settings.
- [allowsDefaultTighteningForTruncation](allowsdefaulttighteningfortruncation.md) — A Boolean value that indicates whether the system tightens character spacing before truncating text.
