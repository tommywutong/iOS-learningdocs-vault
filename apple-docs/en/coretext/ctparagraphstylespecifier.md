---
title: CTParagraphStyleSpecifier
framework: Core Text
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctparagraphstylespecifier
source_url: 'https://developer.apple.com/documentation/coretext/ctparagraphstylespecifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctparagraphstylespecifier.json'
content_hash: 'sha256:29eb889c8f719433'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTParagraphStyleSpecifier

<sub>Enumeration</sub>

Constants used to query and modify a paragraph style object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum CTParagraphStyleSpecifier
```

## Overview

Each specifier has a type and a default value associated with it. The type must always be observed when setting or fetching the value from the `CTParagraphStyle` object. In addition, some specifiers affect the behavior of both the framesetter and the typesetter, and others affect the behavior of only the framesetter, as noted in the constant descriptions.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kCTParagraphStyleSpecifierAlignment](ctparagraphstylespecifier/alignment.md) — The text alignment.
- [kCTParagraphStyleSpecifierFirstLineHeadIndent](ctparagraphstylespecifier/firstlineheadindent.md) — The distance, in points, from the leading margin of a frame to the beginning of the paragraph’s first line.
- [kCTParagraphStyleSpecifierHeadIndent](ctparagraphstylespecifier/headindent.md) — The distance, in points, from the leading margin of a text container to the beginning of lines other than the first.
- [kCTParagraphStyleSpecifierTailIndent](ctparagraphstylespecifier/tailindent.md) — The distance, in points, from the margin of a frame to the end of lines.
- [kCTParagraphStyleSpecifierTabStops](ctparagraphstylespecifier/tabstops.md) — The text tab objects, sorted by location, that define the tab stops for the paragraph style.
- [kCTParagraphStyleSpecifierDefaultTabInterval](ctparagraphstylespecifier/defaulttabinterval.md) — The document-wide default tab interval.
- [kCTParagraphStyleSpecifierLineBreakMode](ctparagraphstylespecifier/linebreakmode.md) — The mode that should be used to break lines when laying out the paragraph’s text.
- [kCTParagraphStyleSpecifierLineHeightMultiple](ctparagraphstylespecifier/lineheightmultiple.md) — The line height multiple.
- [kCTParagraphStyleSpecifierMaximumLineHeight](ctparagraphstylespecifier/maximumlineheight.md) — The maximum height that any line in the frame will occupy, regardless of the font size or size of any attached graphic.
- [kCTParagraphStyleSpecifierMinimumLineHeight](ctparagraphstylespecifier/minimumlineheight.md) — The minimum height that any line in the frame will occupy, regardless of the font size or size of any attached graphic.
- [kCTParagraphStyleSpecifierLineSpacing](ctparagraphstylespecifier/linespacing.md) — The space in points added between lines within the paragraph (commonly known as leading). _(deprecated)_
- [kCTParagraphStyleSpecifierParagraphSpacing](ctparagraphstylespecifier/paragraphspacing.md) — The space added at the end of the paragraph to separate it from the following paragraph.
- [kCTParagraphStyleSpecifierParagraphSpacingBefore](ctparagraphstylespecifier/paragraphspacingbefore.md) — The distance between the paragraph’s top and the beginning of its text content.
- [kCTParagraphStyleSpecifierBaseWritingDirection](ctparagraphstylespecifier/basewritingdirection.md) — The base writing direction of the lines.
- [kCTParagraphStyleSpecifierMaximumLineSpacing](ctparagraphstylespecifier/maximumlinespacing.md) — The maximum space in points between lines within the paragraph (commonly known as leading).
- [kCTParagraphStyleSpecifierMinimumLineSpacing](ctparagraphstylespecifier/minimumlinespacing.md) — The minimum space in points between lines within the paragraph (commonly known as leading).
- [kCTParagraphStyleSpecifierLineSpacingAdjustment](ctparagraphstylespecifier/linespacingadjustment.md) — The space in points added between lines within the paragraph (commonly known as leading).
- [kCTParagraphStyleSpecifierCount](ctparagraphstylespecifier/count.md) — The number of style specifiers.

### Enumeration Cases

- [kCTParagraphStyleSpecifierLineBoundsOptions](ctparagraphstylespecifier/lineboundsoptions.md) — Options that control the alignment of the line edges with the leading and trailing margins.

### Initializers

- [init(rawValue:)](<ctparagraphstylespecifier/init(rawvalue_).md>)

## See Also

### Constants

- [CTTextAlignment](cttextalignment.md) — Constants that specify text alignment.
- [CTLineBreakMode](ctlinebreakmode.md) — These constants specify what happens when a line is too long for its frame.
- [CTWritingDirection](ctwritingdirection.md) — These constants specify the writing direction.
