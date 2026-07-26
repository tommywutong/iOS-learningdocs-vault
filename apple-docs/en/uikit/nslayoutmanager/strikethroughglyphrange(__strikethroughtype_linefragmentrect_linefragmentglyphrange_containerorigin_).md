---
title: 'strikethroughGlyphRange(_:strikethroughType:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nslayoutmanager/strikethroughglyphrange(_:strikethroughtype:linefragmentrect:linefragmentglyphrange:containerorigin:)'
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanager/strikethroughglyphrange(_:strikethroughtype:linefragmentrect:linefragmentglyphrange:containerorigin:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanager/strikethroughglyphrange%28_%3Astrikethroughtype%3Alinefragmentrect%3Alinefragmentglyphrange%3Acontainerorigin%3A%29.json'
content_hash: 'sha256:752442a84f45e618'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutManager](../nslayoutmanager.md)

# strikethroughGlyphRange(_:strikethroughType:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:)

<sub>Instance Method</sub>

Calculates and draws strikethrough for the specified glyphs.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func strikethroughGlyphRange(_ glyphRange: NSRange, strikethroughType strikethroughVal: NSUnderlineStyle, lineFragmentRect lineRect: CGRect, lineFragmentGlyphRange lineGlyphRange: NSRange, containerOrigin: CGPoint)
```

## Parameters

- `glyphRange` — The range of glyphs for which to draw a strikethrough. The range must belong to a single line fragment rectangle (as returned by [- lineFragmentRectForGlyphAtIndex:effectiveRange:](<linefragmentrect(forglyphat_effectiverange_).md>)).

- `strikethroughVal` — The style of underlining to draw. This value is a mask derived from the value for [NSUnderlineStyleAttributeName](../nsunderlinestyleattributename.md)—for example, `(NSUnderlinePatternDash | NSUnderlineStyleThick | NSUnderlineByWordMask)`. Subclasses can define custom underlining styles.

- `lineRect` — The line fragment rectangle containing the glyphs to draw strikethrough for.

- `lineGlyphRange` — The range of all glyphs within `lineRect`.

- `containerOrigin` — The origin of the line fragment rectangle’s `NSTextContainer` in its `NSTextView`.

## Discussion

This method determines which glyphs actually need to have a strikethrough drawn based on `strikethroughVal`. After determining which glyphs to draw strikethrough on, this method invokes [- drawStrikethroughForGlyphRange:strikethroughType:baselineOffset:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:](<drawstrikethrough(forglyphrange_strikethroughtype_baselineoffset_linefragmentrect_linefragmentglyphrange_containerorigin_).md>) for each contiguous range of glyphs that requires it.

## See Also

### Drawing

- [- drawBackgroundForGlyphRange:atPoint:](<drawbackground(forglyphrange_at_).md>) — Draws background marks for the specified glyphs, which must lie completely within a single text container.
- [- drawGlyphsForGlyphRange:atPoint:](<drawglyphs(forglyphrange_at_).md>) — Draws the specified glyphs, which must lie completely within a single text container.
- [- drawStrikethroughForGlyphRange:strikethroughType:baselineOffset:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:](<drawstrikethrough(forglyphrange_strikethroughtype_baselineoffset_linefragmentrect_linefragmentglyphrange_containerorigin_).md>) — Draws a strikethrough for the specified glyphs.
- [- drawUnderlineForGlyphRange:underlineType:baselineOffset:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:](<drawunderline(forglyphrange_underlinetype_baselineoffset_linefragmentrect_linefragmentglyphrange_containerorigin_).md>) — Draws underlining for the glyphs in a specified range.
- [- fillBackgroundRectArray:count:forCharacterRange:color:](<fillbackgroundrectarray(__count_forcharacterrange_color_).md>) — Fills background rectangles with a color.
- [- showCGGlyphs:positions:count:font:textMatrix:attributes:inContext:](<showcgglyphs(__positions_count_font_textmatrix_attributes_in_).md>) — Renders the glyphs at the specified positions, using the specified attributes.
- [- underlineGlyphRange:underlineType:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:](<underlineglyphrange(__underlinetype_linefragmentrect_linefragmentglyphrange_containerorigin_).md>) — Calculates subranges to underline for the specified glyphs and draws the underlining as appropriate.
