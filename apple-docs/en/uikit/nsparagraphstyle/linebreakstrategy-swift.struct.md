---
title: NSParagraphStyle.LineBreakStrategy
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsparagraphstyle/linebreakstrategy-swift.struct
source_url: 'https://developer.apple.com/documentation/uikit/nsparagraphstyle/linebreakstrategy-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsparagraphstyle/linebreakstrategy-swift.struct.json'
content_hash: 'sha256:d99a8c11bd372f6d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSParagraphStyle](../nsparagraphstyle.md)

# NSParagraphStyle.LineBreakStrategy

<sub>Structure</sub>

Constants that specify how the text system breaks lines while laying out paragraphs.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
struct LineBreakStrategy
```

## Overview

Line break strategy describes a collection of options that can affect where line breaks are placed in a paragraph. This is independent from line break mode, which describes what happens when text is too long to fit within its container. These options won’t have any effect when used with line break modes that don’t support multiple lines, like clipping or truncating middle.

Constants that specify how the text system breaks lines while laying out paragraphs.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Getting the line-break styles

- [NSLineBreakStrategyPushOut](linebreakstrategy-swift.struct/pushout.md) — The text system pushes out individual lines to avoid an orphan word on the last line of the paragraph.
- [NSLineBreakStrategyHangulWordPriority](linebreakstrategy-swift.struct/hangulwordpriority.md) — The text system prohibits breaking between Hangul characters.
- [NSLineBreakStrategyStandard](linebreakstrategy-swift.struct/standard.md) — The text system uses the same configuration of line-break strategies that it uses for standard UI labels.

### Creating a line-break style

- [init(rawValue:)](<linebreakstrategy-swift.struct/init(rawvalue_).md>) — Creates a line-break strategy with the specified raw value.

## See Also

### Getting line-break information

- [lineBreakMode](linebreakmode.md) — The mode for breaking lines in the paragraph that don’t fit within a container.
- [NSLineBreakMode](../nslinebreakmode.md) — Constants that specify what happens when a line is too long for a container.
- [lineBreakStrategy](linebreakstrategy-swift.property.md) — The strategy for breaking lines while laying out paragraphs.
- [hyphenationFactor](hyphenationfactor.md) — The paragraph’s threshold for hyphenation.
- [usesDefaultHyphenation](usesdefaulthyphenation.md) — A Boolean value that indicates whether the paragraph style uses the system hyphenation settings.
- [tighteningFactorForTruncation](../../appkit/nsparagraphstyle/tighteningfactorfortruncation.md) — The threshold for using tightening as an alternative to truncation.
- [allowsDefaultTighteningForTruncation](allowsdefaulttighteningfortruncation.md) — A Boolean value that indicates whether the system tightens character spacing before truncating text.
