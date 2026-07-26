---
title: CTLine
framework: Core Text
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctline
source_url: 'https://developer.apple.com/documentation/coretext/ctline'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctline.json'
content_hash: 'sha256:11df3036977e0164'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTLine

<sub>Class</sub>

A line of text.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CTLine
```

## Overview

A `CTLine` object contains an array of glyph runs. Line objects are created by the typesetter during a framesetting operation and can draw themselves directly into a graphics context.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Creating Lines

- [CTLineCreateWithAttributedString](<ctlinecreatewithattributedstring(__).md>) — Creates a single immutable line object from an attributed string.
- [CTLineCreateTruncatedLine](<ctlinecreatetruncatedline(________).md>) — Creates a truncated line from an existing line.
- [CTLineCreateJustifiedLine](<ctlinecreatejustifiedline(______).md>) — Creates a justified line from an existing line.

### Drawing the Line

- [CTLineDraw](<ctlinedraw(____).md>) — Draws a complete line.

### Getting Line Data

- [CTLineGetGlyphCount](<ctlinegetglyphcount(__).md>) — Returns the total glyph count for the line object.
- [CTLineGetGlyphRuns](<ctlinegetglyphruns(__).md>) — Returns the array of glyph runs that make up the line object.
- [CTLineGetStringRange](<ctlinegetstringrange(__).md>) — Gets the range of characters that originally spawned the glyphs in the line.
- [CTLineGetPenOffsetForFlush](<ctlinegetpenoffsetforflush(______).md>) — Gets the pen offset required to draw flush text.

### Measuring Lines

- [CTLineGetImageBounds](<ctlinegetimagebounds(____).md>) — Calculates the image bounds for a line.
- [CTLineGetTypographicBounds](<ctlinegettypographicbounds(________).md>) — Calculates the typographic bounds of a line.
- [CTLineGetTrailingWhitespaceWidth](<ctlinegettrailingwhitespacewidth(__).md>) — Returns the trailing whitespace width for a line.

### Getting Line Positioning

- [CTLineGetStringIndexForPosition](<ctlinegetstringindexforposition(____).md>) — Performs hit testing.
- [CTLineGetOffsetForStringIndex](<ctlinegetoffsetforstringindex(______).md>) — Determines the graphical offset or offsets for a string index.
- [CTLineEnumerateCaretOffsets](<ctlineenumeratecaretoffsets(____).md>) — Enumerates caret offsets for characters in a line.

### Getting the Type Identifier

- [CTLineGetTypeID](<ctlinegettypeid().md>) — Returns the Core Foundation type identifier of the line object.

### Constants

- [CTLineTruncationType](ctlinetruncationtype.md) — Truncation types required by the [CTLineCreateTruncatedLine](<ctlinecreatetruncatedline(________).md>) function to tell the truncation engine which type of truncation is being requested.

## See Also

### Opaque Types

- [CTFont](ctfont.md) — A font object.
- [CTFontCollection](ctfontcollection.md) — A font collection.
- [CTFontDescriptor](ctfontdescriptor.md) — A font descriptor.
- [CTFrame](ctframe.md) — A frame.
- [CTFramesetter](ctframesetter.md) — Generate text frames.
- [CTGlyphInfo](ctglyphinfo.md) — Override a font’s specified mapping from Unicode to the glyph ID.
- [CTParagraphStyle](ctparagraphstyle.md) — Paragraph or ruler attributes in an attributed string.
- [CTRun](ctrun.md) — A glyph run.
- [CTRunDelegate](ctrundelegate.md) — A run delegate.
- [CTTextTab](cttexttab.md) — A tab in a paragraph style, storing an alignment type and location.
- [CTTypesetter](cttypesetter.md) — A typesetter which performs line layout.
