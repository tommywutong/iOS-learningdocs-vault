---
title: Core Text
framework: Core Text
symbol_kind: module
role: collection
role_heading: Framework
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext
source_url: 'https://developer.apple.com/documentation/coretext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext.json'
content_hash: 'sha256:355db39d6fc5d7b2'
translated: false
---

> Navigation: [Technologies](technologies.md)

# Core Text

<sub>Framework</sub>

Create text layouts, optimize font handling, and access font metrics and glyph data.

## Overview

Core Text provides a low-level programming interface for laying out text and handling fonts. The Core Text layout engine is designed for high performance, ease of use, and close integration with [Core Foundation](corefoundation.md). The text layout API provides high-quality typesetting, including character-to-glyph conversion, with ligatures, kerning, and so on. The complementary Core Text font technology provides automatic font substitution (cascading), font descriptors and collections, easy access to font metrics and glyph data, and many other features.

> [!note] Note
> All individual functions in Core Text are thread-safe. Font objects ([CTFont](coretext/ctfont.md), [CTFontDescriptor](coretext/ctfontdescriptor.md), and associated objects) can be used simultaneously by multiple operations, work queues, or threads. However, the layout objects ([CTTypesetter](coretext/cttypesetter.md), [CTFramesetter](coretext/ctframesetter.md), [CTRun](coretext/ctrun.md), [CTLine](coretext/ctline.md), [CTFrame](coretext/ctframe.md), and associated objects) should be used in a single operation, work queue, or thread.

## Topics

### Opaque Types

- [CTFont](coretext/ctfont.md) — A font object.
- [CTFontCollection](coretext/ctfontcollection.md) — A font collection.
- [CTFontDescriptor](coretext/ctfontdescriptor.md) — A font descriptor.
- [CTFrame](coretext/ctframe.md) — A frame.
- [CTFramesetter](coretext/ctframesetter.md) — Generate text frames.
- [CTGlyphInfo](coretext/ctglyphinfo.md) — Override a font’s specified mapping from Unicode to the glyph ID.
- [CTLine](coretext/ctline.md) — A line of text.
- [CTParagraphStyle](coretext/ctparagraphstyle.md) — Paragraph or ruler attributes in an attributed string.
- [CTRun](coretext/ctrun.md) — A glyph run.
- [CTRunDelegate](coretext/ctrundelegate.md) — A run delegate.
- [CTTextTab](coretext/cttexttab.md) — A tab in a paragraph style, storing an alignment type and location.
- [CTTypesetter](coretext/cttypesetter.md) — A typesetter which performs line layout.

### Reference

- [Styling Attributed Strings](coretext/styling-attributed-strings.md) — Attributes to which Core Text responds when placed in a `CFAttributedString` object.
- [Core Text Structures](coretext/core-text-structures.md)
- [Core Text Enumerations](coretext/core-text-enumerations.md)
- [Core Text Constants](coretext/core-text-constants.md)
- [Core Text Functions](coretext/core-text-functions.md)
- [Core Text Data Types](coretext/core-text-data-types.md)
- [SFNT Support](coretext/sfnt-support.md)

### Macros

- [Macros](coretext/coretext-macros.md)

### Classes

- [CTRubyAnnotation](coretext/ctrubyannotation.md)

### Protocols

- [CTAdaptiveImageProviding](coretext/ctadaptiveimageproviding.md)

### Variables

- [kCTFontDescriptorLanguageAttribute](coretext/kctfontdescriptorlanguageattribute.md)

### Functions

- [CTFontGetUIFontType](<coretext/ctfontgetuifonttype(__).md>)

## See Also

### Related Documentation

- [Core Text Programming Guide](https://developer.apple.com/library/archive/documentation/StringsTextFonts/Conceptual/CoreText_Programming/Introduction/Introduction.html#//apple_ref/doc/uid/TP40005533)
