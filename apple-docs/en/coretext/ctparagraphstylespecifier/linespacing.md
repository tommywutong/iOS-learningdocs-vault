---
title: CTParagraphStyleSpecifier.lineSpacing
framework: Core Text
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 3.2+（6.0 起废弃）, iPadOS 3.2+（6.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/coretext/ctparagraphstylespecifier/linespacing
source_url: 'https://developer.apple.com/documentation/coretext/ctparagraphstylespecifier/linespacing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctparagraphstylespecifier/linespacing.json'
content_hash: 'sha256:42d711ce4d8cfb35'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Text](../../coretext.md) · [CTParagraphStyleSpecifier](../ctparagraphstylespecifier.md)

# CTParagraphStyleSpecifier.lineSpacing

<sub>Case</sub>

The space in points added between lines within the paragraph (commonly known as leading).

> [!warning] Deprecated
> See documentation for replacements

<sub>visionOS</sub>

```swift
case lineSpacing
```

## Discussion

Instead, use [kCTParagraphStyleSpecifierMaximumLineSpacing](maximumlinespacing.md), [kCTParagraphStyleSpecifierMinimumLineSpacing](minimumlinespacing.md), and [kCTParagraphStyleSpecifierLineSpacingAdjustment](linespacingadjustment.md) to control space between lines. This value is always nonnegative. Type: [CGFloat](../../corefoundation/cgfloat-swift.struct.md). Default value: `0.0`. Affects: [CTFramesetter](../ctframesetter.md).

## See Also

### Constants

- [kCTParagraphStyleSpecifierAlignment](alignment.md) — The text alignment.
- [kCTParagraphStyleSpecifierFirstLineHeadIndent](firstlineheadindent.md) — The distance, in points, from the leading margin of a frame to the beginning of the paragraph’s first line.
- [kCTParagraphStyleSpecifierHeadIndent](headindent.md) — The distance, in points, from the leading margin of a text container to the beginning of lines other than the first.
- [kCTParagraphStyleSpecifierTailIndent](tailindent.md) — The distance, in points, from the margin of a frame to the end of lines.
- [kCTParagraphStyleSpecifierTabStops](tabstops.md) — The text tab objects, sorted by location, that define the tab stops for the paragraph style.
- [kCTParagraphStyleSpecifierDefaultTabInterval](defaulttabinterval.md) — The document-wide default tab interval.
- [kCTParagraphStyleSpecifierLineBreakMode](linebreakmode.md) — The mode that should be used to break lines when laying out the paragraph’s text.
- [kCTParagraphStyleSpecifierLineHeightMultiple](lineheightmultiple.md) — The line height multiple.
- [kCTParagraphStyleSpecifierMaximumLineHeight](maximumlineheight.md) — The maximum height that any line in the frame will occupy, regardless of the font size or size of any attached graphic.
- [kCTParagraphStyleSpecifierMinimumLineHeight](minimumlineheight.md) — The minimum height that any line in the frame will occupy, regardless of the font size or size of any attached graphic.
- [kCTParagraphStyleSpecifierParagraphSpacing](paragraphspacing.md) — The space added at the end of the paragraph to separate it from the following paragraph.
- [kCTParagraphStyleSpecifierParagraphSpacingBefore](paragraphspacingbefore.md) — The distance between the paragraph’s top and the beginning of its text content.
- [kCTParagraphStyleSpecifierBaseWritingDirection](basewritingdirection.md) — The base writing direction of the lines.
- [kCTParagraphStyleSpecifierMaximumLineSpacing](maximumlinespacing.md) — The maximum space in points between lines within the paragraph (commonly known as leading).
- [kCTParagraphStyleSpecifierMinimumLineSpacing](minimumlinespacing.md) — The minimum space in points between lines within the paragraph (commonly known as leading).
