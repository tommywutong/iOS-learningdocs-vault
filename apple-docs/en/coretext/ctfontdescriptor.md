---
title: CTFontDescriptor
framework: Core Text
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctfontdescriptor
source_url: 'https://developer.apple.com/documentation/coretext/ctfontdescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontdescriptor.json'
content_hash: 'sha256:5edc6562b622b14a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontDescriptor

<sub>Class</sub>

A font descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CTFontDescriptor
```

## Overview

A font descriptor is a dictionary of attributes (such as name, point size, and variation) that can completely specify a font.

A font descriptor can be an incomplete specification, in which case the system chooses the most appropriate font to match the given attributes.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Creating Font Descriptors

- [CTFontDescriptorCreateWithNameAndSize](<ctfontdescriptorcreatewithnameandsize(____).md>) — Creates a new font descriptor with the provided PostScript name and size.
- [CTFontDescriptorCreateWithAttributes](<ctfontdescriptorcreatewithattributes(__).md>) — Creates a new font descriptor reference from a dictionary of attributes.
- [CTFontDescriptorCreateCopyWithAttributes](<ctfontdescriptorcreatecopywithattributes(____).md>) — Creates a copy of the original font descriptor with new attributes.
- [CTFontDescriptorCreateCopyWithVariation](<ctfontdescriptorcreatecopywithvariation(______).md>) — Creates a copy of the original font descriptor with a new variation instance.
- [CTFontDescriptorCreateCopyWithFeature](<ctfontdescriptorcreatecopywithfeature(______).md>) — Copies a font descriptor with new feature settings.
- [CTFontDescriptorCreateCopyWithFamily](<ctfontdescriptorcreatecopywithfamily(____).md>) — Creates a copy of the font descriptor in the specified family based on the traits of the original.
- [CTFontDescriptorCreateCopyWithSymbolicTraits](<ctfontdescriptorcreatecopywithsymbolictraits(______).md>) — Creates a copy of the font descriptor with the specified symbolic traits as the original.
- [CTFontDescriptorCreateMatchingFontDescriptors](<ctfontdescriptorcreatematchingfontdescriptors(____).md>) — Returns an array of normalized font descriptors matching the provided descriptor.
- [CTFontDescriptorCreateMatchingFontDescriptor](<ctfontdescriptorcreatematchingfontdescriptor(____).md>) — Returns the single preferred matching font descriptor based on the original descriptor and system precedence.

### Getting Attributes

- [CTFontDescriptorCopyAttributes](<ctfontdescriptorcopyattributes(__).md>) — Returns the attributes dictionary of the font descriptor.
- [CTFontDescriptorCopyAttribute](<ctfontdescriptorcopyattribute(____).md>) — Returns the value associated with an arbitrary attribute.
- [CTFontDescriptorCopyLocalizedAttribute](<ctfontdescriptorcopylocalizedattribute(______).md>) — Returns a localized value for the requested attribute, if available.

### Getting the Font Descriptor Type

- [CTFontDescriptorGetTypeID](<ctfontdescriptorgettypeid().md>) — Returns the type identifier for Core Text font descriptor references.

### Accessing Font Attributes

- [Font Attributes](font-attributes.md) — The keys for accessing font attributes from a font descriptor.
- [CTFontOrientation](ctfontorientation.md) — The intended rendering orientation of the font for obtaining glyph metrics.
- [CTFontFormat](ctfontformat.md) — The recognized format of the font.
- [CTFontPriority](ctfontpriority.md) — The priority of font descriptors when resolving duplicates and sorting match results.

### Accessing Font Traits

- [Font Traits](font-traits.md) — The keys for accessing font traits from a font descriptor.
- [Font Class Mask Shift Constants](font-class-mask-shift-constants.md) — These constants represent the font class mask shift.
- [CTFontSymbolicTraits](ctfontsymbolictraits.md) — The symbolic representation of stylistic font attributes.
- [CTFontStylisticClass](ctfontstylisticclass.md) — The stylistic class values of the font.

## See Also

### Opaque Types

- [CTFont](ctfont.md) — A font object.
- [CTFontCollection](ctfontcollection.md) — A font collection.
- [CTFrame](ctframe.md) — A frame.
- [CTFramesetter](ctframesetter.md) — Generate text frames.
- [CTGlyphInfo](ctglyphinfo.md) — Override a font’s specified mapping from Unicode to the glyph ID.
- [CTLine](ctline.md) — A line of text.
- [CTParagraphStyle](ctparagraphstyle.md) — Paragraph or ruler attributes in an attributed string.
- [CTRun](ctrun.md) — A glyph run.
- [CTRunDelegate](ctrundelegate.md) — A run delegate.
- [CTTextTab](cttexttab.md) — A tab in a paragraph style, storing an alignment type and location.
- [CTTypesetter](cttypesetter.md) — A typesetter which performs line layout.
