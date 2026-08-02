---
title: 'Managing Fonts: QuickDraw'
apple_id: TP30000982
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/Managing_FontManager/fm_glossary/fmglossary.html
archived_at: '2026-07-15T05:23:29.978550Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Managing Fonts: QuickDraw](Introduction%20to%20Managing%20Fonts-%20QuickDraw.md)


[Next](Index.md)[Previous](Document%20Revision%20History.md)

# Managing Fonts: QuickDraw Glossary

- __advance width__

  The full width of a glyph, measured from the glyph origin to the other side of the glyph, including any white space on either side.

- __application font__

  The default font for use by applications. The application font is defined by each script system.

- __ascent line__

  An imaginary horizontal line chosen by the font’s designer that aligns approximately with the tops of the uppercase letters in the font. See also [base line](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobsfvkfamzqgaydamrsgmwugsscjfbesrcd), [descent line](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobsfvkfamzqgaydamrsgmwugsscijfecq2g).

- __base line__

  An imaginary horizontal line that coincides with the bottom of each character in a font, excluding descenders (tails on letters such as p).

- __bitmapped font__

  A font made up of bitmapped glyphs. Compare [outline font](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobsfvkfamzqgaydamrsgmwugsscjjcucqse).

- __bitmapped glyph__

  A bitmap of a character designed for display at a fixed point size for a particular display device.

- __bounding box__

  The smallest rectangle that entirely encloses the pixels of a bitmapped glyph.

- __character__

  A symbol standing for a sound, syllable, or notion used in a script; one of the simple elements of a written language, for example, the lowercase letter “a” or the number “1”. Compare [character code](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobsfvkfamzqgaydamrsgmwugsscizduqrse), [glyph](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobsfvkfamzqgaydamrsgmwugsscjjceqrsh).

- __character code__

  A value representing a text character. Text is stored in memory as character codes. Each script system’s (`'KCHR'`) resource converts the virtual key codes generation by the keyboard or keypad into character codes; each script system’s fonts convert the character codes into glyphs for display or printing.

- __character encoding__

  The organization of the numeric codes that represent the characters of a character set in memory.

- __derived font__

  A font whose characteristics are partially determined by modifying an intrinsic font. A derived font might be one whose characters are scaled form an intrinsic font to achieve a desired size or are slanted to achieve an italic style.

- __descent line__

  An imaginary horizontal line that usually aligns with the bottoms of descenders (the tails on the glyphs such as “p” or “g”), and it is the same distance from the base line for every glyph in the font. See also [ascent line](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobsfvkfamzqgaydamrsgmwugsscijbuissg).

- __fixed-width font__

  A font whose characters all have the same width. Compare [proportional font](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobsfvkfamzqgaydamrsgmwugsscizbesq2k).

- __font__

  A collection of glyphs that usually have some element of design consistency such as the shapes of the counters, the design of the stem, the stroke thickness, or the use of serifs.

- __font container__

  A file used to store data for a font.

- __font depth__

  The number of bits per pixel.

- __font description__

  A table that contains data that fully describes a font.

- __font family__

  A group of outline and bitmapped fonts that share certain characteristics and a common family name.

- __font family container__

  A file used to store data for a font family.

- __font family reference__

  A reference to an opaque structure that represents a collection of fonts with the same design characteristics. It replaces the font ID and is compatible with Font Manager, QuickDraw, Resource Manager, and Script Manager functions.

- __font ID__

  (1) A font-family ID. (2) A number that identifies the resource file of a particular individual font, of type `'FONT'`, `'nfnt'`, or `'sfnt'`. The font ID is no longer used in Font Manager functions, as it has been replaced by the [font family reference](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobsfvkfamzqgaydamrsgmwugsscjfcuorcj).

- __font family instance__

  A font family reference and Quick Draw style that together defines an outline or bitmapped font that is a member of a font family.

- __filter__

  In the Font Manger, a filter restricts the scope of the enumeration and activation function to the font families and fonts that match a particular technology, font container, or generation tag.

- __font name__

  (1) The name, such as Geneva or Kyoto, given to a font family to distinguish it from other font families. (2) A set of specific information in a font object about a font, such as its family name, style, copyright date, version, and manufacturer. Some font names are used to build menus in an application, whereas other names are used to identify the font uniquely.

- __font object__

  A specific outline font without regard to family.

- __font rectangle__

  The smallest rectangle enclosing all the glyphs in a font if the images are all superimposed over the same glyph origin.

- __font reference__

  A reference to an opaque structure that represents a font object.

- __font scaling__

  The process of changing a glyph from one size or shape to another. The Font Manager can scale bitmapped and outline fonts by changing both sizes and shapes of glyphs.

