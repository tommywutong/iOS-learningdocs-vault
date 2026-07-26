---
title: CTRunDelegate
framework: Core Text
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctrundelegate
source_url: 'https://developer.apple.com/documentation/coretext/ctrundelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctrundelegate.json'
content_hash: 'sha256:742b4b5f833b91af'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTRunDelegate

<sub>Class</sub>

A run delegate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CTRunDelegate
```

## Overview

A run delegate is assigned to a run (attribute range) to control typographic traits such glyph ascent, glyph descent, and glyph width.

The callbacks defined for `CTRunDelegate` objects are provided by the owner of a run delegate and are used to modify glyph metrics during layout. The values returned by the delegate are applied to each glyph in the run or runs corresponding to the attribute with that delegate.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Creating a Run Delegate

- [CTRunDelegateCreate](<ctrundelegatecreate(____).md>) — Creates an immutable instance of a run delegate.

### Getting Information About a Run Delegate

- [CTRunDelegateGetRefCon](<ctrundelegategetrefcon(__).md>) — Returns a run delegate’s “refCon” value.
- [CTRunDelegateGetTypeID](<ctrundelegategettypeid().md>) — Returns the type of CTRunDelegate objects.

### Callbacks

- [CTRunDelegateGetAscentCallback](ctrundelegategetascentcallback.md) — Defines a pointer to a function that determines typographic ascent of glyphs in the run.
- [CTRunDelegateGetDescentCallback](ctrundelegategetdescentcallback.md) — Defines a pointer to a function that determines typographic descent of glyphs in the run.
- [CTRunDelegateGetWidthCallback](ctrundelegategetwidthcallback.md) — Defines a pointer to a function that determines the typographic width of glyphs in the run.
- [CTRunDelegateDeallocateCallback](ctrundelegatedeallocatecallback.md) — Defines a pointer to a function that is invoked when a CTRunDelegate object is deallocated.

### Data Types

- [CTRunDelegateCallbacks](ctrundelegatecallbacks.md) — A structure holding pointers to callbacks implemented by the run delegate.

### Constants

- [Run Delegate Versions](1498177-run-delegate-versions.md) — The version of the run delegate.

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
- [CTTextTab](cttexttab.md) — A tab in a paragraph style, storing an alignment type and location.
- [CTTypesetter](cttypesetter.md) — A typesetter which performs line layout.
