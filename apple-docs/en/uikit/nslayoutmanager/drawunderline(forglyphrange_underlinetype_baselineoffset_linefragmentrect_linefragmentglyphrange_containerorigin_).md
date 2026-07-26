---
title: 'drawUnderline(forGlyphRange:underlineType:baselineOffset:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nslayoutmanager/drawunderline(forglyphrange:underlinetype:baselineoffset:linefragmentrect:linefragmentglyphrange:containerorigin:)'
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanager/drawunderline(forglyphrange:underlinetype:baselineoffset:linefragmentrect:linefragmentglyphrange:containerorigin:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanager/drawunderline%28forglyphrange%3Aunderlinetype%3Abaselineoffset%3Alinefragmentrect%3Alinefragmentglyphrange%3Acontainerorigin%3A%29.json'
content_hash: 'sha256:c179de44c617d031'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutManager](../nslayoutmanager.md)

# drawUnderline(forGlyphRange:underlineType:baselineOffset:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:)

<sub>Instance Method</sub>

Draws underlining for the glyphs in a specified range.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func drawUnderline(forGlyphRange glyphRange: NSRange, underlineType underlineVal: NSUnderlineStyle, baselineOffset: CGFloat, lineFragmentRect lineRect: CGRect, lineFragmentGlyphRange lineGlyphRange: NSRange, containerOrigin: CGPoint)
```

## Parameters

- `glyphRange` — A range of glyphs, which must belong to a single line fragment rectangle (as returned by [- lineFragmentRectForGlyphAtIndex:effectiveRange:](<linefragmentrect(forglyphat_effectiverange_).md>)).

- `underlineVal` — The style of underlining to draw. This value is a mask derived from the value for [NSUnderlineStyleAttributeName](../nsunderlinestyleattributename.md)—for example, `(NSUnderlinePatternDash | NSUnderlineStyleThick)`. Subclasses can define custom underlining styles.

- `baselineOffset` — Specifies the distance from the bottom of the bounding box of the specified glyphs in the specified range to their baseline.

- `lineRect` — The line fragment rectangle containing the glyphs to draw underlining for.

- `lineGlyphRange` — The range of all glyphs within `lineRect`.

- `containerOrigin` — The origin of the `lineRectNSTextContainer` in its `NSTextView`.

## Discussion

This method is invoked automatically by [- underlineGlyphRange:underlineType:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:](<underlineglyphrange(__underlinetype_linefragmentrect_linefragmentglyphrange_containerorigin_).md>); you should rarely need to invoke it directly. This method’s `underlineVal` parameter does not take account of any setting for [NSUnderlineByWordMask](../../appkit/nsunderlinebywordmask.md) because that’s taken care of by [- underlineGlyphRange:underlineType:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:](<underlineglyphrange(__underlinetype_linefragmentrect_linefragmentglyphrange_containerorigin_).md>).

## See Also

### Drawing

- [- drawBackgroundForGlyphRange:atPoint:](<drawbackground(forglyphrange_at_).md>) — Draws background marks for the specified glyphs, which must lie completely within a single text container.
- [- drawGlyphsForGlyphRange:atPoint:](<drawglyphs(forglyphrange_at_).md>) — Draws the specified glyphs, which must lie completely within a single text container.
- [- drawStrikethroughForGlyphRange:strikethroughType:baselineOffset:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:](<drawstrikethrough(forglyphrange_strikethroughtype_baselineoffset_linefragmentrect_linefragmentglyphrange_containerorigin_).md>) — Draws a strikethrough for the specified glyphs.
- [- fillBackgroundRectArray:count:forCharacterRange:color:](<fillbackgroundrectarray(__count_forcharacterrange_color_).md>) — Fills background rectangles with a color.
- [- showCGGlyphs:positions:count:font:textMatrix:attributes:inContext:](<showcgglyphs(__positions_count_font_textmatrix_attributes_in_).md>) — Renders the glyphs at the specified positions, using the specified attributes.
- [- strikethroughGlyphRange:strikethroughType:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:](<strikethroughglyphrange(__strikethroughtype_linefragmentrect_linefragmentglyphrange_containerorigin_).md>) — Calculates and draws strikethrough for the specified glyphs.
- [- underlineGlyphRange:underlineType:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:](<underlineglyphrange(__underlinetype_linefragmentrect_linefragmentglyphrange_containerorigin_).md>) — Calculates subranges to underline for the specified glyphs and draws the underlining as appropriate.
