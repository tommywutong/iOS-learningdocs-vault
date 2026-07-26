---
title: NSLineBreakMode
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nslinebreakmode
source_url: 'https://developer.apple.com/documentation/uikit/nslinebreakmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslinebreakmode.json'
content_hash: 'sha256:b2efa961723a9703'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSLineBreakMode

<sub>Enumeration</sub>

Constants that specify what happens when a line is too long for a container.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
enum NSLineBreakMode
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [NSLineBreakByWordWrapping](nslinebreakmode/bywordwrapping.md) — The value that indicates wrapping occurs at word boundaries, unless the word doesn’t fit on a single line.
- [NSLineBreakByCharWrapping](nslinebreakmode/bycharwrapping.md) — The value that indicates wrapping occurs before the first character that doesn’t fit.
- [NSLineBreakByClipping](nslinebreakmode/byclipping.md) — The value that indicates lines don’t extend past the edge of the text container.
- [NSLineBreakByTruncatingHead](nslinebreakmode/bytruncatinghead.md) — The value that indicates that a line displays so that the end fits in the container and an ellipsis glyph indicates the missing text at the beginning of the line.
- [NSLineBreakByTruncatingTail](nslinebreakmode/bytruncatingtail.md) — The value that indicates a line displays so that the beginning fits in the container and an ellipsis glyph indicates the missing text at the end of the line.
- [NSLineBreakByTruncatingMiddle](nslinebreakmode/bytruncatingmiddle.md) — The value that indicates that a line displays so that the beginning and end fit in the container and an ellipsis glyph indicates the missing text in the middle.

### Initializers

- [init(rawValue:)](<nslinebreakmode/init(rawvalue_).md>)

## See Also

### Getting line-break information

- [lineBreakMode](nsparagraphstyle/linebreakmode.md) — The mode for breaking lines in the paragraph that don’t fit within a container.
- [lineBreakStrategy](nsparagraphstyle/linebreakstrategy-swift.property.md) — The strategy for breaking lines while laying out paragraphs.
- [LineBreakStrategy](nsparagraphstyle/linebreakstrategy-swift.struct.md) — Constants that specify how the text system breaks lines while laying out paragraphs.
- [hyphenationFactor](nsparagraphstyle/hyphenationfactor.md) — The paragraph’s threshold for hyphenation.
- [usesDefaultHyphenation](nsparagraphstyle/usesdefaulthyphenation.md) — A Boolean value that indicates whether the paragraph style uses the system hyphenation settings.
- [tighteningFactorForTruncation](../appkit/nsparagraphstyle/tighteningfactorfortruncation.md) — The threshold for using tightening as an alternative to truncation.
- [allowsDefaultTighteningForTruncation](nsparagraphstyle/allowsdefaulttighteningfortruncation.md) — A Boolean value that indicates whether the system tightens character spacing before truncating text.
