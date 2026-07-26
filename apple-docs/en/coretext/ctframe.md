---
title: CTFrame
framework: Core Text
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctframe
source_url: 'https://developer.apple.com/documentation/coretext/ctframe'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctframe.json'
content_hash: 'sha256:2c8f9a7ae8307622'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFrame

<sub>Class</sub>

A frame.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CTFrame
```

## Overview

A frame contains multiple lines of text. The frame object is the output resulting from the text-framing process performed by a [CTFramesetter](ctframesetter.md) object.

You can draw the entire text frame directly into the current graphic context. The frame object contains an array of line objects that can be retrieved for individual rendering or to get glyph information.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Getting Frame Data

- [CTFrameGetStringRange](<ctframegetstringrange(__).md>) — Returns the range of characters originally requested to fill the frame.
- [CTFrameGetVisibleStringRange](<ctframegetvisiblestringrange(__).md>) — Returns the range of characters that actually fit in the frame.
- [CTFrameGetPath](<ctframegetpath(__).md>) — Returns the path used to create the frame.
- [CTFrameGetFrameAttributes](<ctframegetframeattributes(__).md>) — Returns the frame attributes used to create the frame.

### Getting Lines

- [CTFrameGetLines](<ctframegetlines(__).md>) — Returns an array of lines stored in the frame.
- [CTFrameGetLineOrigins](<ctframegetlineorigins(______).md>) — Copies a range of line origins for a frame.

### Drawing the Frame

- [CTFrameDraw](<ctframedraw(____).md>) — Draws an entire frame into a context.

### Getting the Type Identifier

- [CTFrameGetTypeID](<ctframegettypeid().md>) — Returns the type identifier for the CTFrame opaque type.

### Data Types

- [CTFramePathFillRule](ctframepathfillrule.md) — These constants specify the fill rule used by a frame

### Constants

- [CTFrameProgression](ctframeprogression.md) — Constants that specify frame progression types.
- [kCTFrameProgressionAttributeName](kctframeprogressionattributename.md) — Specifies progression for a frame.
- [kCTFramePathFillRuleAttributeName](kctframepathfillruleattributename.md) — The key used to specify the fill rule for a frame.
- [kCTFramePathWidthAttributeName](kctframepathwidthattributename.md) — The key used to specify the frame width.
- [kCTFrameClippingPathsAttributeName](kctframeclippingpathsattributename.md) — Specifies array of paths to clip frame.
- [kCTFramePathClippingPathAttributeName](kctframepathclippingpathattributename.md) — Specifies clipping path.

## See Also

### Opaque Types

- [CTFont](ctfont.md) — A font object.
- [CTFontCollection](ctfontcollection.md) — A font collection.
- [CTFontDescriptor](ctfontdescriptor.md) — A font descriptor.
- [CTFramesetter](ctframesetter.md) — Generate text frames.
- [CTGlyphInfo](ctglyphinfo.md) — Override a font’s specified mapping from Unicode to the glyph ID.
- [CTLine](ctline.md) — A line of text.
- [CTParagraphStyle](ctparagraphstyle.md) — Paragraph or ruler attributes in an attributed string.
- [CTRun](ctrun.md) — A glyph run.
- [CTRunDelegate](ctrundelegate.md) — A run delegate.
- [CTTextTab](cttexttab.md) — A tab in a paragraph style, storing an alignment type and location.
- [CTTypesetter](cttypesetter.md) — A typesetter which performs line layout.
