---
title: CTFontCollection
framework: Core Text
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctfontcollection
source_url: 'https://developer.apple.com/documentation/coretext/ctfontcollection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontcollection.json'
content_hash: 'sha256:70f0e2c0b0c52bf6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontCollection

<sub>Class</sub>

A font collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CTFontCollection
```

## Overview

A font collection represents a group of font descriptors taken together as a single object.

Font collections provide the capabilities of font enumeration, access to global and custom font collections, and access to the font descriptors comprising the collection.

## Relationships

- **Inherited By**: [CTMutableFontCollection](ctmutablefontcollection.md)

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Creating Font Collections

- [CTFontCollectionCreateFromAvailableFonts](<ctfontcollectioncreatefromavailablefonts(__).md>) — Returns a new font collection containing all available fonts.
- [CTFontCollectionCreateWithFontDescriptors](<ctfontcollectioncreatewithfontdescriptors(____).md>) — Returns a new font collection based on the given array of font descriptors.
- [CTFontCollectionCreateCopyWithFontDescriptors](<ctfontcollectioncreatecopywithfontdescriptors(______).md>) — Returns a copy of the original collection augmented with the given new font descriptors.
- [CTFontCollectionCreateMutableCopy](<ctfontcollectioncreatemutablecopy(__).md>) — Creates a mutable copy of the original collection.

### Excluding and Including Font Descriptors

- [CTFontCollectionCopyExclusionDescriptors](<ctfontcollectioncopyexclusiondescriptors(__).md>) — Retrieves the array of descriptors to exclude from the match.
- [CTFontCollectionCopyQueryDescriptors](<ctfontcollectioncopyquerydescriptors(__).md>) — Retrieves the array of descriptors for font matching.
- [CTFontCollectionSetExclusionDescriptors](<ctfontcollectionsetexclusiondescriptors(____).md>) — Replaces the array of descriptors to exclude from the match.
- [CTFontCollectionSetQueryDescriptors](<ctfontcollectionsetquerydescriptors(____).md>) — Replaces the array of descriptors for font matching.

### Getting Font Descriptors

- [CTFontCollectionCreateMatchingFontDescriptors](<ctfontcollectioncreatematchingfontdescriptors(__).md>) — Returns an array of font descriptors matching the collection.
- [CTFontCollectionCreateMatchingFontDescriptorsWithOptions](<ctfontcollectioncreatematchingfontdescriptorswithoptions(____).md>) — Creates an array of font descriptors that match the specified collection.
- [CTFontCollectionCreateMatchingFontDescriptorsSortedWithCallback](<ctfontcollectioncreatematchingfontdescriptorssortedwithcallback(______).md>) — Returns the array of matching font descriptors sorted with the callback function.
- [CTFontCollectionCreateMatchingFontDescriptorsForFamily](<ctfontcollectioncreatematchingfontdescriptorsforfamily(______).md>) — Retrieves an array of font descriptors that match the specified family, one descriptor for each style in the collection.
- [CTFontCollectionSortDescriptorsCallback](ctfontcollectionsortdescriptorscallback.md) — The collection sorting callback type.

### Get Font Descriptor Attributes

- [CTFontCollectionCopyFontAttribute](<ctfontcollectioncopyfontattribute(______).md>) — Retrieves an array of font descriptor attribute values.
- [CTFontCollectionCopyFontAttributes](<ctfontcollectioncopyfontattributes(______).md>) — Retrieves an array of dictionaries containing font descriptor attribute values.

### Getting the Type Identifier

- [CTFontCollectionGetTypeID](<ctfontcollectiongettypeid().md>) — Returns the type identifier for Core Text font collection references.

### Data Types

- [CTMutableFontCollection](ctmutablefontcollection.md) — A reference to a mutable font collection.

### Constants

- [kCTFontCollectionRemoveDuplicatesOption](kctfontcollectionremoveduplicatesoption.md)
- [CTFontCollectionCopyOptions](ctfontcollectioncopyoptions.md) — Option bits for use with CTFontCollectionCopyFontAttribute(s).

## See Also

### Opaque Types

- [CTFont](ctfont.md) — A font object.
- [CTFontDescriptor](ctfontdescriptor.md) — A font descriptor.
- [CTFrame](ctframe.md) — A frame.
- [CTFramesetter](ctframesetter.md) — Generate text frames.
- [CTGlyphInfo](ctglyphinfo.md) — Override a font’s specified mapping from Unicode to the glyph ID.
- [CTLine](ctline.md) — A line of text.
- [CTParagraphStyle](ctparagraphstyle.md) — Paragraph or ruler attributes in an attributed string.
- [CTRun](ctrun.md) — A glyph run.
- [CTRunDelegate](ctrundelegate.md) — A run delegate.
- [CTTextTab](cttexttab.md) — A tab in a paragraph style, storing an alignment type and location.
- [CTTypesetter](cttypesetter.md) — A typesetter which performs line layout.
