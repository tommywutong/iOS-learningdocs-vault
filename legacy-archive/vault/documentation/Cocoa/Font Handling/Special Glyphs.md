---
title: Font Handling
apple_id: 10000093i
resource_type: Guide
platform: macOS
topic: Data Management
technology: AppKit
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/FontHandling/Concepts/SpecialGlyphs.html
archived_at: '2026-07-15T07:15:44.431537Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Font Handling](Introduction%20to%20Font%20Handling.md)


[Next](Recording%20the%20Font%20in%20a%20Selection.md)[Previous](Calculating%20Glyph%20Layout.md)

# Special Glyphs

NSFont defines two special glyphs. `NullGlyph` indicates
no glyph at all and is useful in some layout methods for calculating
information that isn’t relative to another glyph. For example
in Objective-C, with `positionOfGlyph:precededByGlyph:isNominal:`,
you can specify `NSNullGlyph` as the
first argument to get the nominal advancement of the preceding glyph.

The other special glyph is `ControlGlyph`,
which the text system maps onto control functions such as linefeed
and tab. This glyph has no graphic representation and has no inherent advancement
of its own. Instead, the text system examines the control character underlying
the glyph to determine what kind of special layout it needs to perform.

[Next](Recording%20the%20Font%20in%20a%20Selection.md)[Previous](Calculating%20Glyph%20Layout.md)

