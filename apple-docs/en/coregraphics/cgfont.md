---
title: CGFont
framework: Core Graphics
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgfont
source_url: 'https://developer.apple.com/documentation/coregraphics/cgfont'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgfont.json'
content_hash: 'sha256:d6fbbec247c0446b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGFont

<sub>Class</sub>

A set of character glyphs and layout information for drawing text.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CGFont
```

## Overview

A glyph can represent a single character (such as ‘b’), more than one character (such as the “ﬁ” ligature), or a special character such as a space. Core Graphics retrieves the glyphs for the font from ATS (Apple Type Services) and paints the glyphs based on the relevant parameters of the current graphics state.

Core Graphics provides a limited, low-level interface for drawing text. For information on text-drawing functions, see [CGContext](cgcontext.md). For full Unicode and text-layout support,  use the services provided by TextKit).

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Creating Font Objects

- [CGFontCreateWithDataProvider](<cgfont/init(__)-9aour.md>) — Creates a font object from data supplied from a data provider.
- [CGFontCreateWithFontName](<cgfont/init(__)-1p4b.md>) — Creates a font object corresponding to the font specified by a PostScript or full name.

### Examining Font Metadata

- [CGFontCopyFullName](cgfont/fullname.md) — Returns the full name associated with a font object.

### Examining Font Metrics

- [CGFontGetAscent](cgfont/ascent.md) — Returns the ascent of a font.
- [CGFontGetCapHeight](cgfont/capheight.md) — Returns the cap height of a font.
- [CGFontGetDescent](cgfont/descent.md) — Returns the descent of a font.
- [CGFontGetFontBBox](cgfont/fontbbox.md) — Returns the bounding box of a font.
- [CGFontGetItalicAngle](cgfont/italicangle.md) — Returns the italic angle of a font.
- [CGFontGetLeading](cgfont/leading.md) — Returns the leading of a font.
- [CGFontGetStemV](cgfont/stemv.md) — Returns the thickness of the dominant vertical stems of glyphs in a font.
- [CGFontGetUnitsPerEm](cgfont/unitsperem.md) — Returns the number of glyph space units per em for the provided font.
- [CGFontGetXHeight](cgfont/xheight.md) — Returns the x-height of a font.

### Working with PostScript Fonts

- [CGFontCopyPostScriptName](cgfont/postscriptname.md) — Obtains the PostScript name of a font.
- [CGFontCanCreatePostScriptSubset](<cgfont/cancreatepostscriptsubset(__).md>) — Determines whether Core Graphics can create a subset of the font in PostScript format.
- [CGFontCreatePostScriptSubset](<cgfont/createpostscriptsubset(subsetname_format_glyphs_count_encoding_).md>) — Creates a subset of the font in the specified PostScript format.
- [CGFontPostScriptFormat](cgfontpostscriptformat.md) — Possible formats for a PostScript font subset.
- [CGFontCreatePostScriptEncoding](<cgfont/createpostscriptencoding(encoding_).md>) — Creates a PostScript encoding of a font.

### Working with Font Tables

- [CGFontCopyTableTags](cgfont/tabletags.md) — Returns an array of tags that correspond to the font tables for a font.
- [CGFontCopyTableForTag](<cgfont/table(for_).md>) — Returns the font table that corresponds to the provided tag.
- [Font Table Index Values](font-table-index-values.md) — Possible values for an index into a font table.
- [Obsolete Font Table Index Values](obsolete-font-table-index-values.md) — Deprecated values for an index into a font table.

### Working with Variations

- [CGFontCreateCopyWithVariations](<cgfont/copy(withvariations_).md>) — Creates a copy of a font using a variation specification dictionary.
- [CGFontCopyVariations](cgfont/variations.md) — Returns the variation specification dictionary for a font.
- [CGFontCopyVariationAxes](cgfont/variationaxes.md) — Returns an array of the variation axis dictionaries for a font.
- [Font Variation Axis Keys](font-variation-axis-keys.md) — Keys used for a font variation axis dictionary.

### Working with Glyphs

- [CGFontGetNumberOfGlyphs](cgfont/numberofglyphs.md) — Returns the number of glyphs in a font.
- [CGFontCopyGlyphNameForGlyph](<cgfont/name(for_).md>) — Returns the glyph name of the specified glyph in the specified font.
- [CGFontGetGlyphWithGlyphName](<cgfont/getglyphwithglyphname(name_).md>) — Returns the glyph for the glyph name associated with the specified font object.
- [CGFontGetGlyphBBoxes](<cgfont/getglyphbboxes(glyphs_count_bboxes_).md>) — Get the bounding box of each glyph in an array.
- [CGFontGetGlyphAdvances](<cgfont/getglyphadvances(glyphs_count_advances_).md>) — Gets the advance width of each glyph in the provided array.
- [CGGlyph](cgglyph.md) — An index into the internal glyph table of a font.
- [kCGGlyphMax](kcgglyphmax.md) — The maximum allowed value of a [CGGlyph](cgglyph.md).
- [CGFontIndex](cgfontindex.md) — An index into a font table.
- [kCGFontIndexMax](kcgfontindexmax.md) — The maximum allowed value of a [CGFontIndex](cgfontindex.md).
- [kCGFontIndexInvalid](kcgfontindexinvalid.md) — An invalid font index (a value which never represents a valid glyph).

### Working with Core Foundation Types

- [CGFontGetTypeID](cgfont/typeid.md) — Returns the Core Foundation type identifier for Core Graphics fonts.

## See Also

### Related Documentation

- [Quartz 2D Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066)

### Colors and Fonts

- [CGColor](cgcolor.md) — A set of components that define a color, with a color space specifying how to interpret them.
- [CGColorConversionInfo](cgcolorconversioninfo.md) — An object that describes how to convert between color spaces for use by other system services.
- [CGColorSpace](cgcolorspace.md) — A profile that specifies how to interpret a color value for display.
