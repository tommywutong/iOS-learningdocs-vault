---
title: 'fillBackgroundRectArray(_:count:forCharacterRange:color:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nslayoutmanager/fillbackgroundrectarray(_:count:forcharacterrange:color:)'
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanager/fillbackgroundrectarray(_:count:forcharacterrange:color:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanager/fillbackgroundrectarray%28_%3Acount%3Aforcharacterrange%3Acolor%3A%29.json'
content_hash: 'sha256:f239650208673ff6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutManager](../nslayoutmanager.md)

# fillBackgroundRectArray(_:count:forCharacterRange:color:)

<sub>Instance Method</sub>

Fills background rectangles with a color.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func fillBackgroundRectArray(_ rectArray: UnsafePointer<CGRect>, count rectCount: Int, forCharacterRange charRange: NSRange, color: UIColor)
```

## Parameters

- `rectArray` — The array of rectangles to fill.

- `rectCount` — The number of rectangles in `rectArray`.

- `charRange` — The range of characters whose background rectangles are filled.

- `color` — The fill color.

## Discussion

This is the primitive method used by [- drawBackgroundForGlyphRange:atPoint:](<drawbackground(forglyphrange_at_).md>), providing a finer-grained override point for actually filling rectangles with a particular background color for a background color attribute, a selected or marked range highlight, a block decoration, or any other rectangle fill needed by that method. As with [showPackedGlyphs:length:glyphRange:atPoint:font:color:printingAdjustment:](../../appkit/nslayoutmanager/showpackedglyphs_length_glyphrange_atpoint_font_color_printingadjustment_.md), the `charRange` and `color` parameters are passed in merely for informational purposes; the color is already set in the graphics state. If for any reason you modify it, you must restore it before returning from this method.

This method operates in terms of character ranges, because the relevant attributes are expressed on characters, and they don’t always lie on glyph boundaries—for example, when one character of an “fi” ligature is highlighted.

You should never call this method, but you might override it. The default implementation simply fills the rectangles in the specified array. The graphics operation used for this fill is controlled by a link check; for compatibility reasons, it is [NSCompositeCopy](../../appkit/nscompositecopy.md) for applications linked prior to OS X v10.6 and [NSCompositeSourceOver](../../appkit/nscompositesourceover.md) for applications linked on macOS 10.6 or later. Applications can control the operation used, or modify the drawing, by overriding this method in an `NSLayoutManager` subclass.

## See Also

### Drawing

- [- drawBackgroundForGlyphRange:atPoint:](<drawbackground(forglyphrange_at_).md>) — Draws background marks for the specified glyphs, which must lie completely within a single text container.
- [- drawGlyphsForGlyphRange:atPoint:](<drawglyphs(forglyphrange_at_).md>) — Draws the specified glyphs, which must lie completely within a single text container.
- [- drawStrikethroughForGlyphRange:strikethroughType:baselineOffset:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:](<drawstrikethrough(forglyphrange_strikethroughtype_baselineoffset_linefragmentrect_linefragmentglyphrange_containerorigin_).md>) — Draws a strikethrough for the specified glyphs.
- [- drawUnderlineForGlyphRange:underlineType:baselineOffset:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:](<drawunderline(forglyphrange_underlinetype_baselineoffset_linefragmentrect_linefragmentglyphrange_containerorigin_).md>) — Draws underlining for the glyphs in a specified range.
- [- showCGGlyphs:positions:count:font:textMatrix:attributes:inContext:](<showcgglyphs(__positions_count_font_textmatrix_attributes_in_).md>) — Renders the glyphs at the specified positions, using the specified attributes.
- [- strikethroughGlyphRange:strikethroughType:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:](<strikethroughglyphrange(__strikethroughtype_linefragmentrect_linefragmentglyphrange_containerorigin_).md>) — Calculates and draws strikethrough for the specified glyphs.
- [- underlineGlyphRange:underlineType:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:](<underlineglyphrange(__underlinetype_linefragmentrect_linefragmentglyphrange_containerorigin_).md>) — Calculates subranges to underline for the specified glyphs and draws the underlining as appropriate.
