---
title: CTFramesetter
framework: Core Text
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctframesetter
source_url: 'https://developer.apple.com/documentation/coretext/ctframesetter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctframesetter.json'
content_hash: 'sha256:2517ee14571a90ea'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFramesetter

<sub>Class</sub>

Generate text frames.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CTFramesetter
```

## Overview

`CTFramesetter` is an object factory for [CTFrame](ctframe.md) objects.

The framesetter takes an attributed string object and a shape descriptor object and calls into the typesetter to create line objects that fill that shape. The output is a frame object containing an array of lines. The frame can then draw itself directly into the current graphic context.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Creating a Framesetter

- [CTFramesetterCreateWithAttributedString](<ctframesettercreatewithattributedstring(__).md>) — Creates an immutable framesetter object from an attributed string.
- [CTFramesetterCreateWithTypesetter](<ctframesettercreatewithtypesetter(__).md>) — Creates a framesetter directly from a typesetter.

### Creating Frames

- [CTFramesetterCreateFrame](<ctframesettercreateframe(________).md>) — Creates an immutable frame using a framesetter.
- [CTFramesetterGetTypesetter](<ctframesettergettypesetter(__).md>) — Returns the typesetter object being used by the framesetter.

### Frame Sizing

- [CTFramesetterSuggestFrameSizeWithConstraints](<ctframesettersuggestframesizewithconstraints(__________).md>) — Determines the frame size needed for a string range.

### Getting the Type Identifier

- [CTFramesetterGetTypeID](<ctframesettergettypeid().md>) — Returns the Core Foundation type identifier of the framesetter object.

## See Also

### Opaque Types

- [CTFont](ctfont.md) — A font object.
- [CTFontCollection](ctfontcollection.md) — A font collection.
- [CTFontDescriptor](ctfontdescriptor.md) — A font descriptor.
- [CTFrame](ctframe.md) — A frame.
- [CTGlyphInfo](ctglyphinfo.md) — Override a font’s specified mapping from Unicode to the glyph ID.
- [CTLine](ctline.md) — A line of text.
- [CTParagraphStyle](ctparagraphstyle.md) — Paragraph or ruler attributes in an attributed string.
- [CTRun](ctrun.md) — A glyph run.
- [CTRunDelegate](ctrundelegate.md) — A run delegate.
- [CTTextTab](cttexttab.md) — A tab in a paragraph style, storing an alignment type and location.
- [CTTypesetter](cttypesetter.md) — A typesetter which performs line layout.
