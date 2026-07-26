---
title: CTGlyphInfo
framework: Core Text
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctglyphinfo
source_url: 'https://developer.apple.com/documentation/coretext/ctglyphinfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctglyphinfo.json'
content_hash: 'sha256:84116eb0c033a145'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTGlyphInfo

<sub>Class</sub>

Override a font’s specified mapping from Unicode to the glyph ID.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CTGlyphInfo
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Getting the GlyphInfo Type

- [CTGlyphInfoGetTypeID](<ctglyphinfogettypeid().md>) — Returns the Core Foundation type identifier of the glyph info object

### Creating GlyphInfo Objects

- [CTGlyphInfoCreateWithGlyphName](<ctglyphinfocreatewithglyphname(______).md>) — Creates an immutable glyph info object with a glyph name.
- [CTGlyphInfoCreateWithGlyph](<ctglyphinfocreatewithglyph(______).md>) — Creates an immutable glyph info object with a glyph index.
- [CTGlyphInfoCreateWithCharacterIdentifier](<ctglyphinfocreatewithcharacteridentifier(______).md>) — Creates an immutable glyph info object with a character identifier.

### Getting GlyphInfo Data

- [CTGlyphInfoGetGlyphName](<ctglyphinfogetglyphname(__).md>) — Retrieves the glyph name for a glyph info object, if that object exists.
- [CTGlyphInfoGetCharacterIdentifier](<ctglyphinfogetcharacteridentifier(__).md>) — Gets the character identifier for a glyph info object.
- [CTGlyphInfoGetCharacterCollection](<ctglyphinfogetcharactercollection(__).md>) — Gets the character collection for a glyph info object.
- [CTGlyphInfoGetGlyph](<ctglyphinfogetglyph(__).md>) — Retrieves the glyph for a glyph info, if that object exists.

### Constants

- [CTCharacterCollection](ctcharactercollection.md) — Constants that specify character collections.

## See Also

### Opaque Types

- [CTFont](ctfont.md) — A font object.
- [CTFontCollection](ctfontcollection.md) — A font collection.
- [CTFontDescriptor](ctfontdescriptor.md) — A font descriptor.
- [CTFrame](ctframe.md) — A frame.
- [CTFramesetter](ctframesetter.md) — Generate text frames.
- [CTLine](ctline.md) — A line of text.
- [CTParagraphStyle](ctparagraphstyle.md) — Paragraph or ruler attributes in an attributed string.
- [CTRun](ctrun.md) — A glyph run.
- [CTRunDelegate](ctrundelegate.md) — A run delegate.
- [CTTextTab](cttexttab.md) — A tab in a paragraph style, storing an alignment type and location.
- [CTTypesetter](cttypesetter.md) — A typesetter which performs line layout.
