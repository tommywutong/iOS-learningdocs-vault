---
title: Font Handling
apple_id: 10000093i
resource_type: Guide
platform: macOS
topic: Data Management
technology: AppKit
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/FontHandling/Concepts/GlyphLayout.html
archived_at: '2026-07-15T07:15:42.926680Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Font Handling](Introduction%20to%20Font%20Handling.md)


[Next](Special%20Glyphs.md)[Previous](Characters%20and%20Glyphs.md)

# Calculating Glyph Layout

The Cocoa text system handles many complex aspects of laying
out glyphs. If you need to calculate layout for your own purposes,
you can use methods defined by NSFont. There are three basic kinds
of glyph layout, although Java supports only overstruck:

- Sequential, for running text
- 

  Overstruck, for diacritics and other nonspacing marks
- Stacked, for certain non-Western scripts.

Sequential glyph layout is
supported by the method `positionOfGlyph:precededByGlyph:isNominal:`,
which is available only in Objective-C. This method calculates the
position of a glyph relative to glyph preceding it, using the glyph’s width
and kerning information if they’re available. This is the most
straightforward kind of glyph layout.

Overstruck glyph layout is
the most complex, as it requires detailed information about placement
of many kinds of modifying marks. Generally, you have two characters:

- 

  A base glyph, which may be a character such as “a”
- 

  A nonspacing mark, which may be a diacritical mark such as an acute
  accent (‘) or a cedilla (¸)

Cocoa gives you methods for combining the two characters,
depending on whether the combination is a common one that the font
has metrics for or whether the combination is an unusual one that
you need to create on the fly. Try these methods in the following
order, to get the best result:

- 

  In Objective-C, to see if the font has metrics placing
  the nonspacing mark directly over the base glyph, use the method `positionOfGlyph:struckOverGlyph:metricsExist:` and check
  the value returned in the _metricsExist_ argument.
- 

  In Objective-C, to see if the font has metrics for placing
  the nonspacing mark over the base glyph’s bounding rectangle,
  use the method `positionOfGlyph:struckOverRect:metricsExist:` and
  check the value returned in the _metricsExist_ argument.
  Use the method `boundingRectForGlyph:` to
  get the bounding rect for the base glyph. Note that NSFont always sets _metricsExist_ to `NO` and
  that this method is useful only if you’re using a subclass of
  NSFont that overrides this method.
- To place the nonspacing mark over the base glyph in a legible
  but not necessarily pleasing manner, use the method `positionOfGlyph:forCharacter:struckOverRect:` (`positionOfGlyphForCharacterStruckOverRect` in
  Java). This method handles all the common nonspacing marks, such
  as an acute accent, tilde, or cedilla, for Latin script. Use the
  method `boundingRectForGlyph:` (`boundingRectForGlyph` in
  Java) to get the bounding rectangle for the base glyph.
- 

  To place a nonspacing mark over a base glyph of another font,
  also use the method `positionOfGlyph:forCharacter:struckOverRect:` (`positionOfGlyphForCharacterStruckOverRect` in
  Java). Use the method `boundingRectForGlyph:` (`boundingRectForGlyph` in
  Java) to get the bounding rectangle for the base glyph.

In Objective-C, if you need to place several nonspacing marks
with respect to a base glyph, use the method `positionsForCompositeSequence:numberOfGlyphs:pointArray:`.
This method accepts a C array containing the base glyph followed
by all of its nonspacing marks and calculates the positions for
as many as of the marks as it can. To place the marks that this
method can’t handle, use the methods described above.

Stacked glyph layout is supported
by the method `positionOfGlyph:withRelation:toBaseGlyph:totalAdvancement:metricsExist:`,
which is available only in Objective-C. Stacked glyphs often have
special compressed forms, which standard font metrics don’t account
for. NSFont’s implementation of this method simply abuts the bounding
rectangles of the two glyphs for approximate layout of the individual glyphs.
Subclasses of NSFont can override this method to access any extra
metrics information for more sophisticated layout of stacked glyphs.

[Next](Special%20Glyphs.md)[Previous](Characters%20and%20Glyphs.md)

