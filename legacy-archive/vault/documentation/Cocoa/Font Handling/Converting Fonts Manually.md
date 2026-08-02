---
title: Font Handling
apple_id: 10000093i
resource_type: Guide
platform: macOS
topic: Data Management
technology: AppKit
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/FontHandling/Tasks/ConvertingFontsManually.html
archived_at: '2026-07-15T07:15:45.939865Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Font Handling](Introduction%20to%20Font%20Handling.md)


[Next](Examining%20Fonts.md)[Previous](Responding%20to%20Font%20Changes.md)

# Converting Fonts Manually

NSFontManager defines
a number of methods for explicitly converting particular traits and characteristics
of a font. Table 1 lists these conversion methods.

__Table 1__  Font conversion methods

| Objective-C Methods | Java Methods |
| `convertFont:toFace:` | `convertFontToFace` |
| `convertFont:toFamily:` | `convertFontToFamily` |
| `convertFont:toHaveTrait:` | `convertFontToFamily` |
| `convertFont:toNotHaveTrait:` | `convertFontToNotHaveTrait` |
| `convertFont:toSize:` | `convertFontToSize` |
| `convertWeight:ofFont:` | `convertWeight` |

Each method returns a transformed version of the font provided,
or the original font if it can’t be converted. `convertFont:toFace:` and `convertFont:toFamily:` both
alter the basic design of the font provided. The first method requires
a fully specified typeface name, such as “Times-Roman” or “Helvetica-BoldOblique”,
while the second expects only a family name, such as “Times”
or “Helvetica”.

The `convertFont:toHaveTrait:` and `convertFont:toNotHaveTrait:` methods
use trait masks to add or remove a single trait such as Italic,
Bold, Condensed, or Extended.

The `convertFont:toSize:` method
returns a font of the requested size, with all other characteristics
the same as those of the original font.

The `convertWeight:ofFont:` method
either increases or decreases the weight of the font provided, according
to a Boolean flag. Font weights are typically indicated by a series
of names, which can vary from font to font. Some go from Light to
Medium to Bold, while others have Book, SemiBold, Bold, and Black.
This method offers a uniform way of incrementing and decrementing
any font’s weight.

The default implementation of font conversion is very conservative,
making a change only if no other trait or aspect is affected. For
example, if you try to convert Helvetica Oblique 12.0 point by adding
the Bold trait, and only Helvetica Bold is available, the font isn’t converted.
You can create a subclass of NSFontManager and override the conversion methods
to perform less conservative conversion, perhaps using Helvetica
Bold in this case and losing the Oblique trait.

In addition to the font-conversion methods, NSFontManager defines `fontWithFamily:traits:weight:size:` to
construct a font with a given set of characteristics. If you don’t
care to make a subclass of NSFontManager, you can use this method
to perform approximate font conversions yourself.

[Next](Examining%20Fonts.md)[Previous](Responding%20to%20Font%20Changes.md)

