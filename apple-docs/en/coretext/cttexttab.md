---
title: CTTextTab
framework: Core Text
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/cttexttab
source_url: 'https://developer.apple.com/documentation/coretext/cttexttab'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/cttexttab.json'
content_hash: 'sha256:95b3ac24b161ac1a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTTextTab

<sub>Class</sub>

A tab in a paragraph style, storing an alignment type and location.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CTTextTab
```

## Overview

Core Text supports five alignment types: [kCTTextAlignmentLeft](cttextalignment/left.md), [kCTTextAlignmentCenter](cttextalignment/center.md), [kCTTextAlignmentRight](cttextalignment/right.md), [kCTTextAlignmentJustified](cttextalignment/justified.md) and [kCTTextAlignmentNatural](cttextalignment/natural.md). These alignment types are absolute, not based on the line sweep direction of text.

For example, tabbed text is always positioned to the left of a right-aligned tab, whether the line sweep direction is left to right or right to left. A tab’s location, on the other hand, is relative to the back margin. A tab set at 1.5 inches, for example, is at 1.5 inches from the right in right-to-left text.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Creating Text Tabs

- [CTTextTabCreate](<cttexttabcreate(______).md>) — Creates and initializes a new text tab object.
- [kCTTabColumnTerminatorsAttributeName](kcttabcolumnterminatorsattributename.md) — Specifies the terminating character for a tab column.

### Getting Text Tab Data

- [CTTextTabGetAlignment](<cttexttabgetalignment(__).md>) — Returns the text alignment of the tab.
- [CTTextTabGetLocation](<cttexttabgetlocation(__).md>) — Returns the tab’s ruler location.
- [CTTextTabGetOptions](<cttexttabgetoptions(__).md>) — Returns the dictionary of attributes associated with the tab.

### Getting the Type Identifier

- [CTTextTabGetTypeID](<cttexttabgettypeid().md>) — Returns the Core Foundation type identifier of the text tab object.

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
- [CTTypesetter](cttypesetter.md) — A typesetter which performs line layout.
