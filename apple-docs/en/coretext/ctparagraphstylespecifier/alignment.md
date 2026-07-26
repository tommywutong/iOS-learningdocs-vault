---
title: CTParagraphStyleSpecifier.alignment
framework: Core Text
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctparagraphstylespecifier/alignment
source_url: 'https://developer.apple.com/documentation/coretext/ctparagraphstylespecifier/alignment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctparagraphstylespecifier/alignment.json'
content_hash: 'sha256:2cb1c0b8384632d5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Text](../../coretext.md) · [CTParagraphStyleSpecifier](../ctparagraphstylespecifier.md)

# CTParagraphStyleSpecifier.alignment

<sub>Case</sub>

The text alignment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case alignment
```

## Discussion

Natural text alignment is realized as left or right alignment, depending on the line sweep direction of the first script contained in the paragraph. Type: [CTTextAlignment](../cttextalignment.md). Default value: [kCTNaturalTextAlignment](../cttextalignment/kctnaturaltextalignment.md). Affects: [CTFramesetter](../ctframesetter.md).

## See Also

### Constants

- [kCTParagraphStyleSpecifierFirstLineHeadIndent](firstlineheadindent.md) — The distance, in points, from the leading margin of a frame to the beginning of the paragraph’s first line.
- [kCTParagraphStyleSpecifierHeadIndent](headindent.md) — The distance, in points, from the leading margin of a text container to the beginning of lines other than the first.
- [kCTParagraphStyleSpecifierTailIndent](tailindent.md) — The distance, in points, from the margin of a frame to the end of lines.
- [kCTParagraphStyleSpecifierTabStops](tabstops.md) — The text tab objects, sorted by location, that define the tab stops for the paragraph style.
- [kCTParagraphStyleSpecifierDefaultTabInterval](defaulttabinterval.md) — The document-wide default tab interval.
- [kCTParagraphStyleSpecifierLineBreakMode](linebreakmode.md) — The mode that should be used to break lines when laying out the paragraph’s text.
- [kCTParagraphStyleSpecifierLineHeightMultiple](lineheightmultiple.md) — The line height multiple.
- [kCTParagraphStyleSpecifierMaximumLineHeight](maximumlineheight.md) — The maximum height that any line in the frame will occupy, regardless of the font size or size of any attached graphic.
- [kCTParagraphStyleSpecifierMinimumLineHeight](minimumlineheight.md) — The minimum height that any line in the frame will occupy, regardless of the font size or size of any attached graphic.
- [kCTParagraphStyleSpecifierLineSpacing](linespacing.md) — The space in points added between lines within the paragraph (commonly known as leading). _(deprecated)_
- [kCTParagraphStyleSpecifierParagraphSpacing](paragraphspacing.md) — The space added at the end of the paragraph to separate it from the following paragraph.
- [kCTParagraphStyleSpecifierParagraphSpacingBefore](paragraphspacingbefore.md) — The distance between the paragraph’s top and the beginning of its text content.
- [kCTParagraphStyleSpecifierBaseWritingDirection](basewritingdirection.md) — The base writing direction of the lines.
- [kCTParagraphStyleSpecifierMaximumLineSpacing](maximumlinespacing.md) — The maximum space in points between lines within the paragraph (commonly known as leading).
- [kCTParagraphStyleSpecifierMinimumLineSpacing](minimumlinespacing.md) — The minimum space in points between lines within the paragraph (commonly known as leading).
