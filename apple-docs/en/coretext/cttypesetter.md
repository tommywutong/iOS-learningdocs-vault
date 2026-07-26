---
title: CTTypesetter
framework: Core Text
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/cttypesetter
source_url: 'https://developer.apple.com/documentation/coretext/cttypesetter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/cttypesetter.json'
content_hash: 'sha256:a6a459276b5b92a7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTTypesetter

<sub>Class</sub>

A typesetter which performs line layout.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CTTypesetter
```

## Overview

Line layout includes word wrapping, hyphenation, and line breaking in either vertical or horizontal rectangles. A typesetter object takes as input an attributed string and produces a line of typeset glyphs (composed into glyph runs) in a [CTLine](ctline.md) object. The typesetter performs character-to-glyph encoding, glyph ordering, and positional operations, such as kerning, tracking, and baseline adjustments. If multiline layout is needed, it is performed by a [CTFramesetter](ctframesetter.md) object, which calls into the typesetter to generate the typeset lines to fill the frame.

A [CTFramesetter](ctframesetter.md) encapsulates a typesetter and provides a reference to it as a convenience, but a caller may also choose to create a freestanding typesetter.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Creating a Typesetter

- [CTTypesetterCreateWithAttributedString](<cttypesettercreatewithattributedstring(__).md>) — Creates an immutable typesetter object using an attributed string.
- [CTTypesetterCreateWithAttributedStringAndOptions](<cttypesettercreatewithattributedstringandoptions(____).md>) — Creates an immutable typesetter object using an attributed string and a dictionary of options.

### Creating Lines

- [CTTypesetterCreateLine](<cttypesettercreateline(____).md>) — Creates an immutable line from the typesetter.
- [CTTypesetterCreateLineWithOffset](<cttypesettercreatelinewithoffset(______).md>) — Creates an immutable line from the typesetter at a specified line offset.

### Breaking Lines

- [CTTypesetterSuggestLineBreak](<cttypesettersuggestlinebreak(______).md>) — Suggests a contextual line breakpoint based on the width provided.
- [CTTypesetterSuggestLineBreakWithOffset](<cttypesettersuggestlinebreakwithoffset(________).md>) — Suggests a contextual line breakpoint based on the width provided and the specified offset.
- [CTTypesetterSuggestClusterBreak](<cttypesettersuggestclusterbreak(______).md>) — Suggests a cluster line breakpoint based on the width provided.
- [CTTypesetterSuggestClusterBreakWithOffset](<cttypesettersuggestclusterbreakwithoffset(________).md>) — Suggests a cluster line breakpoint based on the specified width and line offset.

### Getting the Type Identifier

- [CTTypesetterGetTypeID](<cttypesettergettypeid().md>) — Returns the Core Foundation type identifier of the typesetter object.

### Constants

- [Typesetter Options](typesetter-options.md) — Control aspects of the typesetter’s text processing.

## See Also

### Opaque Types

- [CTFont](ctfont.md) — A font object.
- [CTFontCollection](ctfontcollection.md) — A font collection.
- [CTFontDescriptor](ctfontdescriptor.md) — A font descriptor.
- [CTFrame](ctframe.md) — A frame.
- [CTFramesetter](ctframesetter.md) — Generate text frames.
- [CTGlyphInfo](ctglyphinfo.md) — Override a font’s specified mapping from Unicode to the glyph ID.
- [CTLine](ctline.md) — A line of text.
- [CTParagraphStyle](ctparagraphstyle.md) — Paragraph or ruler attributes in an attributed string.
- [CTRun](ctrun.md) — A glyph run.
- [CTRunDelegate](ctrundelegate.md) — A run delegate.
- [CTTextTab](cttexttab.md) — A tab in a paragraph style, storing an alignment type and location.