- __font scaling factors__

  Ratios that indicate how the Font Manager should scale a glyph in the vertical and horizontal directions.

- __font size__

  The size of the glyphs in a font in points; nominally a measure of the distance from the base line of one line of text to the base line of the next line or single-spaced text.

- __font technology__

  A methodology used to store and image fonts, such as PostScript or TrueType.

- __generation count__

  A value used to track changes to the font database. Any operation that adds, deletes, or modifies one or more font family or font references triggers an update of a global generation count.

- __global width table__

  A data structure that stores information about fractional glyph widths.

- __glyph__

  The distinct visual representation of a character in a form that a screen or printer can display. A glyph may represent one character (the lowercase a), more than one character (the fi ligature), part of a character (the dot over an i), or a nonprinting character (the space character). See also [character](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobsfvkfamzqgaydamrsgmwugsscivcuiq2e).

- __glyph origin__

  The point on a base line used as a reference location for drawing a glyph.

- __kerning__

  The process of drawing part of a glyph so that is overlaps another glyph.

- __imaging system__

  The system used to render text or graphics.

- __internal representation__

  The structure and organization used to represent objects, such as font objects, in the operating system.

- __intrinsic font__

  A font whose characteristics are entirely defined in a `'FONT'` or `'NFNT'` resource. The plain-style font of any family is an intrinsic font. Other styles may or may not be intrinsic. Compare [derived font](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobsfvkfamzqgaydamrsgmwugsscijdeuskh).

- __intrinsic style__

  See [intrinsic font](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobsfvkfamzqgaydamrsgmwugsscirduorsg).

- __leading (pronounced “LED-ing”)__

  The amount of blank vertical space between the descent line of one line of text and the ascent line of the next line of single-space text. In early typesetting, strips of lead were placed between lines of type for spacing, hence the term. See also [line spacing](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobsfvkfamzqgaydamrsgmwugssci5bumqsg).

- __left-side bearing__

  The white space between the glyph origin and the visible beginning of the glyph.

- __line spacing__

  The vertical distance between two lines of type, measured from base line to base line. For example, 10/12 indicates 10-point type with 12 points base to base (that is, with 2 points of leading).

- __maximum-y value__

  The highest location on the vertical axis; it corresponds to the tallest glyph in a font

- __minimum-y value__

  The lowest location on the vertical axis; it corresponds to the bottom of the longest descender in a font.

- __missing-character glyph__

  The glyph in a font that is drawn when no glyph is defined for a character code in a font.

- __monospaced font__

  See [fixed-width font](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobsfvkfamzqgaydamrsgmwugsscivdekq2e).

- __off-curve point__

  An outline point between two on-curve points that determines the curve of the line between the two on-curve points. A Bézier curve is defined by all three points.

- __on-curve point__

  One of the outline points that determines the shape of a Bézier curve. Two on-curve points and one off-curve point are required to define the curve.

- __outline font__

  A font made up of outline glyphs in a particular typeface and style, with no size restriction. The Font Manager can generate thousands of point sizes from the same outline font.

- __point__

  A unit used to measure font size. Traditionally, there are 72.27 points per inch. However, QuickDraw and the PostScript language define 1 point to be 1/72 of an inch, so there are exactly 72 points per inch in the Mac OS.

- __proportional font__

  Any font in which different characters have different widths; thus, the space taken up by words having the same number of letters can vary.

- __QuickDraw style__

  The set of styles supported by QuickDraw—bold, italic, underline, outline, shadow, condense, and extend.

- __resource__

  Data of any kind stored in a defined format in a file’s resource fork and managed by the Resource Manager.

- __resource fork entries__

  Code or noncode resource entries in a resource fork.

- __resource identifier__

  An integer that identifies a specific resource of a given type.

- __script system__

  A collection of software facilities that provides for the representation of a specific writing system. It consists of a set of keyboard resources, a set of international resources, one or more fonts, and possibly a script system extension (1-byte or 2-byte). Scripts systems include Roman, Japanese, Arabic, Traditional Chinese, Simplified Chinese, Hebrew, Greek, Thai, and Korean. Types of script systems include 1-byte simple, 1-byte complex, and 2-byte.

- __style__

  A visual attribute, other than size, applied as a systematic variation to the plain (unstyled) characteristics of a font glyph. For example bold, italic, underline, outline, shadow, condense, and extend.

- __system font__

  The font used to display text in menus, dialog boxes, alert boxes, and so forth in a given script system.

- __suitcase file__

  A traditional packaging mechanism for Mac OS fonts that usually contains bitmapped and outline font data as well as family-wide information, such as font metrics.

- __table directory__

  A table that contains data for registering fonts with the operating system.

[Next](Index.md)[Previous](Document%20Revision%20History.md)

