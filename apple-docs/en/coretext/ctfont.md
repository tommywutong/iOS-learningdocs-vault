---
title: CTFont
framework: Core Text
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctfont
source_url: 'https://developer.apple.com/documentation/coretext/ctfont'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfont.json'
content_hash: 'sha256:3d46bb46b4f27a26'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFont

<sub>Class</sub>

A font object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CTFont
```

## Overview

The `CTFont` opaque type represents a Core Text font object.

Font objects represent fonts to an application, providing access to characteristics of the font, such as point size, transform matrix, and other attributes. Fonts provide assistance in laying out glyphs relative to one another and are used to establish the current font when drawing in a graphics context.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Creating Fonts

- [CTFontCreateWithName](<ctfontcreatewithname(______).md>) — Returns a new font reference for the given name.
- [CTFontCreateWithNameAndOptions](<ctfontcreatewithnameandoptions(________).md>) — Returns a new font reference for the given name.
- [CTFontCreateWithFontDescriptor](<ctfontcreatewithfontdescriptor(______).md>) — Returns a new font reference that best matches the given font descriptor.
- [CTFontCreateWithFontDescriptorAndOptions](<ctfontcreatewithfontdescriptorandoptions(________).md>) — Returns a new font reference that best matches the given font descriptor.
- [CTFontCreateUIFontForLanguage](<ctfontcreateuifontforlanguage(______).md>) — Returns the special user-interface font for the given language and user-interface type.
- [CTFontCreateCopyWithAttributes](<ctfontcreatecopywithattributes(________).md>) — Returns a new font with additional attributes based on the original font.
- [CTFontCreateCopyWithSymbolicTraits](<ctfontcreatecopywithsymbolictraits(__________).md>) — Returns a new font in the same font family as the original with the specified symbolic traits.
- [CTFontCreateCopyWithFamily](<ctfontcreatecopywithfamily(________).md>) — Returns a new font in the specified family based on the traits of the original font.
- [CTFontCreateForString](<ctfontcreateforstring(______).md>) — Returns a font reference that most accurately maps the string range based on the current font.
- [CTFontCreateForStringWithLanguage](<ctfontcreateforstringwithlanguage(________).md>) — Returns a font reference that most accurately maps the string range based on the current font and language.

### Getting Font Data

- [CTFontCopyFontDescriptor](<ctfontcopyfontdescriptor(__).md>) — Returns the normalized font descriptor for the given font reference.
- [CTFontCopyAttribute](<ctfontcopyattribute(____).md>) — Returns the value associated with an arbitrary attribute of the given font.
- [CTFontGetSize](<ctfontgetsize(__).md>) — Returns the point size of the given font.
- [CTFontGetMatrix](<ctfontgetmatrix(__).md>) — Returns the transformation matrix of the given font.
- [CTFontGetSymbolicTraits](<ctfontgetsymbolictraits(__).md>) — Returns the symbolic traits of the given font.
- [CTFontCopyTraits](<ctfontcopytraits(__).md>) — Returns the traits dictionary of the given font.
- [CTFontCopyDefaultCascadeListForLanguages](<ctfontcopydefaultcascadelistforlanguages(____).md>) — Retrieves an ordered list of font substitution preferences.

### Getting Font Names

- [CTFontCopyPostScriptName](<ctfontcopypostscriptname(__).md>) — Returns the PostScript name of the given font.
- [CTFontCopyFamilyName](<ctfontcopyfamilyname(__).md>) — Returns the family name of the given font.
- [CTFontCopyFullName](<ctfontcopyfullname(__).md>) — Returns the full name of the given font.
- [CTFontCopyDisplayName](<ctfontcopydisplayname(__).md>) — Returns the display name of the given font.
- [CTFontCopyName](<ctfontcopyname(____).md>) — Returns a reference to the requested name of the given font.
- [CTFontCopyLocalizedName](<ctfontcopylocalizedname(______).md>) — Returns a reference to a localized name for the given font.

### Working With Encoding

- [CTFontCopyCharacterSet](<ctfontcopycharacterset(__).md>) — Returns the Unicode character set of the font.
- [CTFontGetStringEncoding](<ctfontgetstringencoding(__).md>) — Returns the best string encoding for legacy format support.
- [CTFontCopySupportedLanguages](<ctfontcopysupportedlanguages(__).md>) — Returns an array of languages supported by the font.

### Getting Font Metrics

- [CTFontGetAscent](<ctfontgetascent(__).md>) — Returns the scaled font-ascent metric of the given font.
- [CTFontGetDescent](<ctfontgetdescent(__).md>) — Returns the scaled font-descent metric of the given font.
- [CTFontGetLeading](<ctfontgetleading(__).md>) — Returns the scaled font-leading metric of the given font.
- [CTFontGetUnitsPerEm](<ctfontgetunitsperem(__).md>) — Returns the units-per-em metric of the given font.
- [CTFontGetGlyphCount](<ctfontgetglyphcount(__).md>) — Returns the number of glyphs of the given font.
- [CTFontGetBoundingBox](<ctfontgetboundingbox(__).md>) — Returns the scaled bounding box of the given font.
- [CTFontGetUnderlinePosition](<ctfontgetunderlineposition(__).md>) — Returns the scaled underline position of the given font.
- [CTFontGetUnderlineThickness](<ctfontgetunderlinethickness(__).md>) — Returns the scaled underline-thickness metric of the given font.
- [CTFontGetSlantAngle](<ctfontgetslantangle(__).md>) — Returns the slant angle of the given font.
- [CTFontGetCapHeight](<ctfontgetcapheight(__).md>) — Returns the cap-height metric of the given font.
- [CTFontGetXHeight](<ctfontgetxheight(__).md>) — Returns the x-height metric of the given font.

### Getting Glyph Data

- [CTFontCreatePathForGlyph](<ctfontcreatepathforglyph(______).md>) — Creates a path for the specified glyph.
- [CTFontGetGlyphWithName](<ctfontgetglyphwithname(____).md>) — Returns the glyph for the specified name.
- [CTFontGetBoundingRectsForGlyphs](<ctfontgetboundingrectsforglyphs(__________).md>) — Calculates the bounding rects for an array of glyphs and returns the overall bounding rectangle for the glyph run.
- [CTFontGetAdvancesForGlyphs](<ctfontgetadvancesforglyphs(__________).md>) — Calculates the advances for an array of glyphs and returns the summed advance.
- [CTFontGetOpticalBoundsForGlyphs](<ctfontgetopticalboundsforglyphs(__________).md>) — Calculates the optical bounds for an array of glyphs and returns the overall optical bounds for the run.
- [CTFontGetVerticalTranslationsForGlyphs](<ctfontgetverticaltranslationsforglyphs(________).md>) — Calculates the offset from the default (horizontal) origin to the vertical origin for an array of glyphs.

### Working With Font Variations

- [CTFontCopyVariationAxes](<ctfontcopyvariationaxes(__).md>) — Returns an array of variation axes.
- [CTFontCopyVariation](<ctfontcopyvariation(__).md>) — Returns a variation dictionary from the font reference.

### Getting Font Features

- [CTFontCopyFeatures](<ctfontcopyfeatures(__).md>) — Returns an array of font features.
- [CTFontCopyFeatureSettings](<ctfontcopyfeaturesettings(__).md>) — Returns an array of font feature-setting tuples.

### Working with Glyphs

- [CTFontGetGlyphsForCharacters](<ctfontgetglyphsforcharacters(________).md>) — Performs basic character-to-glyph mapping.
- [CTFontDrawGlyphs](<ctfontdrawglyphs(__________).md>) — Renders the given glyphs of a font at the specified positions in the supplied graphics context.
- [CTFontGetLigatureCaretPositions](<ctfontgetligaturecaretpositions(________).md>) — Returns caret positions within a glyph.

### Converting Fonts

- [CTFontCopyGraphicsFont](<ctfontcopygraphicsfont(____).md>) — Returns a Core Graphics font reference and attributes.
- [CTFontCreateWithGraphicsFont](<ctfontcreatewithgraphicsfont(________).md>) — Creates a new font reference from an existing Core Graphics font reference.
- [CTFontGetPlatformFont](<ctfontgetplatformfont(____).md>) — Returns an ATS font reference and attributes. _(deprecated)_
- [CTFontCreateWithPlatformFont](<ctfontcreatewithplatformfont(________).md>) — Creates a new font reference from an ATS font reference. _(deprecated)_
- [CTFontCreateWithQuickdrawInstance](<ctfontcreatewithquickdrawinstance(________).md>) — Returns a font reference for the given QuickDraw instance. _(deprecated)_

### Getting Font Table Data

- [CTFontCopyAvailableTables](<ctfontcopyavailabletables(____).md>) — Returns an array of font table tags.
- [CTFontCopyTable](<ctfontcopytable(______).md>) — Returns a reference to the font table data.

### Getting the Type Identifier

- [CTFontGetTypeID](<ctfontgettypeid().md>) — Returns the type identifier for Core Text font references.

### Global Variables

- [Name Specifier Constants](name-specifier-constants.md) — Name specifier constants provide access to the different names associated with a font.
- [Font Variation Axis Dictionary Keys](font-variation-axis-dictionary-keys.md) — These constants provide keys to font variation axis dictionary values.
- [Font Feature Constants](font-feature-constants.md) — These constants provide keys to font feature dictionary values.

### Enumerations

- [CTFontUIFontType](ctfontuifonttype.md) — Constants that represent the specific user-interface purpose to specify for font creation.
- [CTFontTableTag](ctfonttabletag.md) — Font table tags provide access to font table data.
- [CTFontTableOptions](ctfonttableoptions.md) — Constants that describe font table options.
- [CTFontOptions](ctfontoptions.md) — Options for font creation and descriptor matching.

### Initializers

- [init(_:size:)](<ctfont/init(__size_)-3do9m.md>)
- [init(_:size:)](<ctfont/init(__size_)-6lcja.md>)
- [init(_:size:)](<ctfont/init(__size_)-8bj7b.md>)
- [init(_:size:language:)](<ctfont/init(__size_language_).md>)
- [init(_:transform:)](<ctfont/init(__transform_)-3sscp.md>)
- [init(_:transform:)](<ctfont/init(__transform_)-a23v.md>)
- [init(font:string:range:)](<ctfont/init(font_string_range_).md>)
- [init(font:string:range:language:)](<ctfont/init(font_string_range_language_).md>)

## See Also

### Opaque Types

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
- [CTTypesetter](cttypesetter.md) — A typesetter which performs line layout.
