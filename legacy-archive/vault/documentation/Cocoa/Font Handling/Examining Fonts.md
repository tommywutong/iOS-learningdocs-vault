---
title: Font Handling
apple_id: 10000093i
resource_type: Guide
platform: macOS
topic: Data Management
technology: AppKit
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/FontHandling/Tasks/ExaminingFonts.html
archived_at: '2026-07-15T07:15:47.946019Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Font Handling](Introduction%20to%20Font%20Handling.md)


[Next](Customizing%20the%20Font%20Conversion%20System.md)[Previous](Converting%20Fonts%20Manually.md)

# Examining Fonts

In addition
to converting fonts, NSFontManager provides information on which
fonts are available to the application and on the characteristics
of any given font. The `availableFonts` method
returns an array of the names of all fonts available. The `availableFontNamesWithTraits:` method
filters the available fonts based on a font trait mask.

There are three methods for examining individual fonts. The `fontNamed:HasTraits:` method
returns `true` if the font matches
the trait mask provided. The `traitsOfFont:` method
returns a trait mask for a given font. The `weightOfFont:` method
returns an approximate ranking of a font’s weight on a scale of
0–15, where 0 is the lightest possible weight, 5 is Normal or
Book weight, 9 is the equivalent of Bold, and 15 is the heaviest possible
(often called Black or Ultra Black).

[Next](Customizing%20the%20Font%20Conversion%20System.md)[Previous](Converting%20Fonts%20Manually.md)

