---
title: CTParagraphStyle
framework: Core Text
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctparagraphstyle
source_url: 'https://developer.apple.com/documentation/coretext/ctparagraphstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctparagraphstyle.json'
content_hash: 'sha256:5df54ffe1e72eeb5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTParagraphStyle

<sub>Class</sub>

Paragraph or ruler attributes in an attributed string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CTParagraphStyle
```

## Overview

A paragraph style object represents a complex attribute value in an attributed string, storing a number of subattributes that affect paragraph layout for the characters of the string. Among these subattributes are alignment, tab stops, writing direction, line-breaking mode, and indentation settings.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Creating Paragraph Styles

- [CTParagraphStyleCreate](<ctparagraphstylecreate(____).md>) — Creates an immutable paragraph style.
- [CTParagraphStyleCreateCopy](<ctparagraphstylecreatecopy(__).md>) — Creates an immutable copy of a paragraph style.

### Getting the Value of a Style Specifier

- [CTParagraphStyleGetValueForSpecifier](<ctparagraphstylegetvalueforspecifier(________).md>) — Obtains the current value for a single setting specifier.

### Getting the Type Identifier

- [CTParagraphStyleGetTypeID](<ctparagraphstylegettypeid().md>) — Returns the Core Foundation type identifier of the paragraph style object.

### Data Types

- [CTParagraphStyleSetting](ctparagraphstylesetting.md) — This structure is used to alter the paragraph style.

### Constants

- [CTTextAlignment](cttextalignment.md) — Constants that specify text alignment.
- [CTLineBreakMode](ctlinebreakmode.md) — These constants specify what happens when a line is too long for its frame.
- [CTWritingDirection](ctwritingdirection.md) — These constants specify the writing direction.
- [CTParagraphStyleSpecifier](ctparagraphstylespecifier.md) — Constants used to query and modify a paragraph style object.

## See Also

### Opaque Types

- [CTFont](ctfont.md) — A font object.
- [CTFontCollection](ctfontcollection.md) — A font collection.
- [CTFontDescriptor](ctfontdescriptor.md) — A font descriptor.
- [CTFrame](ctframe.md) — A frame.
- [CTFramesetter](ctframesetter.md) — Generate text frames.
- [CTGlyphInfo](ctglyphinfo.md) — Override a font’s specified mapping from Unicode to the glyph ID.
- [CTLine](ctline.md) — A line of text.
- [CTRun](ctrun.md) — A glyph run.
- [CTRunDelegate](ctrundelegate.md) — A run delegate.
- [CTTextTab](cttexttab.md) — A tab in a paragraph style, storing an alignment type and location.
- [CTTypesetter](cttypesetter.md) — A typesetter which performs line layout.
